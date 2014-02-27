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
       ![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-05-58.png =430x238)
  * Details: 
  
* ##### 30 Seconds Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/1](http://bharathplays.herokuapp.com/twitter/elections/1)
  * Dashboard Sample Image:   
       ![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-06-30.png =430x238)
  * Details: 
  
* ##### 5 Minutes Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/2](http://bharathplays.herokuapp.com/twitter/elections/2)
  * Dashboard Sample Image:   
       ![image](http://bharathwrites.in/images/twitterdashboard/my%20twitter%20dashboard%202014-02-27%2019-27-42.png =430x238)
  * Details: 
  
* ##### 30 Minutes Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/3](http://bharathplays.herokuapp.com/twitter/elections/3)
  * Dashboard Sample Image:
  * Details: 
  
* ##### 3 Hours Tweet Aggregate Grapher
  * URL: [http://bharathplays.herokuapp.com/twitter/elections/4](http://bharathplays.herokuapp.com/twitter/elections/4)
  * Dashboard Sample Image:
  * Details: 

#### Caveats of Twitter Stream Processing

### Design and Code
The code is on github [here](https://github.com/bharath12345/playing). 

     
### WebSocket Addendum

* May not work if you are a behind a proxy which does not tunnel WebSockets
* May not work if your firewall blocks WebSockets
* If you run into any of the above issues, then you could use your mobile device to see the dashboard. Here is the screenshot from my Android Samsung S2 on my home Wifi. However I have checked to see that it works on my Airtel 2G network fairly well too. The dots in the image are some mess-up by the mobile screenshot tool...

![image](http://bharathwrites.in/images/twitterdashboard/2014_02_27_19.51.35.png =220x200)

### Final Note
These graphs are just volumetric. I plan do some simple sentiment analysis next. However, by looking at the graphs and tweets behind them, it is heartening to see the order of popularity of each string. *India* is most popular among the four but next comes *Modi* and it is generally not very far behind. *Rahul* seems to appear more than *Kejri* but both these strings trail a long way behind *Modi*. With me being a diehard Sri Narendra Modi supporter, these graphs and numbers certainly make me happy and hopefully bode for good times to come for my country :-) 
