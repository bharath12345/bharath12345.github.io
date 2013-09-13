---
layout: post
title: "The Bleeding Edge Of A Web Application..."
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
---

Typical web applications have the well-known 3-tiered structure. WebTier > ApplicationTier > DataTier. Both WebTier and ApplicationTier have the web-layer to parse the incoming HTTP requests. Its in the WebTier that one deploy's load-balancing L4-routers like Apache/Nginx or Netscaler like appliances. HTTP requests are forwarded by the WebTier to the ApplicationTier which is generally served by a much bigger farm of servers. Web-layer in the ApplicationTier is the focus of this blog. Its one of the most challenging areas of software development. Among the reasons are - 

* Huge quantum of requests, with *read* generally surpassing *write* by an order of magnitude or so
* Change. Website content and web-service APIs both change very often
* Variety of consumers. People read/write to the web. And so do other software applications

Being a Java and JavaScript developer, my interest is in the emergent software stacks in these two languages. To understand their *raison d'être*. I intend to start by quantifying the numbers (HTTP requests). Then take a look at some of the core technical problems. Finally a comparison of the competing software stacks.

But before starting on the web-layer in the ApplicationTier it is instructive to look at the pure WebTier itself. Its instructive to read [Netcraft's September 2013 Web Server Survey](http://news.netcraft.com/archives/2013/09/05/september-2013-web-server-survey.html). All the top web-servers are C/C++ based. For those unfamiliar with actual application deployments, these web-servers are not used to host real applications. They serve static pages, act as L4-routers and load-balancers. They are placed at the very gate of modern web-shops and all requests go through them. Their tasks are simpler than business applications. So it makes sense to develop them in native languages for brute speed.   

<hr>   

#### 1. Quantifying the 'Bleeding Edge'
Here are the numbers from recently published articles on Twitter, WhatsApp and Facebook. There are others who could not be far behind like Google, Wikipedia, Amazon, Skype etc. 

1. Twitter: 300K requests per second (RPS) for reading and 6000 RPS for writing - [Source1](http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html), [Source2](https://blog.twitter.com/2013/new-tweets-per-second-record-and-how)
2. WhatsApp: 10 billion requests sent and received in one day - [Source](http://thenextweb.com/mobile/2013/06/13/whatsapp-is-now-processing-a-record-27-billion-messages-per-day/) 
3. Facebook: 12 million HTTP requests per second - [Source](http://www.datadoghq.com/2013/07/the-best-of-velocity-and-devopsdays-2013-part-ii/) 

(*All these articles are quite recent*)

<hr>

#### 2. Why Is It Hard?
Two good resources to start understanding why these scales are hard on the ApplicationTier are -

1. C10K problem by [Kegel](http://www.kegel.com/c10k.html) and [Felix von Leitner](http://bulk.fefe.de/scalable-networking.pdf)
2. C10M problem by [Robert Graham](http://c10m.robertgraham.com/p/manifesto.html). And [this video](http://www.youtube.com/watch?v=D09jdbS6oSI) by him is very instructive 

But let me state the problem(s) simply. The reasons why it is hard to handle HTTP requests in web-layer are -

1. **Forking a process**: is too expensive a compute operation to perform everytime a request arrives
2. **Forking a thread**: is less expensive on compute. But writing multi-threaded applications for multi-core systems is very tough (and *actually* forking a new thread is not inexpensive at all)
3. **Use thread pools**: It just shifts the bottleneck. Once you have a thread-pool, each thread has to do a select() or poll() to find the next nonblocking socket ready for IO. But doing a select() or poll() on a huge array of open socket descriptors is extremely inefficient at the kernel level (checkout the deep analysis to C10K problem in the above mentioned links)
4. **The Event driven model**: requires a paradigm shift in thinking and designing applications from bottoms-up. The best way to start grasping the idea is to read the [the Reactive Manifesto](http://www.reactivemanifesto.org). This model is not very different from the SEDA architecture. Reactive applications is a very fine idea and one of the reasons why I dwelled into this subject in the first place…

<hr>

#### 3. Software Development Of Web Applications
Broadly there are 3 different ways to develop web applications -

* JVM Based
* Ruby, PHP
* NodeJS

I dwell into each of these in the next few sections. 

#### 4. JVM Based Web Apps
The web-layer in JVM world is filled with 3 types of frameworks - 

1. Frameworks that support the *servlet specification* (latest one is 3.0) 
2. MVC frameworks 
3. Asynchronous event-driven frameworks based on Netty

##### (i) Servlet Specification Frameworks
These include Tomcat and Jetty. What is the main motivator for the servlet spec? It is to manage state information that does not exist in the stateless HTTP protocol. [HttpServletRequest](http://docs.oracle.com/javaee/6/api/javax/servlet/http/HttpServletRequest.html) provides an API getSession() where the HttpSession object is a container to hold attributes for a single transaction spread across multiple HTTP request/responses. Apart from this central feature of sessions the servlet API also defines the interfaces that the servlet container has to adhere-to to provide concurrent request processing in a sandbox environment. So whats the drawback? The very idea of *state* brings down the performance of these containers. Thats the reason why developing highly performant RESTful APIs using servlet containers is a bad idea. Client maintains the *state*, if required, in [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer). Many servlet containers can be tuned for statelessness - but then, that goes against one of the fundamental motivators for the spec. And my readings tell me that these frameworks don't become highly performant on turning off the statefullness.

##### (ii) MVC Frameworks
These include Spring MVC, Struts, Tapestry, Wicket etc. I have used two of these - [Struts2](http://struts.apache.org/) and [Wicket](http://wicket.apache.org/) in building applications that have seen deployment. The fundamental motivation for these frameworks is ease-of-development (annotations etc), clean separation of concerns (MVC design pattern), a lot of goodies (like templating etc) and integration with other JavaEE stacks (Struts2-Spring integration like). 

##### (iii) Asynchronous Event-Driven Frameworks
And now I come to the most interesting area of Java web application development. [Netty](http://netty.io/) based frameworks like [Play!](http://www.playframework.com/) and [Vert.x](http://vertx.io/). These frameworks do not comply to the servlet specification. They use Netty underneath for asynchronous event based handling of HTTP requests (I cover *what-the-hell-is* asynchronous event-driven in the NodeJS section below). Netty is stateless - so the server side is automatically stateless and fast. The frameworks on top are built to exceed the ease-of-dev and richness offered by the likes of Struts and Tapestry. They also offer APIs for client-side statefulness. So these frameworks are an effort to mix high performance with ease-of-dev. But moving to event-based and asynchronous thinking is not straightforward. It needs a mind shift akin to a transition to Object-oriented-programming. However the promise they hold is to be able to build web applications that defy [Amdahl's law](http://en.wikipedia.org/wiki/Amdahl's_law). If you are a new shop with bright Java engineers wanting to build a highly scalable web-application, then, these are the frameworks you should start exploring first...

<hr>

#### 5. NodeJS - JavaScript on the server side
The [list](https://github.com/joyent/node/wiki/Projects,-Applications,-and-Companies-Using-Node) of companies and websites powered by NodeJS is long. However Node is still a newcomer. Why would somebody want to use Node? NodeJS makes two very interesting promises -
* End-to-end JavaScript shop for you web application
* High performance through event-based asynchronous model

The first promise is easy to understand. Any good web application requires a team of good designers and client-side programmers. If the programming language on both client-side and server-side are the same, then it reduces the risk of investment in diverse technologies and brings down the barriers between teams and moving people.

The second promise of performance is more interesting. But before exploring why NodeJS claims to be fast it is good to pay a little attention to comparisons with the Java based async frameworks. Sample [this](http://www.cubrid.org/blog/dev-platform/inside-vertx-comparison-with-nodejs/) excellent comparison. It goes to show that NodeJS is no match to JVM based frameworks. (for me, that chart in the blog was very highly expected!)

But it pays to dwell a little more on the aspect of performance promised by event-driven asynchronous frameworks. The talk of such frameworks is increasing day-by-day. So how exactly does this help. NodeJS provides a good base to explore since one cannot do anything but asynchronous event-based HTTP processing with NodeJS! Let us study this code fragment for a while - (this comes from [this](http://shop.oreilly.com/product/0636920024606.do) excellent book on NodeJS by O'reilly)

<pre>
        // load http module
        var http = require('http');
        var fs = require('fs');

        // create http server
        http.createServer(function (req, res) {

	        // open and read in a file
	        fs.readFile('textfile.txt', 'utf8', function(err, data) {
		        res.writeHead(200, {'Content-Type': 'text/plain'});
		        if (err) {
			        res.write('Could not find or open file for reading\n');
		        } else {
			        // if no error, write file to client
			        res.write(data);
		        }
		        res.end();
	        });

        }).listen(8124, function() {
	        console.log('bound to port 8124');
        });

        console.log('Server running on 8124/');
</pre>

Following aspects need to be understood -

* The two instances of asynchronous behavior
* The program NEVER blocks
* Multiple types of events are emitted and consumed in a single giant event loop with the framework
* The application itself acts as one giant event-producing and event-consuming engine which should be seen as single-threaded and binding to a single-core
* To make use of multiple-cores multiple-instances of NodeJS can be run on the same system
* Large (NP-Hard) like computes should not be attempted - they take away all the processing core's bandwidth bringing the whole system to a halt. So, such event-based asynchronous processing is most suited for applications that can be broken down into multiple stages like a SEDA architecture

Finally NodeJS has found tremendous traction with developer community. Am heading to [JSFoo in Bangalore](https://jsfoo.in/2013/) next week, and one look at the speaker funnel will tell you that every second session has something to do with NodeJS. And the NodeJS based MVC frameworks like [Express](http://expressjs.com/), [Geddy](http://geddyjs.org/), [FlatironJS](http://flatironjs.org/), [EmberJS](http://emberjs.com/) etc are poised to give MVC frameworks in Ruby and PHP a run for their money in simplicity, performance and features. 

<hr>

#### 6. Ruby and PHP
With JVM based frameworks occupying one end of the pipeline offering { high-performance + Maintainability } and NodeJS based frameworks taking the other end with { simplicity + low-cost + ease-of-dev }, how much of middle-ground is left for PHP and/or Ruby? I am not an expert in either of these two, so I will stay away from making predictions. One thing that is fair to say in favour of PHP/Ruby is that both are *proven* in large production applications while reactive Java frameworks and NodeJS are still not there. How long will this status last? Will NodeJS and Java reactive frameworks take away a chunk of web applications that would otherwise have been Ruby/PHP's? Or will the internet applications playing field get expanded with the entry of these new players and is there room for all?
 
<hr>

#### 7. What to use for my project?
I roundoff my blog with a guidance, albeit reluctantly. Apart from the usual suspects of time-to-market, capex-opex, engineering skill and requirements-complexity that make project delivery complex, I would propose that there are few more criterions that should be payed heed to -

* Should projects be differentiate on the basis of packagable-products (bundled in a CDROM) from those delivered as part of a web company through a website or Saas?
* Should there be a differentiation between intra-enterprise and open-internet usage?
* Should there be a differentiation based on applications for human consumption to consumption by other software services?

I leave those aspects to the good judgement of my readers. I would definitely like to get feedback on those who disagree from my guidance below. The idea of writing this guidance is to paint broad strokes... Exceptions among project/people always exist!

<div class="bs-docs-grid" id="dev">
    <div class="row show-grid">
        <div class="col-md-2 right alignCenter"><h5>JVM Based</h5></div>
        <div class="col-md-10 left">
        	<ol>
                <li>Performance: JVM is worlds best VM in performance. Ruby/PHP/NodeJS are interpreted and don't come close in performance (doing any new project in JRuby according to me is simply a bad idea). Facebook created the HipHop JIT compiler for PHP to make it scale - this counts as an exception. Twitter shifted from Ruby to Scala (which is JVM based) and achieved higher performance numbers. One can find umpteen examples like this…</li>
                <li>Development Time: Java and other JVM languages are supposed to be slower to develop in compared to Ruby/PHP/NodeJS. This argument is very valid. And thats the reason why frameworks like Play! are trying to bridge the gap</li>
                <li>Cost: Java developers are more expensive</li>
                <li>Suited for: Large web applications. Enterprise products. Mission critical applications</li>
            </ol>
        </div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 right alignCenter"><h5>Ruby, PHP</h5></div>
        <div class="col-md-10 left">
        	<ol>
                <li>Performance: Definitely not bad</li>
                <li>Development Time: Fast</li>
                <li>Cost: Medium</li>
                <li>Suited for: Medium sized projects</li>
            </ol>
        </div>
    </div>
    <div class="row show-grid">
        <div class="col-md-2 right alignCenter"><h5>NodeJS</h5></div>
        <div class="col-md-10 left">
        	<ol>
                <li>Performance: The jury is still out. NodeJS has found adaption in only smaller web shops. Large scale production quality Node applications are still some distance away</li>
                <li>Development Time: Fast</li>
                <li>Cost: Low, since the whole application is built on a single language stack the server-side developers and client-side developers can co-work</li>
                <li>Suited for: Smaller chatty applications</li>
            </ol>
        </div>
    </div>
</div>








