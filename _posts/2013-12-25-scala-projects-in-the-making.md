---
layout: post
title: "My Scala Projects In The Making"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
---

Over the last three months I have gone through the rigour of two eye-opening coursera courses. I would highly recommend these to anyone wanting to understand programming for the multicore, realtime, big-data. The courses are -

* [Functional Programming Principles In Scala](https://class.coursera.org/progfun-003)
*  [Principles Of Reactive Programming](https://class.coursera.org/reactive-001)

I have been trudging on and off with Scala for the latter half of 2013. Written many small programs to understand the core concepts. But doing these two courses have put me on very firm footing. The courses had me working on 12 solid assignments. And not a single one of these took me less than couple of days. The courses assignments cover a lot of ground which includes -

* Composing non-trivial higher order functions
* Mixing object oriented with functional
* Usage of Scala collections along with language built-in's like pattern-matching
* Testing with ScalaTest and ScalaCheck
* Using RxJava and Observables on non-trivial data-set
* Using Akka for Actor based concurrency

Inspired by these assignments, I have been working on few of my own ideas. Three projects specifically and all three are in their infancy. However as I head out with the family for a vacation for the new year, I thought of writing this quick post. One of the new year resolutions is to invest more time and energy into these...

### GBridge

* **Project Goal**: Data bridge between [Ganglia](http://ganglia.info/) (gmond) and [ZeroMQ](http://zeromq.org/)
* **The Why**
  * *Why Ganglia?* Because it is (probably) the worlds most popular open-source data collection tool for large data centres
  * *Why ZeroMQ?* Because it is (probably) the worlds most popular open-source data-bus for high volumes, with API in most programming languages
* **Specifics**
  * Ganglia's *gmond* agent responds with cluster wide metric health on TCP in XML. GBridge polls this data
  * GBridge can collect data from multiple clusters and *any* or *random* host within the cluster
  * GBridge is optimised for minimum polling of *gmond*
  * Each metric is published only once (and as a separate message) per polling cycle on ZeroMQ
  * Each metric is published as JSON
  * Use actor based concurrency and futures for polling multiple gmond nodes, parsing response and publishing on ZeroMQ
  * Completely in Scala
  * Graceful degradation on load. Support distribution, automatic recovery on errors and failover
  * Going ahead support [Collectd](http://collectd.org/) on data ingress side. Support writing to [OpenTSDB](http://opentsdb.net/) on the data egress side
* **Code Status**
  * [Coded](https://github.com/bharath12345/gBridge) the data collection, parsing and publish to ZeroMQ
  * Tested only for small loads
  * Very little unit test code
  * Yet to design for distribution, recovery and failover
  
### ScalaBlog
* **Project Goal**: [Jekyll](http://jekyllrb.com/) or [PoetJS](http://jsantell.github.io/poet/) like markdown based static blogging platform in Scala
* **The Why**
  * Scala lends better for server side coding
  * For larger blogs, features like full text search can be much faster in Scala than Ruby or JavaScript
  * Apart from human-readable HTML interface, also provide a machine-readable   RESTful interface
  * Option to store the markdown in flat files on the server side or source it from a RDBMS store
* **Specifics**
  * Use [Spray](http://spray.io/) for HTTP Server side (for both RESTful interface and HTML pages)
  * Use [pegdown](https://github.com/sirthias/pegdown) for markdown processing 
  * Use [Slick](http://slick.typesafe.com/) to read and write to RDBMS from Scala (ORM like)
  * 
* **Code Status**
  * The [code](https://github.com/bharath12345/myspray) for CRUD (post/get/put/delete) operations for the blog with RESTful URLs is complete up to proof-of-concept
  * The code for CRUD at the database layer also done
  * pegdown parsing of markdown complete
  * Work needed to easily extend the URLs, support UI templating and much more

### WebFlow
* **Project Goal**: 
* **The Why**
* **Specifics**
* **Code Status**