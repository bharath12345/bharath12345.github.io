---
layout: post
title: "Few days with Apache Cassandra"
category: posts
published: false
---

Few years ago I was a product developer at a big software (but non-database) company. We were writing the v2 of a new product after a fairly successful development round of v1. For everything OLTP, we used the wonderful open-source database - Postgres. But by v2, we had new, hight-volume data like NetFlow coming in. This would have intensely tested Postgres's scalability and read/write performance. And we had some datawarehousing and OLAP requirements too. A hard look at our queries told us that column-stores would be a great-fit. Looking back, the options for a new product to store and query on massive data volumes boiled down to these few options -

* Throw more hardware: Tell the needy customer to invest more in hardware. But no one really knew how much more hardware was really going to nail it
* Tune, Shard, Rebuild, Redeploy: Invest in tuning our software and database for specific queries. Shard, re-model and/or do whatever that could be done by the development and implementation teams around what we had
* Use Oracle
	* This did not make good business sense for a big product company - tying itself deep into Oracle
	* CTO and architects did not think Oracle could nail the data volumes anyway (actually none of the engineers who understood the problem thought Oracle would nail it anyway!)
* Use column-stores like Sybase, Vertica

The fact was, there were no open-source, reliable, horizontally scalable column-stores or parallel DBMS to consider.

Times have improved. We now have Cassandra, HBase, Hypertable etc (MongoDB, CouchDB etc are document stores with less of modeling - here the context is of schema-full data with rich data-type support).

So, I decided to try and understand Cassandra. Wanted to answer the simple question - if I were to re-live the product development scenario described above, would I choose Cassandra? So in this article I talk about my experiment with Cassandra. Here, I choose a very specific use-case to illustrate what I found - Monitoring JVM metrics in a small data center.

#### A Simple Usecase
* A web company running 50 JVMs. The JVMs could be Apache-Tomcat servlet containers hosting the application
* Each Tomcat instance hosts 50 URLs and thereby, say, 50 front-ending servlet classes each extending HttpServlet
* Method metrics are collected on these servlets (through logs or bytecode instrumentation or aspect-driven). Specifically, the metrics collected - number of invocations and time-spent - just 2 method level metrics!
* Idea is to analyze the metrics to get insights into - how to deploy the servets servers? Are there any hotspots and, if so, where - which URL (object) is being accessed most/least? at what times? trends? and so on…
* Along with monitoring these specific servlet method's also keep a tab on overall application health. The number of active-threads in all JVM's. Various JVM memory parameters. A few MBean stat's. Etc…
* Minimum data view granularity requirements -
	* Last 30 days  - per-minute, per-hour, per-day, per-week, per-month
	* Last 60 days  - per-hour, per-day, per-week, per-month
	* Last 180 days - per-day, per-week, per-month
	* Last 360 days - per-week (52 weeks), per-month
	* Last 720 days - per-month (24 months)
* User primarily requires 'trend' and 'topN' charts. Examples -
	* Chart of Top-10 most invoked servlets in last 2 months at per-hour granularity
	* Trend of three specific servlet's response-times {max, min, avg, 1st and 3rd quartile} over last 6 months plotted per day
* User also wants JVM wide statistics like - active threads, memory stats and datasource stats - all following the same granularities as above. Lets suppose that these combine to 6 separate metrics in all. 
*  From the querying perspective, lets say we have only 2 users in our IT Operations team who will be actively querying this data.
	
#### Data Volumes

###### Fine-grained Data

* JVM Method data: 
	* 50 JVMs * 50 Methods * 24 Hours in a day * 60 minutes per hour * 2 metric-types = 7.2 Million data-points per day. 
	* 7.2 Million * 30 = 216 Million data points per month
* JVM-wide stats: 
	* 50 JVMs * 24 Hours * 60 minutes * 6 metric-types = 432K data points per day 
	* 432K * 30 = 12.96 Million per month

###### Coarse-grained Data

* This corresponds to roll-ups. Hourly, Daily, Weekly and Monthly.
* Hourly rollup for last 60 days
	* JVM method data: 50 JVMs * 50 Methods * 24 Hours * 60 days * 2 metric-types = 7.2 Million data points over last 60 days. Or, 120K data points per day
	* JVM-wide stats: 50 JVMs * 24 Hours * 60 days * 6 metric-types = 432K data points over last 60 days. Or, 7.2K data points per day
* Daily rollup for last 180 days
	* JVM Method data: 50 JVMs * 50 Methods * 180 days * 2 metric-types = 900K data points in 180 days. Or, 5K data points per day
	* JVM-wide stats: 50 JVMs * 180 days * 6 metric-types = 54K data points in 180 days. Or, 300 data points per day
* Weekly rollup for last 52 weeks
	* JVM Method data: 50 JVMs * 50 Methods * 52 weeks * 2 metric-types = 260K data points over last 52 weeks. Or, 5K data points per week. Or, 700 data points per day
	* JVM-wide stats: 50 JVMs * 52 weeks * 6 metric-types = 15.6K data points over last 52 weeks. Or, 300 data points per week. Or, 40 data points per day
* Monthly rollup for last 24 months
	* JVM Method data: 50 JVMs * 50 Methods * 24 months * 2 metric-types = 120K data points for last 24 months. Or, 5K data points per month. Or, 170 data points per day
	* JVM-wide stats: 50 JVMs * 30 days * 6 metric-types = 9000 data points per month. Or, 300 data points per month. Or 10 data points per day

###### Adding it all up!

Number of data points collected PER DAY -

* JVM Method data:
	* Fine grained minute data points = 7.2 Million
	* Hourly rollup = 120K
	* Daily rollup = 5K
	* Weekly rollup = 700
	* Monthly rollup = 170
	* Total (approx) = 7.32 Million
* JVM-wide stats:
	* Fine grained minute data points = 432K
	* Hourly rollup = 7.2K
	* Daily rollup = 300
	* Weekly rollup = 40
	* Monthly rollup = 10
	* Total (approx) = 440K
* Total of totals = 7.76 Million data points per day. Or, 320K data points per hour. Or, 5500 data points per minute. Or 90 data-points per second

There are couple of VERY IMPORTANT things to realize before going further -

* In the DBMS world, multiple data points can fit into a single row. So, 90 data-points per second translates to fewer than 90 row inserts per second. But how fewer depends on the data modeling
* The temporal distribution of inserts is not even. The hourly roll-up kicks in at the end of each hour. Daily roll-up at the end-of-day and so on (not considering the timezone adjustments required for roll-ups) 

#### Before we start data modeling... 
######Data Access methods in Cassandra
There are primarily three ways - Hector, Astyanax and CQL. Cassandra uses Thrift as the underlying RPC mechanism and has a Thrift API. Hector and Astyanax use the Thrift API to talk to the DBMS. CQL3 proposes a new SQL like API. This [slidedeck](http://www.slideshare.net/jericevans/cql-sql-in-cassandra) has CQL3 performance vis-a-vis Thrift-API by the main committer. Take your pick!


######SuperColumns
######Denormalization

#### Data Modeling
* Cassandra focuses on modeling the database per the queries. So by looking at the above usecase, what queries can I expect from the database modeler's perspective?    

#### Reading Recommendations
* Good introduction on the subject - [Oriell's Cassandra Definitive Guide](http://shop.oreilly.com/product/0636920010852.do), 
* Data Modeling - [this](http://www.ebaytechblog.com/2012/07/16/cassandra-data-modeling-best-practices-part-1/) wonderful blog by Jay Patel from Ebay
* Performance comparisons - [this](http://www.datastax.com/dev/blog/2012-in-review-performance) article really nails it (pay attention to the chart!)

 