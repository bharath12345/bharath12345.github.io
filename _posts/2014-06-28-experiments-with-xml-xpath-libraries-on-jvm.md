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

* 