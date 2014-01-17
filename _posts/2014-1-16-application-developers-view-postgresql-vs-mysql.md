---
layout: post
title: "Application Developers View: PostgreSQL vs. MySQL"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
subheading: true
subhead:
---
I reluctantly started to write this post some 6 months ago. As a application developer my knowledge of the internals of DBMS design was (and still is) very limited. But its one thing to work with a DBMS at development time and quite another to keep it running at operations. So the motivation here is to share a few specific ideas with fellow application developers. My attempt here is to do a value judgement of the two systems from a development standpoint and steer as much clear as possible from a value judgement in the *deployed* scenario. After all DBMS systems are probably at the heart of more Aps vs. Ops debates than anything else. So to say it simply (at the cost of barbs from some of my good friends who I know to be excellent operations engineers for MySQL) - PostgreSQL leads MySQL. And by some distance.   

But apart from reading about the internals and playing with both systems I felt a need speak to whomever I could in the developer community to ask for the reasons behind the choice of DBMS in their projects. In the last 6 months I could speak to just about eight such people in different projects. Almost all from medium to small companies doing web applications (but some of these applications projects were themselves quite large). Speaking to these people there is one curious thing that I cannot but share - the answer from all who had chosen MySQL was - *"Unfortunately, MySQL had already been chosen by the time I got involved"*. Of the eight, six had been running projects for 2-3 years and of which three had chosen MySql. Rest had all opted for PostgreSQL.

When I told a colleague of writing this article he smiled and asked a polite, *Why?* After all, the web is filled with such articles. Mostly written by expert database admins. There are fewer articles from *application programmer* point-of-view. I can think of two reasons why there are not many programmers dissecting this -

1. *Developers* find it difficult to talk on this topic in which the *Operations* folk have strong opinions. In many projects of the DevOps kind the decision to pick the database is the prerogative of the *Operations* folk than the *Developer* folk
2. From a developer perspective, the PostgreSQL vs. MySql debate is a non-starter. PostgreSQL wins. And wins quite early (you will know the *why* by the end of this post)  

But before delving deeper into the comparison its good to set the application context -

1. Enterprise Applications. By this, I mean the application has more moving parts than a typical web-stack. The number of tables could stretch into hundreds. Data is collected from myriad sources in real-time (discovery, polling etc)
2. Read-write ratio varies vastly across tables. Database needs to support 90% (and upwards) read-only tables and also tables with much higher write than read, say 60% (and upwards)
3. Many thousand transactions per second
4. Hundreds of stored procedures
5. Automating migrations, upgrades and sharding

Its probably a good idea to start by pointing to some of the good references from the wild web -

1. [MySql vs. PostgreSQL](http://www.wikivs.com/wiki/MySQL_vs_PostgreSQL) - recent and continuously updated. Readers would do well to read the articles in the links section (on last read, I did not find a single article talking glowingly about MySql in comparison to PostgreSQL) 
2. Couple of very good articles comparing these two by Robert Haas
   * [Table Organization](http://rhaas.blogspot.in/2010/11/mysql-vs-postgresql-part-1-table.html)
   * [Vacuum vs. Purge](http://rhaas.blogspot.in/2011/02/mysql-vs-postgresql-part-2-vacuum-vs.html)
3. [PostgreSQL vs MySQL: Which is better?](http://www.databasejournal.com/features/postgresql/article.php/3288951/PostgreSQL-vs-MySQL-Which-is-better.htm) - This article is 10 years old. Still a good read
4. [MySql Gotchas](http://sql-info.de/mysql/gotchas.html) and [PostgreSQL Gotchas](http://sql-info.de/postgresql/postgres-gotchas.html). Just stare at these two lists for some time even if you don't read them. They tell a story
5. [Comparing Reliability and Speed](http://wiki.postgresql.org/wiki/Why_PostgreSQL_Instead_of_MySQL:_Comparing_Reliability_and_Speed_in_2007)
6. [A Comparison of Enterprise Suitability - PostgreSQL is Suited Better](http://www.slideshare.net/techdude/postgres-vs-mysql-presentation) - though MyISAM focused, this comparison is with enterprise products in purview and is 5 years old (2008). Since then, the gap between PostgreSQL and MySql have only widened in favour of PostgreSQL despite InnoDB

I plan and hope not to repeat anything that is already said in these articles. Agreeing with the many writers of these articles, I don't see any point doing performance benchmark comparisons between these two database systems. Also want to steer clear of the *[political](http://www.muktware.com/2013/05/there-is-no-reason-at-all-to-use-mysql-mariadb-mysql-founder-michael-widenius/4298)* aspects of this comparison. MySql has been acquired by Oracle. One can find all sorts of speculation about MySql future roadmap due to this (the birth of MariaDB et al). 

Now moving on to the specifics...

#### The 'Null' Problem
The biggest accusation one can make against any database system is that it is not careful with data integrity. MySql is notorious for its inability to handle Null with many data types. Effort to accommodate query mistakes ruins MySql. For example - 

* MySql will insert empty strings for text fields that have not-null constraint. This happens if you forgot to mention a field during the insert or if you somehow ended up inserting a blank value ('') for a field. It goes ahead with the insert in both these cases - irrespective of weather we use ORM or direct JDBC or some other kind of wrappers, there simply is no way to gracefully handle this kind of thing PostgreSQL won't do such a thing
* Non-null timestamps end up getting all zero value dates. If you push a NULL as date, it defaults to current time!
* With decimal numbers, if you are not careful with precision and scale, then, on inserts MySql will *change the data* to fit the column constraints. Of course its necessary to be careful when playing with data but the problem here is a change in precision (column constraint) should in no way change the data as MySql does. This kind of problem is just plain horror. Just refer to the MySql gotchas site to get a clear understanding of this problem. Postgres does not alter data no matter what
* While writing functions, MySql does not throw graceful exceptions for divide by zero. It just returns a plain NULL all the time!
* In MySql set a text field length to *X* and insert a string which is *2X* in length... MySql will just promptly truncate the extra *X*. Holy cow! The length X was a *constraint*. On trying to insert longer length strings, we expect MySql to throw errors... not play with our data...
* MySql has no idea about dates. Try inserting 31st Feb and it will promptly comply inserting shit
* MySql will allow inserting of strings to decimal columns, sometime storing it as 0 and sometimes as NULL

This problem is not isolated. MySql takes liberties to not abide by user supplied constraints many time in many ways

#### Object Relational Database System!
Concepts unique to PostgreSQL which lends well with enterprise 
* Logical Partitioning
* Windowing Functions
* Table Inheritance

**Object oriented tables**

    CREATE TABLE shape ( name varchar(50) );

    CREATE TABLE square    (edge int)     INHERITS (shape);
    CREATE TABLE circle    (radius int)   INHERITS (shape);
    CREATE TABLE rectangle (w int, h int) INHERITS (shape);

    INSERT into shape     (name)         VALUES ('random')
    INSERT into square    (name, edge)   VALUES ('square', 10);
    INSERT into circle    (name, radius) VALUES ('circle', 10);
    INSERT into rectangle (name, w, h)   VALUES ('rectangle', 5, 10);

    Running the above SQL statements, will result in following status in different tables -
    
    * shape - 4 records
    * square, circle, rectangle tables - 1 record each!
    
Like 'INHERITS' there is a 'NO INHERITS' also to mix different table just precisely. And Postgres uses partitioning under the covers to enable inheritance. So, not only does inheritance give the programmer flexibility in data modelling lending to lesser duplication, it also helps improve performance! Afterll without inheritance, the engineers will be forced to do multiple table joins and filters (many times going up to boolean value *marker* columns) - which sounds over-engineering for a OOP developer standpoint. Thinking about it, the non-object oriented SQL design adds to overhead to SQL optimiser, makes indexing overhead higher and so many more such misses.

 
    


#### Choice Of Data Types
* All strings are default UTF-8 encoded
* A massive choice of data types to choose from for dates
* IPv4, IPv6, MAC, Inet address data types
* Arrays, JSON, UUID, XML. Search within Arrays using indexes, where clauses
* Serial and other sequences - leads to very fast ID key finding and incrementing
* Rounding errors can be eliminated to a much larger extent with the huge bouquet of floating point data-types 
* Infinity, -Infinity, NaN as values for numeric data types - in MySql you will have no way of doing these. You will have to insert a number or Null and thats all
* Money type
* ORM tools often convert 'String' datatype to nvarchar(max) which kills performance on MySql. Inserting multibyte characters (say japanese) into varchar fields complete corrupts the data (no database exception thrown!). Sometimes it is not sufficient to just change the column type to nvarchar when trying to store multibyte characters. Even the insert statements need a prefix (application level code change if you are using JDBC). PostgreSQL uses default UTF8 encoding. There is no varchar/nvarchar problems. Everything simply works!
* Adding constraints to complex types likes dates is made extremely simple with embedded functions. No such thing possible in MySql. Special keywords like 'today', 'tomorrow', 'yesterday', 'allballs'
*  


Why are data-types important? Why store less? When performance becomes key and probable bottleneck, to squeeze out the max performance requires optimised storage... because finally, things in your DB schema are going to end up in RAM caches and larger datatypes will mean more space being taken up on the RAM. Less conservatively used RAM cache will bring down the performance of your application more than anything else


#### Free Features
* Automatic Data Compress by Default
* Logical Partitioning
* Unlimited File Size
* Index even functions (no other DB can do!)
* 

#### Performance
Comparing performance of PostgreSQL and MySql (InnoDB) is a loaded question. The references I have spelt out earlier have links to many scholarly articles that articulate the subtle differences in the MVCC implementation of both. Both provide row locking, Page locking, along with read/write lock separation. After digging into the details picking a one of these two on the basis of *performance* again comes back to the nature of the application that is being built. Designers should pay attention to three critical questions and answer them sufficiently before making a choice -

* Read/Write characteristics of the application
* Concurrent access characteristics of various tables
* Cost of dirty reads, non-repeatable reads, phantom reads etc

These are not easy questions to answer. But, personally, after much pondering, estimation and simple math, I don't see any reason to pick to MySql ahead of PostgreSQL ever on the basis of performance. Ever. The performance area is complex enough and if concurrent writes are on the extreme for a particular application then moving away totally from SQL to NoSQL is a better option than trying to split hairs over RDBMS engines. A move to NoSQL will bring massive freedom to design around these problems along with massive responsibility to handle things correctly. So to round it off, if you are choosing MySql over PostgreSQL due to some (misplaced) notions of higher performance without concrete answers to the above posers, then, in all probability you are thinking wrong.

##### Partitioning Problems
##### MVCC

#### Philosophical difference that influences technology
MySql is a product sold multiple times over. Large scale code corrections are tough and few - thats why the its v5. Thats why a different engine for storage and SQL... promote business model etc

PostgreSQL is a project. The folks behind PostgreSQL are driven to bring the progress in database technology to the fingertips of developers and admins. Thats why PostgreSQL has made larger course corrections in its evolutions lending to a bigger number v9. Thats why you will find MySql always playing catch-up with PostgreSQL on features and even performance (which was supposed to be MySql forte years ago!)

#### Concerns with PostgreSQL
##### Vacuuming
##### Case insensitive search strings
##### Syntax War Games

#### Epilogue
I have a hypothesis. MySql is more popular in applications developed using Ruby, PHP, Perl or Python. Just like Microsoft's SQL-Server is the default database if you are a C# application. This is so because of the community and peer group effect. And also because there are many tools and expertise within the ecosystem if you choose a popular stack. But the most popular language to develop *enterprise* applications is Java. And I personally get more fond of Scala by every passing day. So the hypothesis is, for JVM developers MySql does not lend well *just* because of the community/peer-group effect. So the choice needs to be based more on technological pro's and con's.



