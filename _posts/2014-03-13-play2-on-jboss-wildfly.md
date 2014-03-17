---
layout: post
title: "Play2 Application on Wildfly: Why and How"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
---
[JavaEE](http://en.wikipedia.org/wiki/Java_Platform,_Enterprise_Edition) (v5 and v6) has a commanding presence in both marketshare and (developer) mindshare in the enterprise software world. The specifications are well thought-out, battle-tested and highly relied upon. I started using JavaEE (v5) way back in 2007 with JBoss 4.x. The latest release, [JavaEE-7](http://www.oracle.com/technetwork/java/javaee/tech/index.html), which was released close to a year ago brings with itself a lot of worthy changes to the specs and impl. To bring myself up to speed on it I went through a few books and attended a conference (JUDCon, Bangalore). But I have also been coding and acquainting myself with Typesafe's Scala *[reactive](https://typesafe.com/platform)* stack. These two stacks are bound to compete with each more and more in the coming days. However I feel, they can be used in applications in complementary ways when carefully designed. The competition and challenge to JavaEE-7 stems from two tough requirements -

1.  Horizontal scalability
2.  Near real-time persist/process/view of ever increasing data volumes

The JavaEE stack is broadly split into 3 tiers - web, business and persistence. JSF (broadly, including expression-lang, JSTL, JSP and Servlets) is the technology of choice (per the specs) in the web tier. And JSF, to me, seems most vulnerable of *not* being able to raise up to the above mentioned two challenges. JSF does feel like the *loose brick* in the JavaEE stack. And it feel ever more so after spending some time with the [Play Framework](http://www.playframework.com/)!

### Web Tier In JavaEE - *the loose brick?*
This was a recent tweet by Peter Thomas -

<a href="http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-05-58.png">![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-05-58.png =430x238)</a>

<blockquote class="twitter-tweet" lang="en"><p>ThoughtWorks on <a href="https://twitter.com/search?q=%23JSF&amp;src=hash">#JSF</a>: &quot;We continue to see teams run into trouble [..] and are recommending you avoid this technology&quot; <a href="http://t.co/hzW6PYSzVZ">pic.twitter.com/hzW6PYSzVZ</a></p>&mdash; Peter Thomas (@ptrthomas) <a href="https://twitter.com/ptrthomas/statuses/428460021265887232">January 29, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I group the Web Tier of JavaEE applications as consisting of code and relying on libraries from 3 baskets. The bullet points are notes on each of these... 

1. **Component Frameworks**: 
   * Component frameworks like JSF are suited for parts of the application with lot of forms and CRUD operations. JSF is an aggregate of multiple technical pieces which include facelets, expression language, jstl, converters, listeners, validators etc.  JSF helps build composable UI components with server side validation in a scalable way
   * It abstracts away a lot of *state* information in its stack which is not good for building UI components that serve a lot of *read only* and *voluminous* data. Tasks like JSON transformation within JSF are not efficient at scale 
   * Now, rarely do programmers get completely satisfied with the component library within JSF. So they use the richer component frameworks (above and beyond JSF) like Apache Wicket and Tapestry. And for dynamic pages with lot of AJAX there are frameworks like RichFaces and PrimeFaces which provide features atop JSF
2. **Action Frameworks**: For *read-only* and voluminous data handling atop servlets *action* frameworks are preferred which explicitly tie to the HTTP request/response cycle. Action frameworks typically implement the famous MVC pattern for clear separation of concerns. So applications tend to use frameworks like Struts, SpringMVC etc
3. **Standalone, Proprietary Frameworks**: These are the ones that are unbelievably beautiful for quick-small projects and unbelievably ugly for large ones. Technologies like JSP, GWT, Dart et al. These are just *pure evil* from enterprise products perspective

### Play Framework
With me having done quite a bit of programming in JSP and JSF, I found Play to be fresh breath of air. Web application programmers must spend some time reading and understanding ([this blog](http://guillaumebort.tumblr.com/post/558830013/why-there-is-no-servlets-in-play) by Guillaume Bort on reasons behind the decision to not write yet another framework atop Java HttpServlet. My experience with Play has been by building a lookalike for my blog with it (hosted on Heroku [here](http://bharathplays.herokuapp.com)). I have built my blog on NodeJS and RubyRails as well - and honestly, it took much lesser time to build it with Play. But more important is the question of should enterprise web-tiers be programmed with Play? Is Play up to the mark for projects of development scale and complexity? My answer is a thumping YES!!

Let me list the specific features that I found especially useful and important -

* Scala templating with compile time type safety - I have found UI composition to be very intuitive and much simpler than JSF (JSF's composability really feels like a mess when compared with Play!)
* Websockets - Futures, Async - much better API for streaming data than the WebSocket Spec in JavaEE
* Stateless. Easy to use with Akka
* Marshalling/unmarshalling of JSON data without reflection which provides huge performance improvement
* Explicit, clean server side routing methodology (what a mess this is in JavaEE where programmers often mix annotations, xml *and* client-side routing) 
* No server side sessions at all! 
* Built-in build-time JavaScript compilation
* [WebJars](http://www.webjars.org/)
* Less verbose Scala code. The joy of composable functional programming
* Hot deployment during development
* Netty underneath - performance no issue
* Cloud deployment ready (Heroku, Cloudbees support it)

### JavaEE + Play2
Since I claim JSF to the *loose brick* in JavaEE stack and Play2 to be a wonderful replacement + application containers are good to have in enterprise setups => is it possible to use Play2 app within Wildfly? Yes, with Play2War plugin. It does the whole job except websockets. I really feel Play2 will be a really good fit even in the JavaEE stack a few years down the line when some more bridges will appear around it to make it easily compatible to JavaEE application servers
