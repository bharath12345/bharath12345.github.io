---
layout: post
title: "Play2 on Wildfly"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---
JavaEE-5 and JavaEE-6 have a commanding presence in both marketshare and (developer) mindshare in the enterprise software world. The specifications are very well thought-out, battle-tested and highly relied upon. I started using JavaEE-5 way back in 2007 with JBoss 4.x. Now, JavaEE-7 was released close to a year ago. So I read a few books to understand all the new features that JavaEE-7 brings (and attended JUDCon Bangalore). I have also been coding and acquainting myself with Typesafe's Scala stack. In the coming days, JavaEE-7 will have to face-off with two really daunting challenges  -

1.  Horizontal scalability
2.  Idea of complete statelessness to satisfy near real-time data

So, among all the JavaEE specs, I feel JSF is the *loose brick*.

Now, a word about other JavaEE technologies before going back to JSF -  

* Stateless EJB's have no equivalent in the stateless Scala world, yet. This is because of the lack of an application server in that world... though DI as a design pattern is eminently programmable. So EJB's can be made to scale with application server clustering. And EJBs are a proven technology with massive investment already - so I feel, they will stay and do well for a long time to come
* Nextly, Persistence. Hibernate is a killer technology. Though not scalable or performant, it is here to stay just because all products have a lot of data in SQL databases that have no *performance* constraints attached to them. Like configuration data
* Messaging. I am no expert in this area and hence won't comment

### Web Tier In JavaEE - *the loose brick?*
I would group the Web Tier of modern enterprise applications into 3 baskets. 

* The JavaEE specifications mandate JSF as the technology to build user interfaces for web applications. JSF is an aggregate of multiple technical pieces which include facelets, expression language, converters, listeners, validators etc. Modern dynamic web applications place a plethora of requirements on the server-side like composable components, server side data validation, json transformation etc. JSF tries to satisfy all. And since UI usecases are ever changing, the effort of the spec writers has been to give a technology that can scale from a development standpoint. Developers treat JSF as a *component* framework, which means it is suited for applications with lot of forms and CRUD operations. It abstracts away a lot of *state* information in its stack which is not good if UI serves a lot of *read only* and *voluminous* data. Now, there are *other* web-component frameworks (non JSF compliant) like Apache Wicket and Tapestry. And there are those like RichFaces and PrimeFaces which comply to JSF and provide more functionality (above and beyond the spec) 
* For *read-only* and voluminous data handling atop servlets *action* frameworks are preferred which explicitly tie to the HTTP request/response cycle. Action frameworks typically implement the famous MVC pattern for clear separation of concerns. So applications tend to use frameworks like Struts, SpringMVC etc
* Finally the ugly ones. JSP. GWT. Dart. I dislike each of these so much that I won't spend any more of my time into explaining them. These are just *pure evil*

### Play Framework
Having done quite a bit of programming in JSP and JSF, I have found Play to be fresh breath of air. That Guillaume Bort made the decision to not write yet another framework on servlets was a good starting point ([this blog](http://guillaumebort.tumblr.com/post/558830013/why-there-is-no-servlets-in-play) is a good read). I built my blog on Play.

Let me list the specific features that I found especially useful and important -

* Scala templating with compile time type safety
* Less verbose code
* JavaScript compilation
* Hot deployment during development
* Netty underneath
* Stateless. Easy to use Akka with it
* Websockets - Futures, Async
* Cloud deployment on Heroku, Cloudbees etc

### JavaEE + Play2
Since I claim JSF to the *loose brick* in JavaEE stack and Play2 to be a wonderful replacement + application containers are good to have in enterprise setups => is it possible to use Play2 app within Wildfly? Yes, with Play2War plugin. It does the whole job except websockets. I really feel Play2 will be a really good fit even in the JavaEE stack a few years down the line when some more bridges will appear around it to make it easily compatible to JavaEE application servers


