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

### Web Tier In JavaEE - *The Loose Brick?*
This was a recent tweet by Peter Thomas -

<a style="float: left; padding-right: 2em" href="https://twitter.com/ptrthomas/statuses/428460021265887232">![image](http://bharathwrites.in/images/peter%20thomas%20tweet.png)</a>

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

[This one](http://www.slideshare.net/brikis98/composable-and-streamable-play-apps) is a excellent presentation (and [code](https://github.com/brikis98/ping-play)) by Yevginy Brikman from LinkedIn (LinkedIn uses Play! for multiple web apps in its stack). The title is apt - building web apps that are composable and streamable. More and more, enterprise applications have UI requirements of the kind described here. And building these using JSF/Java would be too complex a web project and not worth the trouble!    

### HOWTO - Play2 on Wildfly to interop with JavaEE
For very good reasons enterprise applications are generally hosted on application containers. And application containers mostly come built with a servlet container for web frontend. So does it mean using Play! in enterprise applications straightaway get vetoed? Not necessarily. If the engineers have a little chutzpah, the gap can be bridged. Here is how I was able to host my Play2 application on JBoss-Wildfly -

1. The thing to study and use for the task is the [Play2War](https://github.com/dlecan/play2-war-plugin) plugin. Play2War builds a WAR out of the Play2 application which I was then able to deploy on Wildfly
2. After following the usage/configuration instructions from the Play2War's GitHub page, the first thing to do is to configure the *excludes*. That is, number of JARs that will get packaged using Play2War would clash with JBoss's modules. Here is a quick list of such JAR's from my project -
<table class="table table-striped table-bordered table-condensed">
  <thead>
  	<tr>
  	  <th>Artifact</th>
  	  <th>GroupID</th>
  	  <th>Play Version</th>
  	  <th>Wildfly Version</th>
  	  <th>Newer</th>
  	</tr>
  </thead>
  <tbody>
    <tr>
      <td>Google Guava</td>
      <td>com.google.guava</td>
      <td>14.0.1</td>
      <td>16.0.1</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Jackson Core, Annotations and Databind</td>
      <td>com.fasterxml.jackson.core.jackson* </td>
      <td>v2.2.2</td>
      <td>v2.3.0</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>H2 Database</td>
      <td>com.h2database.h2*</td>
      <td>v1.3.172</td>
      <td>v1.3.173</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Apache Commons Codec</td>
      <td>org.apache.commons.codec</td>
      <td>v1.6</td>
      <td>v1.9</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Apache Commons IO</td>
      <td>org.apache.commons.io</td>
      <td>v1.3.2</td>
      <td>v2.4</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Netty</td>
      <td>io.netty</td>
      <td>v3.7.0</td>
      <td>v4.0.15</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Hibernate Commons Annotations</td>
      <td>org.hibernate</td>
      <td>v4.0.2</td>
      <td>v4.0.4</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Hibernate Core, Entity Manager</td>
      <td>org.hibernate</td>
      <td>v4.2.3</td>
      <td>v4.3.1</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Hibernate Validator</td>
      <td>org.hibernate</td>
      <td>v5.0.1</td>
      <td>v5.0.3</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Javaassist</td>
      <td>org.javaassist</td>
      <td>v3.18.0</td>
      <td>v3.18.1</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>JBoss Logging</td>
      <td>org.jboss.logging</td>
      <td>v3.1.1</td>
      <td>v3.1.4</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>JBoss Transaction</td>
      <td>javax.transaction.api</td>
      <td>v1.0.0</td>
      <td>v1.0.1</td>
      <td>Wildfly</td>
    </tr>
    <tr>
      <td>Yaml</td>
      <td>org.yaml.snakeyaml</td>
      <td>v1.12</td>
      <td>v1.13</td>
      <td>Wildfly</td>
    </tr>
    <tr>      
      <td>Antlr</td>
      <td>org.antlr</td>
      <td>v2.7.7</td>
      <td>v2.7.7</td>
      <td>Same</td>
    </tr>
    <tr>
      <td>dom4j</td>
      <td>org.dom4j</td>
      <td>v1.6.1</td>
      <td>v1.6.1</td>
      <td>Same</td>
    </tr>
    <tr>
      <td>Postgres</td>
      <td>org.postgres</td>
      <td>v9.1-901</td>
      <td>v9.1-901</td>
      <td>Same</td>
    </tr>
    <tr>
      <td>javax.validation</td>
	  <td></td>
      <td>v1.1.0</td>
      <td>v1.1.0</td>
      <td>Same</td>
    </tr>
    <tr>
      <td>Joda time</td>
      <td>org.joda.time</td>
      <td>v2.2</td>
      <td>v1.6.2</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>Apache Commons Lang</td>
      <td>org.apache.commons.lang</td>
      <td>v3.1</td>
      <td>v2.6</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>HttpCore</td>
      <td>org.apache.httpcomponents.</td>
      <td>v4.3.1</td>
      <td>v4.2.1</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>HttpClient</td>
      <td>org.apache.httpcomponents.</td>
      <td>v4.3.2</td>
      <td>v4.2.1</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>Hibernate JPA</td>
      <td>javax.persistence.api</td>
      <td>v1.0.1</td>
      <td>v1.0.0</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>Asm</td>
      <td>asm.asm</td>
      <td>v4.1</td>
      <td>v3.3.1</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>jcl-over-slf4j</td>
      <td>org.slf4j</td>
      <td>v1.7.5</td>
      <td>v1.7.2</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>jul-to-slf4j</td>
      <td>org.jboss.logging</td>
      <td>v1.7.5</td>
      <td>v1.0.1</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>slf4j-api</td>
      <td>org.slf4j</td>
      <td>v1.7.5</td>
      <td>v1.7.2</td>
      <td>Play</td>
    </tr>
    <tr>
      <td>Xerces</td>
      <td>org.apache.xerces</td>
      <td>v2.11</td>
      <td>v2.9.1</td>
      <td>Play</td>
    </tr>
  </tbody>
</table>

3.  

One caveat - websocket support is missing.

Since I claim JSF to the *loose brick* in JavaEE stack and Play2 to be a wonderful web framework + application containers are good to have in enterprise setups => is it possible to use Play2 app within Wildfly? Yes, with Play2War plugin. It does the whole job except websockets. I really feel Play2 will be a really good fit even in the JavaEE stack a few years down the line when some more bridges will appear around it to make it easily compatible to JavaEE application servers
