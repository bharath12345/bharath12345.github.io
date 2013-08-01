---
layout: post
title: "Real Time Dashboard with Camel, ActiveMQ, Dojo on JBoss using JMS & WebSocket"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

I have built real-time 'stock-ticker' like dashboards. There are many ways one can build them -

##### Poll
Ajax requires a client side request to get data. So the simplest solution is to buld a client side timer based poller. Maybe use JavaScript timers like setInterval or setTimeout (or wrappers from libraries). 
###### Pro
Simple
###### Con
If the data being polled is increasing, continuous degradation in performance is natural as more data is fetched and rendered every time. If the 'real-time' SLAs call for changes to be shown quickly (within 5 seconds of happening or so), then continous polling on the client starts to weigh heavy on the data source. It could lead to continously running large number of SQLs

##### Stateful
Maintain 'states' between requests. Either, the client asks for only the incremental (what I like to call client-side stateful). Or the server responds with only the incremental when a request from the same client arrives (server-side stateful). On the server-side one can use RESTful API's to publish incremental data of different types. However a session handshake or client-subscription is required before the start (think of server maintaining state for each client by an ID). Otherwise a timestamp based method could be adopted by the client to get the incrementals. RESTful APIs are a deep field and there are a plethora of good, bad and horrible libraries/designs. Coming the the client-side state maintenance for real-time, there are some wonderful JavaScript frameworks that make this possible. For example one might use [BackboneJS](http://backbonejs.org) or Dojo's "[Observable](http://dojotoolkit.org/reference-guide/1.9/dojo/store/Observable.html)" pattern to build a store in the browser and update the UI only on the incremental changes.
###### Pro
Since only the incremental 'delta' is what in transit and changed on the UI, these methods scale in performance. They are well suited for web applications where 3rd party developers could be using your data feed to build UIs.   
###### Con
Maintaining state can quickly become very complex. Multiple types of data, with different incrementals can lead to 'cache-mess'. Many caches and really big caches. User actions like filtering add considerable complexity to the underlying infra. And despite only incrementals being in transit, it is still a request-response system, making tight SLA's (<5 seconds refresh rate) quite a challenge. 

##### COMET
###### Pro
###### Con

###### WebSocket
###### Pro
###### Con
