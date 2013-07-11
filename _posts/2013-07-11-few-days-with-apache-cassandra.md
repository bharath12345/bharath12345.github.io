---
layout: post
title: "Few days with Apache Cassandra"
category: posts
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
* Data Modeling - [this](http://www.ebaytechblog.com/2012/07/16/cassandra-data-modeling-best-practices-part-1/) wonderful by Jay Patel from Ebay
* Performance comparisons - [this](http://www.datastax.com/dev/blog/2012-in-review-performance) one really nails it (pay attention to that chart!)



