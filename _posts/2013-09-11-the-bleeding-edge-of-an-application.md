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

... is the web server along with the HTTP software stack that powers it. Of the many reasons that make this layer extremely challenging for software development let me just state a few -

* Huge quantum of requests. Both for static web pages and dynamic content
* Change. Websites and services change very often
* Variety of consumers. People read/write to web. And so do software applications using web-services etc

A few weeks ago I decided to study this area thoroughly. Being a Java and JavaScript developer, my focus was on the emergent software stacks in these languages. And to understand what is/was lacking in the frameworks that exist/have-gone-by. Unearth the real problems of the web-layer from development and deployment standpoint. This blog is an attempt to digest what I discovered.In this blog, I start by quantifying the numbers that make the web-layer the bleeding edge for software development. I then have a look at some of the core technical problems. Finally a comparison of software stacks.

Before starting on the sections, I request my readers to have a look at these two webpages before proceeding further -

1. [Netcraft's September 2013 Web Server Survey](http://news.netcraft.com/archives/2013/09/05/september-2013-web-server-survey.html) - These graphs are instructive. All the top web-servers are C/C++ based. But for those who are not familiar with actual application deployments, the thing to note is that these web-servers are seldom used to host real applications. They serve static pages and act as load-balancers for dynamic ones. Firewalls and load-balancers are placed at the very gate of modern web-shops. Any and all requests go through them. And their tasks are generally simpler than business applications. So it makes sense to develop them in native languages for brute speed. A hundred load-balancing servers would generally be supporting 8X times or more of application servers. The requests that land at this C/C++ load-balancing web-tier are forwarded to the application-tier. And responses from the application-tier are sent back along the same path. The focus of this blog is on the web-layer at this application-tier and *not* at the web-tier.
2. [The Reactive Manifesto](http://www.reactivemanifesto.org) - In this blog I plan to work my way through explaining why *the reactive manfiesto* and event-driven model are such fine ideas. However please do take some time out to read it. Especially that graph on Amdahl's Law…      

### Quantifying the 'Bleeding Edge'
Here are the numbers from recently published articles on Twitter, WhatsApp and Facebook. There are others who could be far behind like Google Search, Wikipedia etc. 

1. Twitter: [This recent article](http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html) says 300K requests per second for reading and 6000 RPS for writing. And Twitter's own [blog](https://blog.twitter.com/2013/new-tweets-per-second-record-and-how) talks about new peaks

2. WhatsApp: [This article](http://thenextweb.com/mobile/2013/06/13/whatsapp-is-now-processing-a-record-27-billion-messages-per-day/) puts the numbers at 10 billion messages sent and received in one day recently

3. Facebook: was getting no less than 12 million HTTP requests per second not very long ago per [this article](http://www.datadoghq.com/2013/07/the-best-of-velocity-and-devopsdays-2013-part-ii/) 

### JVM based web-apps
#### Web application stack
##### Servlet Specification
##### The Reactive Manifesto
#### Web servers
#### Tomcat
#### Jetty
#### Netty

### NodeJS - The JavaScript web-server

### C/C++ web-servers
#### Apache
#### Nginx






