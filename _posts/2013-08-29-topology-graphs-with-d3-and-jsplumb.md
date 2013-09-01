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

#### About these graphs
<div class="bs-docs-grid">
    <div class="row show-grid">
        <div class="col-md-6 left alignCenter"><h5>D3</h5></div>
        <div class="col-md-6 right alignCenter"><h5>jsPlumb</h5></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-6 left">
            <ol>
                <li>The two different types of icons stand for single-applications and application-groups</li>
                <li>The graph can be panned and zoomed using. To pan => click on the graph and drag it. To zoom => use the mouse scroller</li>
                <li>The graph actually represents a set of interconnected applications and application-groups</li>
                <li>On top of this graph, it is not very difficult to add hover effect on nodes and links. It is also not difficult to add color effects to application nodes and edges</li>
                <li>The icons, text and links are all SVG - so they scale beautifully on zooming</li>
                <li>Every refresh of the page should lead to a re-rendering of the graph in a different way. This is so because the graph is rendered by D3 Force directed graph layout. The position of nodes and edges is not fixed but computed randomly each time. I have not done a very good or thorough job of getting the nitty gritties of this force layout right so that the graph appears perfectly within the coordinates of its box (or, the zoom level is just correct for a given viewport size). Such tuning however is very possible and will make the suitable for all form factors</li>
            </ol>
        </div>
        <div class="col-md-6 right">
            <ol>
                <li>This depicts a typical web-application with its 3-tiers: web-layer, app-layer and datasource (database, external etc).</li>
                <li>jsPlumb provides many different types of connectors and endpoints. After playing with the options for a while I have the left the connections to look like 'Z' - it just looked interesting to me! Maybe the more appropriate links are straight lines. Also have chosen the source endpoint of the connections to have a blue dot. And the connections to have an arrow - there are many choices for all these settings</li>
                <li>Mouse-over the links to see the color change from yellow to blue - all this needs is a simple css setting</li>
                <li>To differentiate the 3-layers I have used Dojo Titlepane's. I have a liking for their neat rendering</li>
                <li>The icons are SVG. Did not try to implement zoom, pan or node/link movement. They are very much possible though non-trivial and I did not attempt for this prototype</li>
            </ol>
        </div>
    </div>
</div>

#### Comparison
<div class="bs-docs-grid">
    <div class="row show-grid">
        <div class="col-md-2 first"></div>
        <div class="col-md-5 left alignCenter"><h5>D3</h5></div>
        <div class="col-md-5 right alignCenter"><h5>jsPlumb</h5></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Scalability</h5></div>
        <div class="col-md-5 left">D3 is built for scalability of visual components. Hundreds and thousands of nodes and edges can be quickly created and the visualization renders really fast (I did a quick scale test of close to 5000 nodes and few hundred thousand edges - one has to really see it to believe how fast the rendering is)</div>
        <div class="col-md-5 right">jsPlumb is much slower than D3 in rendering. However that does not mean it is slow - D3 is simply too fast!</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Layouts: Force etc</h5></div>
        <div class="col-md-5 left">D3 has pre-built force layout visualization with many options. https://github.com/mbostock/d3/wiki/Force-Layout. A force directed graph works beautifully when the real-estate available for rendering is dynamic along with a (probable) huge number of nodes and edges. The graph layout can optimize itself (per some settings) to be inferencable to the human eye</div>
        <div class="col-md-5 right">jsPlumb provides endpoints and connectors. One can use the facilities to build a force directed graph but such rendering algorithms are not provided OOTB and coding these is not easy. However if the number of edges and nodes is know and falls into a clean pattern (like the above graph) then jsPlumb can be a very neat layout.</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Visual Beauty</h5></div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Development Simplicity</h5></div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Rendering Speed</h5></div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Layer transitions, Panning, Zoom</h5></div>
        <div class="col-md-5 left"></div>
        <div class="col-md-5 right"></div>
    </div>
</div>

### APM Products

Hello World! Hello World! Hello World! Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!
<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojox/image/resources/image.css" media="screen">
<div id="apm"></div>





