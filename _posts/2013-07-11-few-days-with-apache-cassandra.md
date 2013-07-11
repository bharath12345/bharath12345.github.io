---
layout: post
title: "Few days with Apache Cassandra"
category: posts
published: false
---

Few years ago I was a product developer at a big software (but non-database) company. We were writing the v2 of a new product after a fairly successful development round of v1. For everything OLTP, we used the wonderful open-source database - Postgres. But by v2, we had new, hight-volume data like NetFlow coming in. This would have intensely tested Postgres's scalability and query performance. And we had some datawarehousing and OLAP requirements too. A hard look at our queries told us that column-stores would be a great-fit. Looking back, the options for a new product to store and query on massive data volumes boiled down to these few options -

* Throw more hardware: Tell the needy customer to invest more in hardware. But no one really knew how much more hardware was really going to nail it
* Tune, Shard, Rebuild, Redeploy: Invest in tuning our software and database for specific queries. Shard, re-model and/or do whatever that could be done by the development and implementation teams around what we had
* Use Oracle: (1) This did not make good business sense for a big product company - tying itself deep into Oracle (2) No one thought Oracle could nail the data volumes anyway
* Use column-stores like Sybase, Vertica

The fact was, there were no open-source, reliable, horizontally scalable column-stores or parallel DBMS to consider.

Times have improved. We now have Cassandra, HBase etc (MongoDB, CouchDB etc are document stores with less of modeling - here the context is of schema-full data with rich data-type support).

So, I decided to try and understand Cassandra. Wanted to answer the simple question - if I were to relive the product development scenario described above, would I choose Cassandra? So in this article I talk about my experiment with Cassandra with a very specific use-case. BTW, my reading recommendations -

* Good introduction on the subject - [Oriell's Cassandra Definitive Guide](http://shop.oreilly.com/product/0636920010852.do), 
* Data Modeling - [this](http://www.ebaytechblog.com/2012/07/16/cassandra-data-modeling-best-practices-part-1/) wonderful blog by Jay Patel from Ebay
* Performance comparisons - [this](http://www.datastax.com/dev/blog/2012-in-review-performance) article really nails it (pay attention to the chart!)

#### A Simple Usecase
* A web company running 50 JVMs. The JVMs are apache-tomcat servlet containers hosting your site's front-end dynamic data
* Each tomcat instance hosts 50 URLs and thereby, say, 50 front-ending servlet classes each extending HttpServlet
* You collect metrics on these servlets (logs or byte instrumentation or aspect-driven or whatever). Metrics collected - number of invocations and time-spent
* You would like to analyze these metrics to get insights into - how do I deploy these servet classes across my servers? where is the hotspot - which URL (object) is being accessed most/least? at what times? trends? and so on…
* Along with monitoring these specific servlet method's you also want to keep a tab on overall application health. The number of active-threads in all these JVM's. Various JVM memory parameters. A few MBean stat's. Etc…
* You necessarily want to see this data at fine-grained per-minute level for recent history. You are okay with more of a coarse-grained view of this data over longer periods but necessarily want that too…

#### Data Volumes
It is important to realize that in the DBMS world the number of data points collected loosely translates into number of row insertions. So, how much data does this usecase real mean?

Lets start with the fine-grained piece…

* By fine-grained, let us hope that our user will be satisfied to see trend and changes at per-minute granularity
* 50 JVMs X 50 Methods X 24 Hours in a day X 60 minutes per hour => 3.6 Million data-points. Which translates to 3.6 Million row inserts per day (yay! I found my own personal big-data problem right there!)
* Lets suppose our user wants this fine-grained picture of methods just for last one month. So that makes it all but just 108 Million inserts (try that on MySql you downloaded, not one from facebook or twitter mind you!)
*  And thats just half the story. Our user afterall wants the thread and JVM memory stats too. Lets suppose that he is okay with 2 minute interval of collection for these - so we have 54 Million inserts per month for say 4 metrics (one for threads and rest for memory)
*  Adding that we get around 162 Million records to insert
*  From the querying perspective, lets say we have only 2 users in our IT Operations team who will be actively querying this data.
*  If you think you can make this work with something in open-source RDBMS, then its time to stop reading this article right here and conserve some time...


#### Before we start data modeling... 
######Data Access methods in Cassandra
There are primarily three ways - Hector, Astyanax and CQL
######SuperColumns
######Denormalization

#### Data Modeling
* Cassandra focuses on modeling the database per the queries. So by looking at the above usecase, what queries can I expect from the database modeler's perspective?    

 