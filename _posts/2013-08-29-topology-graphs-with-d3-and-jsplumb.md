---
layout: post
title: "Application Topology Graphs - Usecase, Different Product Offerings, Prototype Using D3 and jsPlumb"
category: posts
published: false
tags: []
categories: [Technical]
tweetfb: true
disqus: true
toc: true
---

There are many traditional areas of graph depictions like computer networks, social networks etc. Sometime ago, I came across the use-case of graphs for software application topologies. This post covers the few things I discovered on the topic of application topologies and their graphical representation.

### Usecase
The aspect that makes application topologies a challenge is that they are deeply logical. A database can be shared by multiple applications (like a CMDB). Depending upon the organization hierarchies different application components (both hardware resources like servers and software components like application servers ) may be required to be grouped differently. And different users and user groups may require different layer transitions starting with a top level view of the application in focus and drilling through to its component details. Many Application Performance Management (APM) products provide such graphical views. A later section in this blog shows the application graph views of popular APM like AppDynamics, OpTier etc

### Prototype
Before getting too deep into my ideas for application graphs I decided to work to develop a prototype for graph representations. After a few hours of looking through the world of JavaScript I discovered multiple libraries capable of good graph rendering. One can buy libraries like yFiles or use open-source freewares like GraphDracula, mxGraph etc. But the libraries that I was most impressed with were D3 and jsPlumb. I have played with D3 for over a year now and it is one of the most exciting JavaScript libraries out there. The very paradigm of data-modeling for D3 provides for extremely vivid and smooth graphical representations of all kind. And just a visit to the jsPlumb website is good enough to excite any programmer of its potential. So I got cracking with D3 and jsPlumb. Below are the two graph prototypes I came up with (it honestly did not really much of an effort to quickly code these up using the existing code available on the web). The code for these prototypes are available in my GitHub repository. I use Dojo for AMD functionality and outer containers.

http://stackoverflow.com/questions/7034/graph-visualization-code-in-javascript

<link rel="stylesheet" type="text/css" href="/lib/my/topograph/topograph.css"/>
<div id="graphs" style="width: 1150px; height: 600px;"></div>

### APM Products
<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojox/image/resources/image.css" media="screen">
<div id="apm"></div>





