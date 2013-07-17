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
	* Last 30 days   - Per minute
	* 30 - 60 days   - Hourly granularity
	* 60 - 180 days  - Daily granularity
	* 180 - 360 days - Weekly granularity
	* 360 - 720 days - Monthly granularity
* User primarily requires 'trend' and 'topN' charts. Examples -
	* Chart of Top-10 most invoked servlets in last 2 months at per-hour granularity
	* Trend of three specific servlet's response-times {max, min, avg, 1st and 3rd quartile} over last 6 months plotted per day
* User also wants JVM wide statistics like - active threads, memory stats and datasource stats - all following the same granularities as above. Lets suppose that these combine to 6 separate metrics in all. 
*  From the querying perspective, lets say we have only 2 users in our IT Operations team who will be actively querying this data.
	
#### Data Volumes
It is important to realize that in the RDBMS world the number of data points collected loosely translates into number of row insertions. And the number of row inserts in turn translates to the DB modeling.

###### Fine-grained Data

* JVM Method data: 
	* 50 JVMs * 50 Methods * 24 Hours in a day * 60 minutes per hour * 2 metric-types = 7.2 Million data-points per day. 
	* 7.2 Million * 30 = 216 Million data points per month
* JVM-wide stats: 
	* 50 JVMs * 24 Hours * 60 minutes * 6 metric-types = 432K data points per month. 
	* 432K * 30 = 12.96 Million per month

###### Coarse-grained Data

* This corresponds to roll-ups. Hourly, Daily, Weekly and Monthly.
* Hourly rollup
	* JVM method data: 50 JVMs * 50 Methods * 24 Hours * 2 metric-types = 120K data points per day
	* JVM-wide stats: 50 JVMs * 24 Hours * 6 metric-types = 7200 data points per day
* Weekly rollup
	* JVM Method data:  
* Monthly rollup
	* JVM Method data: 50 JVMs * 50 Methods * 30 days * 2 metric-types = 150K data points per month. Or, 5K data points per day
	* JVM-wide stats: 50 JVMs * 30 days * 6 metric-types = 9000 data points per month. Or, 300 data points per day
* 

###### Adding it all up!

* Number of data points per day = 

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

 