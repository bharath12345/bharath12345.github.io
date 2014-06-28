---
layout: post
title: "Experiments with XML XPath libraries on JVM"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

These days I mostly program in Scala. Few weeks ago I ran into a problem to search for data within fairly large XMLs. XPath and XQuery are the standard technologies to query XML's. JVM programmers have a choice of multiple libraries to choose from when it comes to XPath. One constraint in my problem was that the program to crunch these XML was a long-running one. So, apart from trying to make the search fast I had to make sure that the CPU/memory requirements were sane. On submitting a XPath search if a library forked many hundred threads, broke the XML into many hundred stubs thus consuming every single ounce of CPU/RAM at disposal on my machine, then it was simply a no-go. Even if such a library turned out to be an order of magnitude faster than the rest.

A look at the XML-XPath JVM library landscape made me shortlist the following for a quick investigation - 

* [scala.xml](https://github.com/scala/scala-xml) - Scala's built-in parser
* [javax.xml.xpath](http://docs.oracle.com/javase/7/docs/api/javax/xml/xpath/package-summary.html)
* [net.sf.saxon](http://saxon.sourceforge.net/saxon7.7/api-guide.html)
* [vtd-xml](http://vtd-xml.sourceforge.net/)

This post is a work-in-progress and I will refrain from drawing conclusions. As and when I find more, I shall add. Some passing reader may find the numbers helpful for some other cause in the wild.

Now, the environment details -

* The approx size of XML's I used was ~ 70MB. That does not make it very large but the complexity of the structure can be the *dark* variable in XML processing. Even a 5MB XML with small elements, recursive lookups etc (those that people refer to as XML *database*) can be much harder to search within than a 500MB one which has a straight simple flow (say like Log4J Xml logs). The XML I used was neither as complex as a *database* or as simple as a *log*. It was more alike the *configuration* (more complex than tomcat web.xml but similar) XML files with fairly deep nesting
* All numbers are mean over run of 30 iterations. they should be treated as ballparks
* Tests were run on my 4core 8GB Mac OSX Mavericks
* Java version "1.7.0_51". Scala version "2.11.0"
* No cpu/memory hungry process running on the system while running the test. It was just a text editor, console, test application and operating system services after a fresh reboot
* Tests tried with 4 big buckets of Xmx setting - 512M, 1024M, 2048M, 4096M
* All numbers and screen captures are with jvisualvm. wanted to use jstat but got a little lazy

One important consideration while choosing the right XML library is the API. But that is project specific and I leave it out of this comparison.



