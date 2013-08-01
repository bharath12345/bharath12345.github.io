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

1. Poll: Ajax requires a client side request to get data. So the simplest solution is to buld a client side timer based poller. Maybe use JavaScripts timers like setInterval or setTimeout (or wrapper from libraries). 
	* Pro: Simple
	* Con: If the data being polled is increasing, continuous degradation in performance is natural as more data is fetched and rendered every time. If the 'real-time' SLAs call for changes to be shown quickly (within 5 seconds of happening or so), then continous polling on the client starts to weigh heavy on the data source. It could lead to continously running large number of SQLs
2. Server side stateful:  
	* Pro:
	* Con: 
3. Client side stateful:
	* Pro:
	* Con: 
4. COMET
	* Pro:
	* Con: 
5. WebSocket
	* Pro:
	* Con: 


