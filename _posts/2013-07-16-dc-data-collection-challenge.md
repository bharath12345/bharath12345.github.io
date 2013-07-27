---
layout: post
title: "DC Data Collection Challenge"
category: posts
published: false
tags: []
categories: [Technical]
tweetfb: true
disqus: true
---

Small Data Center Configuration

Total Servers = 100
Servers running Java App = 30
Servers running C++ Front-end Webserver (Apache or Nginix) = 20
Servers running Ruby/PHP application = 30
Servers running Database = 20

------

Most optimistic data collection

- In doing a SSH to collect the uptime 99% of time is taken by connection establishment and teardown. And the time taken itself can be assumed to have a mean of around 5~6 seconds. So a maximum of 10 hosts can be handled in a minute by a single thread. Let us assume multiple KPIs (CPU, memory etc) are retrived by a single SSH. So for a small Data Center of 100 servers, the number of threads required is around 100/10 = 10 threads

- Similarly the mean of JMX can be assumed to be around 10 seconds. Problem with JMX - you cannot retrieve multiple variables in a single session like JMX. Let us assume there are 30 JVMs in our 300 node DC. And we want to retrieve 10 KPIs per JVM. Total data-points = 30 * 10 = 300. With a 10 second mean, 6 KPIs can be retrieved in a minute by a single thread. Total threads required to retrieve all KPIs = 300/6 = 50 threads

- Suppose there are 20 data-base servers in the farm. JDBC mean times can be assumed to be no different than JMX. However more than 1 KPI can be retrieved in a single JDBC session. Suppose there are 10 Database KPIs to retrieve and assuming a single session to query 3 DB tables to retrieve all of them, the mean time to retrieve will be close to 15 seconds. Which is 4 DB servers can be polled per thread. Which gives us a requirement of 20/4 = 5 threads

- 20 Apache front-end webservers and load-balancers. RPC to retrieve data. Again around 10 seconds mean time = 6 server per thread. Not possible to group multiple KPIs in single session. Around 6 KPIs per server, which is 20 * 6 = 120 data points. 120/6 = 20 threads

- RPC/RMI like mechanism to retrieve data from the Ruby/PHP applications. Similar to JVM. Gives us around 50 threads

-----

Host data collector threads = 10
JMX data collector threads = 50
DB data collector threads = 5
Webserver data collector threads = 20
WebApp data collector threads = 50
Total data collector threads = 135 threads

Connections per minute
Host = 100 connections per minute
JMX = 30 connections per minute
JDBC = 20
Apache = 20
WebApp = 30
Total = 200 connections per minute
