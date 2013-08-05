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

My champion-hacker friend Sumanth and I spent a little time few weeks ago applying ourselves to understand the data collection challenge at a typical small data center. We started by asking whether there was a challenge at all. 

I looked at tools like Ganglia and also discovered that they are widely deployed. Ganglia is very active as a development project and uses Multicast for data transmission. It caches data at all nodes within a cluster. The collection station has to communicate to only one (any) node within a cluster. I asked myself what could be the rationale behind this design. And as I looked more deeply into the world of Ganglia I discovered amazing attention to detail - to optimise data and time without compromising accuracy or extensibility. For those wishing to understand Ganglia, [this book](http://shop.oreilly.com/product/0636920025573.do) is a must read. The chapter on case-studies in this book makes for a truly fascinating read. [This paper](http://www.ittc.ku.edu/~niehaus/classes/750-s07/documents/ganglia-parallel-computing.pdf) also provides a very good intro.

In this blog I present the numbers first and my inferences later. 

#### Usecase

Let us take the example of a small eCommerce company called "WebTraveller". On this company -

* WebTraveller is a travel portal on the lines of Expedia but a startup with a target market of few small-and-medium-sized enterprises in a region
* WebTraveller decided to build its web application using Ruby (which is going strong as No.2 on GitHub top languages - https://github.com/languages)
* For its many static pages and load-balancing, the IT folk at WebTraveller decided to do the time-tested thingy - use Apache HTTPD or Nginix
* WebTraveller has to interface with travel data providers (airlines, bus company's et al), payment gateways, advertisers etc. Let us assume a simple idealistic world where all this data comes through superbly designed RESTful interface. So, the  IT folk at WebTraveller decided to publish/subscribe to this RESTful external data interface through a Java application
* WebTraveller uses MySql or Postgres as its database to store user info etc
* Analytics is important for WebTraveller to run promotions, tune resources per demand/supply and present forecasts/state-of-business to investors - so, as a policy 10% of all IT resources are ear-marked for 'analytics'
* And as a policy, no more than 5% of IT resources should be consumed by monitoring and management tools - these are overheads and should be kept to a minimum after all 

#### IT Resources
Now, how much IT resources will WebTraveller require? Since I am the de facto CIO of WebTraveller and it is my first CIO job, I decide to start with a nice whole number - say 100 servers (okay, I hear you, all on cloud). Now, here is the split up of what this 100 servers are going to do…
  
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>Servers running WebTraveller's Ruby based dynamic Web-Application</td>
		<td>25</td>
	</tr>
	<tr>
		<td>Servers sourcing WebTraveller's static page and load-balancer (httpd/nginix)</td>
		<td>15</td>
	</tr>
	<tr>
		<td>Servers running WebTraveller Java interface with its data providers</td>
		<td>25</td>
	</tr>
	<tr>
		<td>WebTraveller database servers</td>
		<td>20</td>
	</tr>
	<tr>
		<td>IT analytics</td>
		<td>10</td>
	</tr>
	<tr>
		<td>IT management/monitoring</td>
		<td>5</td>
	</tr>
	<tr>
		<td>Total Servers</td>
		<td>100</td>
	</tr>
</table>	
	
*(How much am I off the mark in these assumptions? If its horrific, then please let me know and I promise to re-do this blog)*

#### Quantum of data to collect
Being the CIO, I want to understand how my IT is coping. So I need data. Data on server's utilisation, database metrics, web-server metrics etc. Industry calls these various metrics as KPI - Key Performance Indicators. So KPI it will be. How many KPIs do I need to collect for each type of IT resource?

<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>KPI Type</td>
		<td>Approximate Number of KPIs per instance</td>
		<td>Number of Instances (from the above table)</td>
		<td>Total KPIs to collect</td>
	</tr>
	<tr>
		<td>Operating system level KPIs - CPU, RAM, open sockets, HDD usage, network card stats etc</td>
		<td>5</td>
		<td>100</td>
		<td>500</td>
	</tr>
	<tr>
		<td>Ruby web-app KPIs</td>
		<td>10</td>
		<td>25</td>
		<td>250</td>
	</tr>
	<tr>
		<td>Ruby web-app runs on the Rails server. KPIs that speak Rails health</td>
		<td>10</td>
		<td>25</td>
		<td>250</td>
	</tr>
	<tr>
		<td>Java web-app KPIs</td>
		<td>10</td>
		<td>25</td>
		<td>250</td>
	</tr>
	<tr>
		<td>Java web-app's use a JVM and app-server (JBoss/Glassfish/Tomcat). KPIs that speak Java platform health</td>
		<td>10</td>
		<td>25</td>
		<td>250</td>
	</tr>
	<tr>
		<td>HTTPD or NGINIX KPIs</td>
		<td>10</td>
		<td>15</td>
		<td>150</td>
	</tr>
	<tr>
		<td>Database Server KPIs</td>
		<td>20</td>
		<td>20</td>
		<td>400</td>
	</tr>
	<tr>
		<td>KPIs from the Analytics system (say running Hadoop)</td>
		<td>10</td>
		<td>10</td>
		<td>100</td>
	</tr>
	<tr>
		<td>Total</td>
		<td>-</td>
		<td>-</td>
		<td>2150</td>
	</tr>
</table>

So, the approximate total number of KPIs to collect is 2150. Which is an average of about 21 KPIs to be collected from the 100 servers of WebTraveller. Now, how frequently do we want to collect this data? I as the CIO of WebTraveller want my IT to be really AGILE - which means I don't want to miss any data (especially in its initial days!). And I also want to keep it SIMPLE. So I ask my monitoring team to collect all these KPIs *every minute*.  

#### The Developer's View
'Mr. Bean' is the developer in WebTravellers IT team. Mr. Bean's task is cut out. He would be given one out of the 5 server's from IT management/monitoring team's quota to collect these KPIs and store them in the database (of the other 4 - one each for monitoring database, monitoring front-end, provisioning/configuration system and a single lone 'test-box' :-)).

Mr. Bean does not know if one server is going to be sufficient. But being a seasoned developer, he knows for sure that to collect so many KPIs he needs to code a 'multi-threaded' application. So Bean decides to do some estimation. How many threads will his application need to capture 2150 KPIs every minute?

First of all, what are the different methods that exist to capture these KPIs from a remote server? Here are the necessary few -

* JMX to collect from Java applications
* JDBC to collect from the databases itself
* RPC/RMI or SSH based log-monitoring mechanism to retrieve data from the Ruby part
* RPC/RMI or SSH based log-monitoring to retrieve data from HTTPD/NGINX
* Server level stats through remote SSH or SNMP

Looking at this list, Bean wants to chuck SNMP in v1.0 of the project. He wants to write as few connectors as possible and SSH seems to work for multiple KPIs. Bean calculates the response-time for various collection methods - 

<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>Collection Method</td>
		<td>Observation</td>
		<td>Mean time to collect one KPI data-point (Optimistic)</td>
		<td>Num of data-points that can be retrieved in 1 minute by a single thread</td>
	</tr>
	<tr>
		<td>SSH</td>
		<td>In doing a SSH to collect the uptime 99% of time is taken by connection establishment and teardown. Though multiple commands can be run on a remote SSH session and data retrieve, this optimisation comes at the cost of increased complexity of development</td>
		<td>6 seconds</td>
		<td>60/6 => 10 data-points</td>
	</tr>
	<tr>
		<td>JMX</td>
		<td>Problem with JMX - you cannot retrieve multiple variables in a single session. Every variable has connection establishment and authentication</td>
		<td>10 seconds</td>
		<td>60/10 => 6 data-points</td>
	</tr>
	<tr>
		<td>JDBC</td>
		<td>More than 1 KPI can be retrieved in a single JDBC session</td>
		<td>Let us assume 20 seconds to retrieve all 20 database server KPIs of one instance</td>
		<td>60 data-points</td>
	</tr>
	<tr>
		<td>RPC or RMI</td>
		<td>Not possible to group multiple KPIs in single session</td>
		<td>10 seconds</td>
		<td>60/10 => 6 data-points</td>
	</tr>
	<tr>
		<td>SNMP</td>
		<td>Highly dependent on the KPI itself and its agent implementation</td>
		<td>NA</td>
		<td>NA</td>
	</tr>
</table>

With this understanding, Mr. Bean decides to use the following collection technology for each class of KPIs -

<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>KPI Type</td>
		<td>Data Collection Technology</td>
	</tr>
	<tr>
		<td>Operating system level KPIs - CPU, RAM, open sockets, HDD usage, network card stats etc</td>
		<td>SSH</td>
	</tr>
	<tr>
		<td>Ruby web-app KPIs</td>
		<td>RPC or RMI</td>
	</tr>
	<tr>
		<td>Ruby web-app runs on the Rails server. KPIs that speak Rails health</td>
		<td>RPC or RMI</td>
	</tr>
	<tr>
		<td>Java web-app KPIs</td>
		<td>JMX</td>
	</tr>
	<tr>
		<td>Java web-app's use a JVM and app-server (JBoss/Glassfish/Tomcat). KPIs that speak Java platform health</td>
		<td>JMX</td>
	</tr>
	<tr>
		<td>HTTPD or NGINIX KPIs</td>
		<td>SSH</td>
	</tr>
	<tr>
		<td>Database Server KPIs</td>
		<td>JDBC</td>
	</tr>
	<tr>
		<td>KPIs from the Analytics system (say running Hadoop)</td>
		<td>SSH</td>
	</tr>
</table>

After deciding on which technology to use for each KPI, Mr. Bean tabulates the total KPIs in each category

<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>Data Collection Technology</td>
		<td>Total KPIs to collect</td>
	</tr>
	<tr>
		<td>SSH</td>
		<td>500 + 150 + 100 = 750</td>
	</tr>
	<tr>
		<td>RPC or RMI</td>
		<td>250 + 250 = 500</td>
	</tr>
	<tr>
		<td>JMX</td>
		<td>250 + 250 = 500</td>
	</tr>
	<tr>
		<td>JDBC</td>
		<td>400</td>
	</tr>
	<tr>
		<td>Total</td>
		<td>2150 (this tallies with the previously calculated # of KPIs)</td>
	</tr>
</table>

With this knowledge of total KPIs, methodology for each and time taken for each, Mr. Bean wants to know the number of threads his application may have to run. Mr. Bean know that ideally, he would want to do Asynchronous collection for each of these - that is, start a request in Thread-A and retrieve the data from Thread-B when it arrives - there are many libraries that provide such Asynchronous capabilities for each of SSH, RPC, RMI, JMX, JDBC etc. However, Asynchronous communication does not lead to conservative number of threads - a thread gets forked whenever data arrives. For most conservative number of threads, a select-and-poll based method is most appropriate. The big deficiency of select-and-poll approach however is that data collection with time boundaries becomes tougher. There is no guarantee that the above mentioned mean times will always hold good. And also, the data that arrives is distributed wildly on the temporal scale. 

So, Mr. Bean calculates the number of threads that his application will end-up with if he takes either of the approaches -

##### With the more thread-conservative select-and-poll approach -

<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>Data Collection Technology</td>
		<td>Num of data-points that can be retrieved in 1 minute by a single thread</td>
		<td>Total KPIs to collect in a minute</td>
		<td>Number of threads required to collect all KPIs in a minute</td>
	</tr>
	<tr>
		<td>SSH</td>
		<td>10</td>
		<td>750</td>
		<td>750/10 => 75</td>
	</tr>
	<tr>
		<td>RPC or RMI</td>
		<td>6</td>
		<td>500</td>
		<td>500/6 => 83</td>
	</tr>
	<tr>
		<td>JMX</td>
		<td>6</td>
		<td>500</td>
		<td>500/6 => 83</td>
	</tr>
	<tr>
		<td>JDBC</td>
		<td>60</td>
		<td>400</td>
		<td>400/60 => 7</td>		
	</tr>
	<tr>
		<td>Total</td>
		<td>82</td>
		<td>2150</td>
		<td>Approx 250</td>
	</tr>
</table>
 
##### Asynchronous approach

<table class="table table-bordered table-striped table-condensed bs-docs-grid">
	<tr>
		<td>Data Collection Technology</td>
		<td>Total KPIs to collect in a minute</td>
		<td>Observation on number of Asynchronous calls required</td>
		<td>Potentially max number of threads running in a minute</td>
	</tr>
	<tr>
		<td>SSH</td>
		<td>750</td>
		<td>One Async call per KPI</td>
		<td>750</td>
	</tr>
	<tr>
		<td>RPC or RMI</td>
		<td>500</td>
		<td>One Async call per KPI</td>
		<td>500</td>
	</tr>
	<tr>
		<td>JMX</td>
		<td>500</td>
		<td>One Async call per KPI</td>
		<td>500</td>
	</tr>
	<tr>
		<td>JDBC</td>
		<td>400</td>
		<td>20 database server KPIs of one instance in a single Async call</td>
		<td>400/20 => 20</td>
	</tr>
	<tr>
		<td>Total</td>
		<td>-</td>
		<td>-</td>
		<td>Approx 1750</td>
	</tr>
</table>

-----------------

- Similarly the mean of JMX can be assumed to be around 10 seconds.  Let us assume there are 30 JVMs in our 300 node DC. And we want to retrieve 10 KPIs per JVM. Total data-points = 30 * 10 = 300. With a 10 second mean, 6 KPIs can be retrieved in a minute by a single thread. Total threads required to retrieve all KPIs = 300/6 = 50 threads

- Suppose there are 20 data-base servers in the farm. JDBC mean times can be assumed to be no different than JMX. However more than 1 KPI can be retrieved in a single JDBC session. Suppose there are 10 Database KPIs to retrieve and assuming a single session to query 3 DB tables to retrieve all of them, the mean time to retrieve will be close to 15 seconds. Which is 4 DB servers can be polled per thread. Which gives us a requirement of 20/4 = 5 threads

- 20 Apache front-end webservers and load-balancers. RPC to retrieve data. Again around 10 seconds mean time = 6 server per thread. Not possible to group multiple KPIs in single session. Around 6 KPIs per server, which is 20 * 6 = 120 data points. 120/6 = 20 threads

- RPC/RMI like mechanism to retrieve data from the Ruby/PHP applications. Similar to JVM. Gives us around 50 threads

-----

Host data collector threads = 10
JMX data collector threads = 50
DB data collector threads = 5
WebServer data collector threads = 20
WebApp data collector threads = 50
Total data collector threads = 135 threads

Connections per minute
Host = 100 connections per minute
JMX = 30 connections per minute
JDBC = 20
Apache = 20
WebApp = 30
Total = 200 connections per minute
