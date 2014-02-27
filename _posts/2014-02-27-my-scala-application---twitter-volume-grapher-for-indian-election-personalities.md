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
  * Dashboard Sample Image:   
       <a href="http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-05-58.png">![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-05-58.png =430x238)</a>
  * Details: 
    * In this graph, a new data-point get created every 3-seconds. It appears as a dot on the chart. A mouse over of the dot shows the exact time and value of the data-point
    * The title of the four grid's shows the string the graph is for. For example, the title of the graph showing the line chart for string *rahul* has the title **Twitter Trends Graph for rahul**
    * x-axis is time. y-axis is number-of-tweets
  
* ##### 30 Seconds Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/1](http://bharathplays.herokuapp.com/twitter/elections/1)
  * Dashboard Sample Image:   
       <a href="http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-06-30.png">![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-06-30.png =430x238)</a>
  * Details: 
    * In this graph a new data-point gets created on the chart every 30 seconds
    * Refer to the details of 3-seconds chart (above) for other info
  
* ##### 5 Minutes Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/2](http://bharathplays.herokuapp.com/twitter/elections/2)
  * Dashboard Sample Image:   
       <a href="http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-27-42.png">![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-27-42.png =430x238)</a>
  * Details: 
    * In this graph a new data-point gets created on the chart every 5 minutes (300 seconds)
    * Refer to the details of 3-seconds chart (first one above) for other info
  
* ##### 30 Minutes Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/3](http://bharathplays.herokuapp.com/twitter/elections/3)
  * Dashboard Sample Image:
  * Details: 
    * In this graph a new data-point gets created on the chart every 30 minutes (1800 seconds)
    * Refer to the details of 3-seconds chart (first one above) for other info
  
* ##### 3 Hours Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/4](http://bharathplays.herokuapp.com/twitter/elections/4)
  * Dashboard Sample Image:
  * Details: 
    * In this graph a new data-point gets created on the chart every 3 hours (10800 seconds)
    * Refer to the details of 3-seconds chart (first one above) for other info

### Design, Code and Logic
The gist - 

* The code is on GitHub [here](https://github.com/bharath12345/playing)
* It uses [Play! Framework's](http://www.playframework.com/) capabilities for all UI work which includes templates, URL-routing and WebSockets communication
* To bind to Twitter's stream firehose it uses [Spray.IO](http://spray.io/)
* All the code is in Scala. It does *not* use threads and uses the actor-method of concurrency using [Akka](http://akka.io/)
* Play's capability to do [async](http://www.playframework.com/documentation/2.2.x/api/scala/index.html#play.api.mvc.WebSocket$) websocket concurrent [broadcast](http://www.playframework.com/documentation/2.2.x/api/scala/index.html#play.api.libs.iteratee.Concurrent$) is leveraged
* It connects to [filter](https://dev.twitter.com/docs/api/1.1/post/statuses/filter) API among the many Twitter's streaming APIs
* The part of code which connects to Twitter's streaming APIs and retrieves individual tweets is an extension of [this](http://www.cakesolutions.net/teamblogs/2013/12/08/streaming-twitter-api-in-akka-and-spray/) example by [Jan Machacek](https://twitter.com/honzam399)
* This is NOT a sentiment analysis but a brute-force volume graphing. So a higher count for a candidate does not imply positive popularity but just that his name is trending more. 
* The keyword strings used, for example *Rahul* might appear anywhere in the tweet. That is it could be anywhere in the text, may be part of hashtag or may even be part of a user handle that appears in the tweet
* While trying to find a match, I convert the whole tweet to lowercase and then use Java's String *contains()* to find a match. So the matching is case insensitive - the count for string *Rahul* includes those for *rahul*, *raHul*, *rahuL* etc. The matching string could also be a substring. So *modi* will match *modified*, *moditva*, *amodi*, etc.
* The design flow essence is captured in this image - 

    <a href="http://bharathwrites.in/images/twitterdashboard/algo.png">![image](http://bharathwrites.in/images/twitterdashboard/algo.png)</a>


### WebSocket Addendum
The graph may not appear if you are a behind a proxy which does not tunnel WebSockets (if you are working within in office network). Also if a firewall blocks WebSockets. But in case you run into any of the above issues, then you could use your **mobile device** to see the dashboard. Here is the screenshot from my Android Samsung S2 on my home Wifi. However I have checked to see that it works on my Airtel 2G network fairly well too. The dots in the image are some mess-up by the mobile screenshot tool...

   <a href="http://bharathwrites.in/images/twitterdashboard/2014_02_27_19.51.35.png">![image](http://bharathwrites.in/images/twitterdashboard/2014_02_27_19.51.35.png =220x200)</a>

### Final Note
These graphs are just volumetric. I plan do some simple sentiment analysis next. However, by looking at the graphs and tweets behind them, it is heartening to see the order of popularity of each string. *India* is most popular among the four but next comes *Modi* and it is generally not very far behind. *Rahul* seems to appear more than *Kejri* but both these strings trail a long way behind *Modi*. With me being a diehard Sri Narendra Modi supporter, these graphs and numbers certainly make me happy and hopefully bode for good times to come for my country :-) 
