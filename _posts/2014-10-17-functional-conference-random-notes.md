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

The first 'Functional Conference' happened in Bangalore between Oct 9-11. I had been keenly looking forward to it. This is a quick post on the sessions I attended and the conference itself. 

As the lineup of speakers and topics shaped up in the buildup to the conference, it heightened my expectations. As a younger engineer I have gone through the cycle of expecting too much from conferences and thus not being able to learn sufficiently what was on offer. Time has had a mellowing effect... I find it much better to keep an open mind and try to absorb all that is on offer. And then, a little later, retain only thats useful/pertinent. With that mindset and approach I found 'Functional Conference' a useful engineering experience - plenty of technical richness to absorb and sufficient ideas to retain for long.

#### Day 1, Session 1: The Keynote, by Venkat Subramaniam
Venkat is as fabulous a speaker/presenter as he is writer/thinker. The theme of his keynote was an elaboration on the idea of **mainstream**. Why did it take many centuries for heliocentricity to gain acceptance over the *mainstream* idea of geocentricity? Why did it take many centuries for well meaning doctors to accept the existence microbial *germs* as the cause of diseases over other widely held *mainstream* theories? **Mainstream** in the world of programming is OOP in the style of Java and C++. They may not be false idol's after all. However that *non-mainstream* is generally not even introduced in colleges and software engineers have proceeded to long careers without even basic understanding of other programming approaches is sad indeed. Venkat drew the attention of the audience that things were nevertheless changing. Maybe it took a long incubation for the geocentric idea to gain... but once the right ideas, even if *non-mainstream*, gain a foothold, there is no turning back. Maybe functional programming has had a 80 year incubation! After all it took 22 years for even OOPS to become *mainstream*. But things are changing (lambdas in java!) and will never be the same again! 

Two answers by Venkat in the post-session stuck a chord with me. 

* The first was a question on his favourite language... after all he had written books and applications in so many! Venkat responded by saying he treated languages as tools, say like vehicles. we sometime use a car and sometimes a flight, don't we!? So no *favorites*. 
* The second was actually a counter-question by Venkat - Do languages shape new thought or new thoughts shape languages? There is enough material in terms of academic research to tell us that this stream runs both ways! 

#### Day 1, Session 2: Haskell for everyday programmers, by Venkat Subramaniam
I was split between going for the Haskell session or the parallel Elm session. Since my work has been more and more away from UI, I chose Haskell. However, later on, heard great feedback on the Elm session by other folks at the conf. Now waiting for the slides of that session to be up to check it out.

The Haskell session was a runaway hit with Venkat giving a quick intro of the many aspects of the language using the ghci REPL. The key ideas learn/relearnt were:  

* Polymorphic Types
* Functional Purity (no haskell speaker can never not mention this!): functions cannot have side effect. and purity always means thread-safety!
* Memoization: the massive performance gain that could comes ones way due to functional purity
* Order of program evaluation: Normative vs. Applicative
* Expressions vs. Statements: statements promote mutability that one cannot escape. expressions do the opposite

#### Day 1, Session 3: [Functional programming in large scale data processing](https://speakerdeck.com/kishore/applying-functional-programming-principles-to-large-scale-data-processing), by Kishore Nallan
My day job is programming in Scala to build a *large scale data processing* platform. So choosing this session from a fellow traveler was natural. Kishore described the journey at Indix to build a web-scale product catalog by crawling and indexing the internet. The story behind their adoption of the Lambda Architecture. The benefits of using a log-structured database as first port of store than a *continuously mutating* RDBMS or column store. Indix is a huge Hadoop shop with continuous jobs to persist data, aggregate it and run both ritual and ad-hoc queries. It was a fascinating talk giving a peek into what must be a very exciting product to develop.

#### Day 1, Session 4: [Compile your own cloud with MirageOS](http://decks.openmirage.org/functionalconf14#/), by Thomas Gazagnaire
Unikernels are specialized OS kernels that are written in a high-level language and act as individual software components. A full application (or appliance) consists of a set of running unikernels working together as a distributed system. MirageOS is based on the OCaml (http://ocaml.org) language and emits unikernels that run on the Xen hypervisor. Now, whats the main advantage of doing this? Unikernel wins by allowing applications to access hardware resources directly without having to make repeated privilege transitions to move data between user space and kernel space. Unikernels OS are being attempted in more languages than just OCaml. There is HaLVM in Haskell, Ling in Erlang, OSv in Java and maybe more. This introduction to unikernels and perspective on Virtualization was superlative and I wish I could have absorbed more.

#### Day 1, Session 5: [Property based testing for functional domain models](http://www.slideshare.net/debasishg/property-based-testing), by Debasish Ghosh
I have been an avid reader of Debasish Ghosh's blog and books. They are rich both in theoretical argument setting and practical advise. Hence I was looking forward for this session. Am no newbie to ScalaCheck which he was planning to introduce. However, yet again, the theoretical underpinnings for property based testing were a big takeaway. To quote a statements from the session that will stay with me - 

* "To test any sufficiently complex domain model with xUnit based testing will mean some corner cases will be missed". And unit-testing, automated-testing is all about catching those corner cases. 
* "Paramatricity tests more conditions than unit test suites ever will - Edward Knett"

The talk also included a intro to dependenty-types and parametric polymorphism. One key takeaway of listening to new people often is coming to know of new books - and after this session "Theorems for free!" by Phil Wadler got added to my ToRead list!  

#### Straddling sessions - Session 6: Clojurescript & Om, and Code Jugalbandi. Session 7: Functional Groovy, and Learning from Haskell
Eearlier in the day, the chief organiser of the conference, Naresh Jain, had described what was called "law of two feet" - the law basically asks you to get the most out of the conference by walking to the sessions even in-between, if required. Unable to decide which session to stay in for the last two sessions I decided to use this law!

* Om is a library for ClojureScript programmers. Vagmi provided a [breezy intro](http://www.slideshare.net/vagmi/pragmatic-functional-programming-in-the-js-land-with-clojurescript-and-om) to why ClojureScript makes React.js faster. And finally, why and how does Om make ClojureScript faster by giving an example of DOM diffing and the showComponentUpdate() call
* [Code Jugalbandi](http://www.codejugalbandi.org) was a very interesting act between two programmers (Brahma and Krishna) to showcase interesting features like currying and pattern matching. It was a breath of fresh air to the otherwise usual way of sessions in a conference 
* Groovy is a dynamic language on the JVM. Since I have never programmed in Groovy I was pleasantly surprised with its many capabilities in functional programming showcased by Naresha. 
* The Haskell experience session was filled with anecdotes that the speaker, Aditya Godbole, recounted from his workplace (and elsewhere) of trying to bring in healthy-code practice.  

#### Day 2, Session 1: The role of Fear in language adoption, by Bruce Tate
Bruce Tate's book "Seven Languages in Seven Days" was probably the first book I bought on Kindle. I was looking forward to hear from this Guru of Java and Rails. The title added to the curiosity. Bruce kicked off the talk making some very thought provoking observations -

* Fear and *Discovery* are intertwined
* When fear lurks within the team, the commits go down!
* Bruce went on to draw a parallel between Geoff Moore's celebrated 'Technology Adoption Curve' and called for the audience to think of language adoption on similar lines. Languages *die* in the chasm...
* Just as frequency of technology waves frustrates businessmen, the frequency of language waves frustrates programmers (how many new languages did I come across so far in 2014 - Wolfram, Swift, Hack... and I can go on...)
* Just like 'behaviour change' apps have a difficult time in adoption, significant syntax changed languages lose out in the mass programmer market. Java success due to its almost identical syntax to C is NOT incidental...
* And then there are language adoption curves and *language paradigm* adoption curves. The curves for Procedural, OOPS and Functional are much deeper, wider and steeper
* What are the *fears* for different consumers of languages:
	* Paralysing Fear: Jobs, Cost
	* Motivating Fear: Concurrency, Multi-core, Time-to-market
* Now here is a question to all career programmers - how many more years do we want to program in the C/C++ style syntax??   
* The next wave of language adoption will *NOT* be a big massive wave like Java. It will instead be a tsunami of many smaller waves composed of of the Scala's, Clojure's, Ruby's, Swift's and so many more...

#### Day 2, Session 2: Functional programming using Dyalog, by Morten Kromberg
[APL](http://tryapl.org/). I had never heard of it. The name of Ken Iverson sounded familiar and in league with Alonzo Church, Alan Turing, Haskell Curry et al. But nothing more...

And what an eye-opener it was! If there was a award for the most mind-blowing session, then this one won the 1st, 2nd and 3rd places!

The language is beyond words that this humble writer can conjure up. It takes the idea of *functional* programming to an all new level is all I can say (and yet its not logic programming like Prolog or likes).

However the story of Dyalog as a company and its business came across as not any less astonishing. To be in *software development* business for over 40 years, going through the many industry upheavals (mainframes -> unix/windows -> cloud) and solving some of the most difficult problems in all streams of engineering and yet remain totally unknown to most! Morten Kromberg, the CTO of Dyalog, had a interesting observation to share - "All engineers take to APL easily except the software engineers". That says it all about our education system. 

#### Day 2, Session 3: [Monads you already use](https://speakerdeck.com/gja/lightning-monads-you-already-use-without-knowing-it), by Tejas Dinkar
Next was a lightening talk by Tejas on giving a (yet another!) perspective on Monads. In a delightfully constructed talk Tejas presented the idea through a box analogy and thereby trying to simplify the understanding of monads for list, IO etc. There would not be a functional programmer on the planet who has not heard/read at least one video/blog on Monads without scratching his head in disbelief. It takes a certain bravado to attempt presenting the topic to a roomful of programmers at the *functional* conference! And Tejas did a splendid job of it.  

#### Day 2, Session 4: [Purely functional data structures demystified](http://www.slideshare.net/mohitthatte/purely-functional-data-structures-demystified), by Mohit Thatte
Mohit's talk was based on Chris Okasaki's famed work on the topic "[Purely Functional Data Structures](http://www.cs.cmu.edu/~rwh/theses/okasaki.pdf)". This is a deep topic. I have tried to read Okasaki's work and have found it hard to get past the first few chapters. Its in the same league as SICP. I was curious about how justice for such a voluminous work can be done in one session! The first challenge is to try and formulate the problem definition - Mohit kept the audience glued as he demystified why it is tough to implement a *correct*, *fully functional* and *performant* implementation of common ADT's like Queue, List, Map etc. The next challenge was to explain the complex idea of **structural sharing**. The whole idea of *persistence* in data structures and *performance* is after all derived from *structural sharing*. One has to really try and attempt implementing common data-structures with *structural-sharing* to start comprehending the complexity that it introduces and the power behind the idea. That it becomes extremely complex to come up with even different list implementations when *no side effects* barrier is introduced is also an idea that needs real hands on work to grasp. Mohit's session was a fine effort to jog my memories of my few late night battle-losses with Okasaki and the illuminating world of *persistent* data-structures!

#### Day 2, Session 5: Demystify functional jargons, by Mushtaq Ahmed
Scala has multiple library API that are very well suited for certain usecases. In this talk Mushtaq covered, with examples, the when-to, why-to and how-to use the [Async](https://github.com/scala/async), [Await](http://www.scala-lang.org/files/archive/nightly/docs/library/index.html#scala.concurrent.Await$), [Blocking/Future/Promise](http://docs.scala-lang.org/overviews/core/futures.html). In addition to these *in-house* Scala utilities he also demonstrated the usecase for [Observables](https://github.com/ReactiveX/RxJava/wiki/Observable) in the context of streams. He demonstrated an example of a simple application built using these to capture, filter and search on tweets.   

#### Day 2, Session 6: Object-functional programming: Beautiful unification or kitchen sink, by Rahul Goma Phulore
This was a talk I was eagerly looking forward to. The reason was very specific - a couple of close friends and former colleagues engaged me in long winding discussions on building *large* applications in Scala. Like all languages Scala has its pro's and con's. However opinions stand divided by a wide(ening?) chasm...

I was looking forward to Rahul to give me some new perspectives. In a thoroughly technically-engaging talk Rahul deconstructed the myth of Scala being a kitchen-sink. The very startup to the talk was made super intriguing when he proceeded to ask the audience 3 questions - (a) how many see the future in a purely OOPS world? (b) how many see the future in a purely functional world? (c) how many see the future in a hybrid of both?. Almost no hands went up for question (a). A few enthusiastic hands went up for question (b). But almost **ALL** hands went up for question (c). That was significant food for thought in itself. 

Scala has been called the "Grand unification of all programming languages". It has also been called "Vegetarian ham in chicken flavor"... arguments like these have split the programming world into tribes of believers/unbelievers without significantly adding to the knowledge/understanding of either groups. Coming from a workplace where we use Scala predominantly I can testify this to true by experience.

But it pays great dividends to dive-in a little deep to understand just *how* Scala provides this *grand-unification*. Now thats where real illumination is. How can functions be first-class objects? How does pattern-maching happened under the hood? The idea behind algebraic data types? How can using the mere term *sealed* lead to exhaustiveness checking and much higher type checking kick-in at compile-time? How do mixins works? 

#### Day 2, Session 7: Methodologies, Mathematics, and the Metalinguistic Implications of Swift, by Daniel Steinberg
