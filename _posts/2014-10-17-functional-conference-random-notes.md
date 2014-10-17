---
layout: post
title: "Functional Conference: Random Notes..."
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

The first 'Functional Conference' happened in Bangalore between Oct 9-11. I had been keenly looking forward to it. As the lineup of speakers and topics shaped up in the buildup to the conference, it heightened my expectations. As a younger engineer I have gone through the cycle of expecting too much from conferences and thus not being able to learn sufficiently what was on offer. Time has had a mellowing effect... I find it much better to keep an open mind and try to absorb all that is on offer. And then, a little later, retain only thats useful/pertinent. With that mindset and approach I found 'Functional Conference' a useful engineering experience - plenty of technically richness to absorb and sufficient ideas to retain for long.

With two parallel tracks happening in the conferences listeners had to choose one. I came up with my own shortlist and this is a blog on the sessions I attended. 

### Session 1: The Keynote, by Venkat Subramaniam

Venkat is as fabulous a speaker/presenter as he is writer/thinker. The theme of his keynote was an elaboration on the idea of **mainstream**. Why did it take many centuries for heliocentricity to gain acceptance over the *mainstream* idea of geocentricity? Why did it take many centuries for well meaning doctors to accept the existence microbial *germs* as the cause of diseases over widely held *mainstream* theories? **Mainstream** in the world of programming is OOP with Java and C++. They are not necessarily as false idol's as the other examples. However that *non-mainstream* is generally not even introduced in colleges and software engineers have proceeded to long careers without even basic understanding of other approaches is sad indeed. Venkat drew the attention of the audience that things were nevertheless changing. Maybe it took a long incubation for the geocentric idea to gain... but once the right ideas even if *non-mainstream* gain a foothold, there is no turning back. Maybe functional programming has had a 80 year incubation. But things are changing (lambs in java!) and will never be the same again!

### Session 2: Haskell for everyday programmers, by Venkat Subramaniam

I will split between going for the Haskell session or the parallel Elm session. Since my work has been more and more away from UI I chose Haskell. However heard great feedback of the Elm session by many folks. Now waiting for the slides of that session to be up to check it out.

The Haskell session was a runaway hit with Venkat giving a quick intro of the many aspects of the language using the ghci REPL. The key ideas learn/relearnt were of:  

* polymorphic type
* purity: functions cannot have side effect
* memoization: the massive performance gain that may comes one way due to functional purity
* order of program evaluation: normative vs. applicative

### Session 3: Functional programming in large scale data processing, by Kishore Nallan

My day job is programming in Scala to build a *large scale data processing* platform. So choosing this session from a fellow traveler was natural. Kishore described the journey at Indix to build a web-scale product catalog by crawling and indexing the internet. The story behind their adoption of the Lambda Architecture. The benefits of using a log-structured database as first port of store than a *continuously mutating* RDBMS or column store. Indix is a huge Hadoop shop with continuous jobs to persist data, aggregate it and run both ritual and ad-hoc queries. It was a fascinating talk giving a peek into what must be a very exciting product to develop.


 

 