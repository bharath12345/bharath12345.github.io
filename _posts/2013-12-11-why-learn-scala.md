---
layout: post
title: "Why Learn Scala?"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
---
It was a long time ago when I read this masterpiece by the software engineering guru, Peter Norvig - [Teach Yourself Programming In Ten Years](http://norvig.com/21-days.html#answers). Peter advises wannabe programmers to learn at least half a dozen programming languages. Taking stock of myself earlier this year I realised having terribly missed out. In my decade long career, I had worked deeply in only 4 languages - C++, Java, JavaScript and Perl. And *none* of them strongly functional as Peter advises (functional JavaScript hasn't come to me yet). I then posed two questions to myself - 

* Why do I need another language? 
* If I have to pick one, then, which one?

The answer to the first question came to me rather quickly. At that time I was exploring what was new with JVM-7. And what is expected with Java and JVM-8. JVM-7 with its *invoke dynamic* and Java-8 with *lambdas* were clearly pointing the finger in a certain direction. I realised JVM had started to embrace Polyglot and functional programming. On digging a little deeper, the reasons for this move were easy to realise. Java's issues with type-safety, lack of immutable collections (in the JDK), rampant usage of shared mutability etc., were beginning to weigh heavy. The distributed, multicore, big-data computing, realtime world were making Java a little too verbose, justifying the need to look for alternatives.

Surprisingly, the second question turned out to be the tougher of the two. The choice essentially was between Groovy, Scala and Clojure. I chose Scala. My pre-learning decision has got richly rewarded by what I have learnt after taking the plunge into Scala. Even as I continue to make the (sometimes) steep climb, this is a small, humble attempt to articulate the amazing things I have learnt. This write-up is a little too theoretical. For *show-me-the-code* types, I will soon write about a *not-so-small* 3-tier (DB <=> Biz <=> UI) application I have built entirely with Scala. 

In this post I allude to three broad reasons to *Why Learn Scala* -

1. Scala is a great mix. It imbibes some of the best features of other popular, successful languages
2. Scala ecosystem of frameworks/libraries is big, mature, created by some great people from academia/industry and very well documented cum supported
3. Some features of Scala that have made me a more thoughtful, better programmer

<hr>

### Scala Is A Great Mix 

Scala brings in some of the best features from 4 other programming languages -

1. Haskell
2. Erlang
3. C#
4. Java

Let us take a slightly deeper look...

#### Haskell and Scala
These are two interesting surveys -

* [Learning This Language Improved My Ability As A Programmer](http://hammerprinciple.com/therighttool/statements/learning-this-language-improved-my-ability-as-a-pr)
* [Learning This Language Significantly Changed How I Use Other Languages](http://hammerprinciple.com/therighttool/statements/learning-this-language-significantly-changed-how-i)

Haskell tops both these lists for a reason. Scala incorporates a lot of Haskell's good features into itself. Here is a short list -

1. Type Inference
2. First Class Functions
3. Currying
4. Lazy Evaluation
5. List Comprehensions
6. Immutability
7. Algebraic Data Types
8. Higher Order Types
9. Monads

One question that begs for an answer - If Haskell is so good, then why not use it itself and why go for Scala? If thats an option then I would definitely encourage you to go ahead. But to those like me who just love the JVM and have a overarching need of platform independency, Scala is a welcome choice.

#### Erlang and Scala
[WhatsApp](http://highscalability.com/blog/2013/11/8/stuff-the-internet-says-on-scalability-for-november-8th-2013.html?SSLoginOk=true) gets more messages than Twitter. WhatsApp is built on Erlang. And thats for a reason. To run massively concurrent applications, you need a lot of parallel execution. And Actor based method for concurrency brought in by Erlang is backed by solid academic/research foundations and has also tasted production success. However Erlang takes a thread backed method for its Actor's concurrency. An Erlang process is very lightweight, and Erlang applications commonly have tens-of thousands of threads or more. However thread's are a scarce resource. And in a distributed, horizontally scaling setup the constraints can be quite strict. Scala has two types of Actors: thread-based and event based. Thread based actors execute in heavyweight OS threads. They never block each other, but they don’t scale to more than a few thousand actors per VM. Event-based actors are simple objects. They are very lightweight, and, like Erlang processes, you can spawn millions of them on a modern machine. The difference with Erlang processes is that within each OS thread, event based actors execute sequentially without preemptive scheduling. This makes it possible for an event-based actor to block its OS thread for a long period of time (perhaps indefinitely).

Coming back to a point stated earlier - if you are looking to engineer on the JVM, then Scala's Actor model provides a compelling option for highly scalable and concurrent applications. One can listen to the many talks by the architects Scala Actor model like Jonas Boner and Roland Kuhn to get the idea that its an effort to bring the best of Erlang's proven model to the JVM engineers.

#### C#, Java and Scala
Scala has taken a lot of good things from C# and Java, especially in the syntax area. The syntax seems to have been designed especially keeping the Java programmers in mind, all the while trying to reduce the verbosity. One of the very interesting features that seems to have been inspired by its C# counterpart is [Implicits](http://www.artima.com/pins1ed/implicit-conversions-and-parameters.html). They provide a means to extend libraries, help in type conversion etc. 

<hr>

### Scala Ecosystem
The greatest joy that working with Scala has brought to me is with the library ecosystem. One might be surprised that I say this. There has been quite some furore over backward compatibility of Scala's native libraries over releases 2.7 > 2.8 > 2.9 > 2.10 (present). The Actors model seem to have been written multiple times over - once as native scala.actors, once as part of the Lift library to what one hopes to be the final one - as part of Akka. But I started using Scala after some of these tides have come and gone. Let me first present a list of popular frameworks written and supporting Scala -

Scala natively comes with an excellent collections framework supporting both immutable and mutable collections. Java JDK has no support for immutable collections.

1. **Concurrency, Event Management, ESB**
    a. [Akka](https://github.com/akka/akka)
    b. [Eventsourced](https://github.com/eligosource/eventsourced) - persistence, recovery, redelivery of messages
2. **Data structures**
    a. [Scalaz](https://github.com/scalaz/scalaz) -  Data Structures for functional programming
    b. [RxJava](https://github.com/Netflix/RxJava) - composing asynchronous and event-based programs using observable sequences (not written in Scala but, probably, better used with Scala than Java from code hygiene POV!)
3. **Build and Testing**
    a. [ScalaCheck](https://github.com/rickynils/scalacheck) - testing framework with probably no Java equivalent (at least that I know of)
    b. [SBT](https://github.com/sbt/sbt) - more concise than Maven. No XML crap - build instructions as Scala DSL
4. **Object Relational Mapping** -
    a. [Slick](https://github.com/slick/slick) - Database access
5. **Distributed Big Data Tasks**
    a. [Finagle](https://github.com/twitter/finagle) - Fault tolerant, protocol agnostic RPC system
    b. [Scalding](https://github.com/twitter/scalding) - MapReduce for Scala
    c. [SummingBird](https://github.com/twitter/summingbird) - Streaming, continuous, real-time MapReduce on top of Scalding or Storm
6. **Web Development** (only the more powerful, popular ones)
    a. [Lift](http://liftweb.net/)
    b. [Play!](http://www.playframework.com/) 
    c. [Spray.IO](http://spray.io/)

<hr>

### Unlearning and Relearning Programming
For those coming from Java and no functional programming background Scala can be a steep learning curve. Apart from exposure to many concepts totally new to me, it has helped me a great deal in revisiting some of the most fundamentals I have made about programming. I now have clarity of things I need to *unlearn* to become a better programmer! I thought a passing reader might find this claim interesting. So here is a small list...

1. Immutability: Tradeoffs in using the C/Java style innocuous looking *for* loop; Utility (and at times necessity) of Immutable collections (which do not exist in Oracle's Java JDK)
2. Type safety: Strengths of Java/JVM style strict typing; [Problems](http://code.stephenmorley.org/articles/java-generics-type-erasure/) in Java's type safety offering
3. Inheritance: A better understanding of covariance and contra-variance 
3. Rethinking code verbosity by composing higher order functions, partial functions etc (lesser code after translates to fewer bugs)
4. A better way to alleviate null-checks using Options
5. Dependency Injection without annotations or XMLs
6. It can be better than *static* classes, methods, variables
7. Closures and Mixin's possible on JVM too (Until now, I had thought of these only from the JavaScript angle)
8. Using Map when I needed Tuple was not exactly bright of me
9. I can do so much more when I can write code that my build system understands... looking for Maven plugins need not be a way of life...

... and I can go on and on!! 
