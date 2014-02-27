---
layout: post
title: "My Scala Application: Real-time Twitter Volume Grapher For Indian Elections 2014"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
---

The Indian general elections are around the corner. For engineers, this time around, there is data to play with. Data from the social media giants - Twitter and Facebook. Though social media may not be the right barometer to judge voter sentiments in a country as big and diverse as India, it is nonetheless a very tempting datasource for anyone curious. So couple of days ago I decided to do a small project - to simply *chart* the volume of tweets with strings like "modi", "rahul", "kejri" and "india" in it. I thought just a graph of volumes by itself will be a interesting resource. So here I present the v1 of my Indian-general-elections-social-media-tracker!

### The Application
The application has 5 dashboards and a URL for each. Each URL is a dashboard of 4 graphs. Here is a quick summary of each - 

* ##### 3 Seconds Tweet Aggregate Grapher  
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/0](http://bharathplays.herokuapp.com/twitter/elections/0)
  * Dashboard Sample Image: ![image](http://)
  * Details: 
  
* ##### 30 Seconds Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/1](http://bharathplays.herokuapp.com/twitter/elections/1)
  * Dashboard Sample Image:
  * Details: 
  
* ##### 5 Minutes Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/2](http://bharathplays.herokuapp.com/twitter/elections/2)
  * Dashboard Sample Image:
  * Details: 
  
* ##### 30 Minutes Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/3](http://bharathplays.herokuapp.com/twitter/elections/3)
  * Dashboard Sample Image:
  * Details: 
  
* ##### 3 Hours Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/4](http://bharathplays.herokuapp.com/twitter/elections/4)
  * Dashboard Sample Image:
  * Details: 

### Design and Code
The code is on github [here](https://github.com/bharath12345/playing). 

     
