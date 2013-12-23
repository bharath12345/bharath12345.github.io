---
layout: post
title: "Open Source DB For Enterprise Apps"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
subheading: true
subhead: PostgreSQL vs MySql. PostgreSQL Wins Hands-Down!
---
I started on this post some 6 months ago. Over that period, as I slowly worked on and studied multiple database systems the ideas and data on each has swelled. But this is a quick post focusing on just one topic - comparing the two giants of open-source SQL databases - Postgres and MySql. 

One amazing line that keeps coming up reading these many articles - *"Unfortunately, MySQL had already been chosen by the time I got involved"*

When I told a colleague of writing this article he smiled and asked a polite, *Why?* The web is filled with such articles. Many of whom written by professional database admins and academics. I have read many of these articles in the last 6 months. Yet, I have not come across an article from a *enterprise application programmer* point-of-view. I have wondered why this could be so. I think there are two reasons why there are not many programmers dissecting this -

1. *Developers* find it difficult to talk on this topic in which the *Operations* folk have strong opinions. And somehow (keeping the current DevOps ideology aside) the decision of picking the database system has been the prerogative of the *Operations* folk than the *Developer* folk
2. From a developer perspective, the PostgreSQL vs. MySql debate is a non-starter. PostgreSQL wins in round-one and by such a huge margin that any talk to the contrary is just bizarre to a *programmers ears* (you will know why so by the end of this post)

(Another small hassle with the many articles on the web is that very few of them are recent from circa 2013 perspective... a comparison of these two database systems as they stand towards the end of 2013 is what I hope to write about)  

But before I begin to delve deeper into the comparison I need to set the application context. After all every comparison should be in a specific context. the definition of the context in which I compare are as follows -

1. Enterprise Applications. By this, I mean the application has more moving parts than a typical web-stack. The number of tables could stretch into hundreds. Data is collected from myriad sources in real-time (discovery, polling etc)
2. Read-write ratio varies vastly across tables. Database needs to support 90% (and upwards) read-only tables and also tables with much higher write than read, say 60% (and upwards)
3. Many thousand transactions per second
4. Hundreds of stored procedures
5. Automating migrations, upgrades and sharding

On a topic like this its probably a good idea to get started by stating some of the good references that I have found in the wild-wild web (filled with SEO articles on the topic written by training institutes and outsourced IT operations companies)

1. [MySql vs. PostgreSQL](http://www.wikivs.com/wiki/MySQL_vs_PostgreSQL) - recent and continuously updated. Readers would do well to read the articles in the links section (on last read, I did not find a single article talking glowingly about MySql in comparison to PostgreSQL) 
2. [PostgreSQL vs MySQL: Which is better?](http://www.databasejournal.com/features/postgresql/article.php/3288951/PostgreSQL-vs-MySQL-Which-is-better.htm) - This article is 10 years old. Still a good read
3. [MySql Gotchas](http://sql-info.de/mysql/gotchas.html) and [PostgreSQL Gotchas](http://sql-info.de/postgresql/postgres-gotchas.html). Just stare at these two lists for some time even if you don't read them. They tell a story 

I plan and hope not to repeat anything that is already said in these articles. Agreeing with the writers of these articles, let me also say that I am done with seeing performance benchmark articles on database systems.

I also want to steer clear on the *[political](http://www.muktware.com/2013/05/there-is-no-reason-at-all-to-use-mysql-mariadb-mysql-founder-michael-widenius/4298)* aspects of this comparison. MySql has been acquired by Oracle. One can find all sorts of speculation about MySql future roadmap due to this (the birth of MariaDB et al). 

#### The 'Null' Problem

#### Object Relational DB

#### Choice Of Data Types

#### Performance

##### Partitioning Problems
##### MVCC

#### Philosophical difference that influences technology
MySql is a product sold multiple times over. Large scale code corrections are tough and few - thats why the its v5. Thats why a different engine for storage and SQL... promote business model etc

PostgreSQL is a project. The folks behind PostgreSQL are driven to bring the progress in database technology to the fingertips of developers and admins. Thats why PostgreSQL has made larger course corrections in its evolutions lending to a bigger number v9. Thats why you will find MySql always playing catch-up with PostgreSQL on features and even performance (which was supposed to be MySql forte years ago!)

#### Concerns with PostgreSQL
##### Vacuuming
##### Case insensitive search strings
##### Syntax War Games


