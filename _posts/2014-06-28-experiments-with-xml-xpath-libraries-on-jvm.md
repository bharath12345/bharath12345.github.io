---
layout: post
title: "Experiments with XML XPath libraries on JVM"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
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

One important consideration while choosing a XML library is the API. But that is project specific and I leave it out of this comparison.

### Results Tabulated

<table class="table table-striped table-bordered table-hover table-condensed">
	<thead>
		<tr>
			<th colspan="11" class="text-center">Xmx512m</th>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td><strong>Time Taken</strong></td>
			<td><strong>App CPU Usage</strong></td>
			<td><strong>GC CPU Usage</strong></td>
			<td><strong>App Heap Size</strong></td>
			<td><strong>Heap Used</strong></td>
			<td><strong>Eden collection count/time spent</strong></td>
			<td><strong>Old Gen collection count/time spent</strong></td>
			<td><strong>Eden pattern</strong></td>
			<td><strong>Survivor pattern</strong></td>
			<td><strong>Old Gen pattern</strong></td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>scala.xml</strong></td>
			<td>240s</td>
			<td>70-80%</td>
			<td>20%</td>
			<td>512M</td>
			<td>250-300M</td>
			<td>359/15.2s</td>
			<td>303/3m18s</td>
			<td>either 0M or 170M</td>
			<td>not much usage</td>
			<td>between 170-340M</td>
		</tr>
		<tr>
			<td><strong>javax.xml.xpath</strong></td>
			<td colspan="10" class="text-center">does not complete</td>
		</tr>
		<tr>
			<td><strong>net.sf.saxon.xpath</strong></td>
			<td>67s</td>
			<td>60-80%</td>
			<td>20%</td>
			<td>512M</td>
			<td>250-300M</td>
			<td>162/6.2s</td>
			<td>123/39.3s</td>
			<td>0-170M tall spikes</td>
			<td>consistent use of 57M * 2</td>
			<td>stepwise between 0-340M</td>
		</tr>
		<tr>
			<td><strong>vtd.xml</strong></td>
			<td>11s</td>
			<td>26%</td>
			<td>0.10%</td>
			<td>500M</td>
			<td>150-250M</td>
			<td>13/138ms</td>
			<td>9/262ms</td>
			<td>between 100-170M</td>
			<td>very less and infrequent</td>
			<td>between 80-240M</td>
		</tr>
	</tbody>
	<thead>
		<tr>
			<th colspan="11" class="text-center">Xmx1024m</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>scala.xml</strong></td>
			<td>85s</td>
			<td>70-80%</td>
			<td>20%</td>
			<td>1G</td>
			<td>250-500M</td>
			<td>299/36s</td>
			<td>38/14s</td>
			<td>0-340M tall spikes</td>
			<td>100M consistent</td>
			<td>80-600M neat triangles</td>
		</tr>
		<tr>
			<td><strong>javax.xml.xpath</strong></td>
			<td>57s</td>
			<td>50-70%</td>
			<td>10-20%</td>
			<td>1G</td>
			<td>250-500M</td>
			<td>197/14s</td>
			<td>34/15s</td>
			<td>0-340M tall spikes</td>
			<td>100M consistent</td>
			<td>200-600M neat triangles</td>
		</tr>
		<tr>
			<td><strong>net.sf.saxon.xpath</strong></td>
			<td>49s</td>
			<td>50-70%</td>
			<td>10-20%</td>
			<td>1G</td>
			<td>250-500M</td>
			<td>110/12s</td>
			<td>34/15s</td>
			<td>0-340M tall spikes</td>
			<td>100M consistent</td>
			<td>200-600M neat triangles</td>
		</tr>
		<tr>
			<td><strong>vtd.xml</strong></td>
			<td>11s</td>
			<td>30%</td>
			<td>1-2%</td>
			<td>300-800M</td>
			<td>200-700M</td>
			<td>11/66ms</td>
			<td>6/204ms</td>
			<td>200-300M</td>
			<td>10M</td>
			<td>400-600M</td>
		</tr>
	</tbody>
	<thead>
		<tr>
			<th colspan="11" class="text-center">Xmx2048m</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>scala.xml</strong></td>
			<td>70s</td>
			<td>70-80%</td>
			<td>10-20%</td>
			<td>2G</td>
			<td>0.5-1G</td>
			<td>154/27s</td>
			<td>26/21s</td>
			<td>0-680M tall spikes</td>
			<td>100M consistent</td>
			<td>200M-1G neat triangles</td>
		</tr>
		<tr>
			<td><strong>javax.xml.xpath</strong></td>
			<td>59s</td>
			<td>40-70%</td>
			<td>10-20%</td>
			<td>2G</td>
			<td>0.5-1G</td>
			<td>105/14s</td>
			<td>23/17s</td>
			<td>0-680M tall spikes</td>
			<td>100M consistent</td>
			<td>0.3-1.1G</td>
		</tr>
		<tr>
			<td><strong>net.sf.saxon.xpath</strong></td>
			<td>39s</td>
			<td>40-70%</td>
			<td>10-20%</td>
			<td>2G</td>
			<td>0.5-1G</td>
			<td>69/10s</td>
			<td>18/8s</td>
			<td>0-680M tall spikes</td>
			<td>200M consistent</td>
			<td>300-600M</td>
		</tr>
		<tr>
			<td><strong>vtd.xml</strong></td>
			<td>11s</td>
			<td>26%</td>
			<td>0%</td>
			<td>0.5-1.25G</td>
			<td>0.5-1.25G</td>
			<td>14/190ms</td>
			<td>6/272ms</td>
			<td>600M consistent</td>
			<td>200M</td>
			<td>1.3G no pattern</td>
		</tr>
	</tbody>
</table>


<div id="javaxcpumem"></div>



