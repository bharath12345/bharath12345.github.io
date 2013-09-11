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

... is the web server. As a JVM, JavaScript and (formerly) C++ programmer I took a tour of the popular web-server implementations in each of these technology areas. This post is on what I discovered.

### Quantifying the 'Bleeding Edge'
Why is the web-server the bleeding edge?

1. Twitter
This recent article - http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html -
says 300K requests per second for reading and 6000 RPS for writing.

https://blog.twitter.com/2013/new-tweets-per-second-record-and-how

2. WhatsApp
10 billion sent and received in one day - http://thenextweb.com/mobile/2013/06/13/whatsapp-is-now-processing-a-record-27-billion-messages-per-day/

3. Facebook
12 million HTTP requests per second - http://www.datadoghq.com/2013/07/the-best-of-velocity-and-devopsdays-2013-part-ii/

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






