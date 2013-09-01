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

Graph depictions are common for problems like computer networks, social networks etc. Sometime ago, I came across the use-case of graphs for software application topologies. This post covers the few things I discovered on the topic of application topologies and their graphical representation.

### Usecase
One aspect that makes application topologies a challenge is that they are logical. That is, the boundaries of a application are difficult to define. Its usual to find in web companies/banks one 'application owner' just responsible for the database systems while another for applications that make use of the database. The database thus becomes a shared application with potentially multiple owners. From the point of view of graphical representation of applications in the enterprise, the representation of running application thus becomes 'logical'. Depending upon the organization hierarchies different application components (both hardware resources like servers and software components like application servers ) may be required to be grouped differently. Inter and intra application views are required. And different users and user groups may require different layer transitions starting with a top level view of the application in focus and drilling through to its constituents details. Many Application Performance Management (APM) products provide such graphical views. A later section in this blog shows the application graph views of popular APM like AppDynamics, OpTier etc

### Prototype
Before getting too deep into thinking about application graphs I decided to develop a prototype for such graph representations. After a few hours of looking through the world of JavaScript discovered multiple libraries capable of good graph rendering. [This](http://stackoverflow.com/questions/7034/graph-visualization-code-in-javascript) StackOverflow thread is useful. One can buy libraries like [yFiles](http://www.yworks.com) or use open-source freewares like [GraphDracula](http://www.graphdracula.net), mxGraph etc. But the libraries that I was most impressed with were [D3](http://www.d3js.org) and [jsPlumb](http://www.jsplumbtoolkit.com). I have played with D3 for over a year now and it is one of the most exciting JavaScript libraries. The very paradigm of data-modeling and programming for D3 is enlightening and it provides for extremely vivid and smooth graphical representations of all kind. And just a visit to the jsPlumb website is good enough to excite any programmer of its potential. So I got cracking with D3 and jsPlumb. Below are the two graph prototypes I came up with (it did not take much of an effort to code these up using help from existing code available on web). The code for these prototypes are available on my GitHub repository. I use Dojo for modularising the code (AMD way) and draw up the containers.

<link rel="stylesheet" type="text/css" href="/lib/my/topograph/topograph.css"/>
<div id="graphs" style="width: 1150px; height: 600px; border: 1px solid black;"></div>
&nbsp;

#### About these graphs
<div class="bs-docs-grid" id="about">
    <div class="row show-grid">
        <div class="col-md-6 left alignCenter"><h5>D3 Graph</h5></div>
        <div class="col-md-6 right alignCenter"><h5>jsPlumb Graph</h5></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-6 left">
            <ol>
                <li>This is more like a inter-applications and application-group view</li>
                <li>The two different types of icons stand for single-applications and application-groups</li>
                <li>The graph can be panned and zoomed. To pan click on the graph and drag it. To zoom use the mouse scroller</li>
                <li>The graph actually represents a set of interconnected applications and application-groups</li>
                <li>With D3 it is not very difficult to add hover effect on nodes and links atop such a graph. It is also not difficult to add color effects to application nodes and edges to signify status</li>
                <li>The icons, text and links are all SVG - so they scale beautifully on zooming</li>
                <li>Every refresh of the page leads to a re-rendering of the graph in a different way. This is so because the graph is rendered using D3 Force directed graph layout. The position of nodes and edges is not fixed but computed each time by the algorithm for the given gravity, distance and charge setting (this prototype is not a thorough job of getting the nitty-gritty of a force layout with D3 right for the best possible rendering within the coordinates of a box. Thoughtful tuning of parameters should make the graph good for all form factors)</li>
            </ol>
        </div>
        <div class="col-md-6 right">
            <ol>
                <li>This is more like a intra-application view</li>
                <li>This depicts a typical web-application with its 3-tiers: web-layer, app-layer and datasource (database, external etc)</li>
                <li>jsPlumb provides many different types of connectors and endpoints. After playing with the options for a while I have the left the connections to look like 'Z' simply because it looked nice to me! (the more appropriate links would probably be straight lines, but this was just a playful prototype!). Have chosen the source endpoint of the connections to have a blue dot. The connections have an arrow on top (there are many choices for all such settings)</li>
                <li>Mouse-over the links to see the color change from yellow to blue - all it takes to do this piece is to get a simple css setting right</li>
                <li>To differentiate the 3-layers, I have used Dojo Titlepane's. I have a liking for their neat rendering</li>
                <li>The icons are SVG. Did not try to implement zoom, pan or node/link movement. They are very much possible though non-trivial</li>
            </ol>
        </div>
    </div>
</div>

#### Comparison
<div class="bs-docs-grid" id="comparison">
    <div class="row show-grid">
        <div class="col-md-2 first"></div>
        <div class="col-md-5 left alignCenter"><h5>D3</h5></div>
        <div class="col-md-5 right alignCenter"><h5>jsPlumb</h5></div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Scalability</h5></div>
        <div class="col-md-5 left">D3 is built for scalability of visual components. Hundreds and thousands of nodes and edges can be quickly created/updated/removed and the visualization render and transition really fast (I did a quick scale test of close to 5000 nodes and few hundred thousand edges - one has to really see it to believe how fast the rendering is)</div>
        <div class="col-md-5 right">jsPlumb is much slower than D3 in rendering. However that does not mean it is slow - D3 is simply too fast!</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Layouts: Force etc</h5></div>
        <div class="col-md-5 left">D3 has pre-built [force layout](https://github.com/mbostock/d3/wiki/Force-Layout) visualization with many options. A force directed graph works beautifully when the real-estate available for rendering is dynamic along with a (probable) huge number of nodes and edges. The graph layout optimizes itself (per gravity/distance/charge settings) to provide the best cognitive view possible</div>
        <div class="col-md-5 right">jsPlumb provides endpoints and connectors. One can use the facilities to build a force directed graph but such rendering algorithms are not provided OOTB (coding a force layout algorithm is not trivial). However if the number of edges and nodes is known, is not very huge and falls into a clean pattern (like the 3-layers in the above graph), jsPlumb can be used to create very neat layouts</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Visual Beauty</h5></div>
        <div class="col-md-5 left">Requires programming. One can search and lookup upteen amazing D3 visualizations including many that are graphs. One can use SVG for scalable zooming. Building a beautiful graph framework for a product with D3 will require some work</div>
        <div class="col-md-5 right">Even the default setting can produce excellent looking graphs. Building better looking graphs (with fewer elements) should be considerably easier with jsPlumb</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Development Simplicity</h5></div>
        <div class="col-md-5 left">D3 takes some learning. The paradigm of create/update/destroy of elements along with modelling of json data for a particular library function can be complex. But once the mind gets used to the paradigm one realizes its power and simplicity. Compared to all the JS visualization frameworks that I have used (Dojo, jQuery, Raphael, mootools, YUI, Google toolkit, FusionCharts etc) D3 is in a class of its own. Once you get hooked to creating charts/visuals the D3 way, I bet you wont go near anything else!</div>
        <div class="col-md-5 right">jsPlumb is truly simple. As a well thought out, well written and well documented library, one can start having working graphs in less than a day (which would be quite a challenge for D3 newbie to accomplish)</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Rendering Speed</h5></div>
        <div class="col-md-5 left">No other JS framework in that I have come across comes even in the vicinity of D3 in speed and performance. D3 is a class act. And this is for sure!</div>
        <div class="col-md-5 right">Definitely not slow</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Layer transitions, Panning, Zoom</h5></div>
        <div class="col-md-5 left">D3 is built for zoom, pan like functionality from bottoms-up. The transitions are smooth, fast and just work</div>
        <div class="col-md-5 right">Requires some doing</div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 first"><h5>Project Liveness, Community, Future roadmap</h5></div>
        <div class="col-md-5 left">Super active. Its one of the most cloned projects in the JS world on GitHub. There is a large community of users and questions are quickly answered on StackOverflow, Google groups etc. With such strong foundations, I dont see the momentum behind D3 slowing down in near future</div>
        <div class="col-md-5 right">Not as hot as D3 but nevertheless very popular. Enjoys a fairly large community of users and in the tradition of jQuery plugin's one can easily see, understand, tweak the library's code which seems straightforward to understand for good developers on a demanding projects</div>
    </div>
</div>

### APM Products
<ol>
    <li>The nodes in the topology are representative of the components (in AppsOne terminology). The links in the topology are representative of transactions</li>
    <li>multi-level Application Groups</li>
    <li>heterogeneous groups</li>
    <li>The n:n mapping between Application and Application-group is 'soft' or 'tag-like'. Customers want to easily create new application-groups and add/remove applications from existing groups (all the time). This calls for a flexible model</li>
    <li>Different 'Users' might want to see application topology's with different applications and groups on them. Since the whole idea of Application Topology is logical and per user understanding (and not something physical) - a user would have multiple topology views with some applications and groups present in many. Example, a user could define -
        <ol>
            <li>Topology Layer 'A' with 2 applications - 'CRM', 'CoreBanking' - and 2 application groups - 'InternalBusinessApps', 'InternalOperationsApps'</li>
            <li>Topology Layer 'B' with 1 application - 'CoreBanking' and 4 application groups - 'InternalBusinessApps', 'InternalOperationsApps', 'CustomerFacingApp', 'CriticalInterfacingApps'</li>
            <li>So now, between Layer 'A' and Layer 'B' there is one overlapping application and 2 overlapping application-groups</li>
        </ol>
     </li>
    <li>'origin' or 'destination' for individual transactions</li>
    <li>Links in different layers would have a configurable set of transactions mapped on them. Going back to the earlier example of layers 'A' and 'B' - the link between CRM and InternalBusinessApps in layer-A can be configured to show the status per a configured set of Transactions, say TxA and TxB. While the link between the same CRM and InternalBusinessApps in layer-B can be configured to show the status per TxB and TxC</li>
    <li>Nodes in different layers would have a configurable set of components mapped on them. Going back to the earlier example of layers 'A' and 'B' - the node for CRM in layer-A can be configured to show the status per a configured set of Components, say ServerA and DatabaseB. While the same CRM in layer-B can be configured to show the status per DatabaseB and AppServerC</li>
    <li>Once a user defines multiple layers of topology he needs to stitch the transition. Transitions are invoked on double click of an Application Group/Tag. Apart from the configurable option, this action requires a default which will show a topology layer of all individual application constituents of a Application Group</li>
    <li>'intra-application' and 'inter-application' views</li>
    <li>User is presented with multiple topology views per definition of layers. User can group multiple topology views into a single directory per context</li>
</ol>

<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojox/image/resources/image.css" media="screen">
<div id="apm"></div>





