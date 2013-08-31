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
<div id="graphs" style="width: 1150px; height: 600px; border: 1px solid black;"></div>
&nbsp;

Now, here is a quick roundup of what I found about these two...

<div class="bs-docs-grid">
    <div class="row show-grid">
        <div class="col-md-2 first"></div>
        <div class="col-md-5 left">D3</div>
        <div class="col-md-5 right">jsPlumb</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first">Scalability</div>
        <div class="col-md-5 left">D3 is built for scalability of visual components. Hundreds and thousands of nodes and edges can be quickly created and the visualization renders really fast (I did a quick scale test of close to 5000 nodes and few hundred thousand edges - one has to really see it to believe how fast the rendering is)</div>
        <div class="col-md-5 right">jsPlumb is much slower than D3 in rendering. However that does not mean it is slow - D3 is simply too fast!</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first">Layouts: Force etc</div>
        <div class="col-md-5 left">D3 has pre-built force layout visualization with many options. https://github.com/mbostock/d3/wiki/Force-Layout. </div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first">Visual Beauty</div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first">Development Simplicity</div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first">Rendering Speed</div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first">Layer transitions, Panning, Zoom</div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
</div>

### APM Products
<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojox/image/resources/image.css" media="screen">
<div id="apm"></div>





