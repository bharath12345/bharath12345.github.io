---
layout: post
title: "Threads - Book by Brian Goetz and Doug Lea"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
toc: true
---

1. If multiple threads access the same mutable state variable without appropriate synchronization, your program is broken. There are three ways to fix it: 
	* Make the state variable immutable; or 

	
	A  class is threadsafe if it behaves correctly when accessed from multiple threads, regardless of the scheduling or interleaving of the execution of those threads by the runtime environment, and with no additional synchronization or other coordination on the part of the calling code.
	
3. Where practical, use existing threadsafe objects, like AtomicLong, to manage your class's state. It is simpler to reason  about the possible states and state transitions for existing threadsafe objects than it is for arbitrary state variables, and  this makes it easier to maintain and verify thread safety.

4. To preserve state consistency, update related state variables in a single atomic operation. 

5. ￼Stateless and immutable objects are always thread safe. 







	When an object creates a thread from its constructor, it almost always shares its this reference with the new thread,  either explicitly (by passing it to the constructor) or implicitly (because the Thread or Runnable is an inner class of the  owning  object).  The  new  thread  might  then  be  able  to  see  the  owning  object  before  it  is  fully  constructed.  There's  nothing wrong with creating a thread in a constructor, but it is best not to start the thread immediately. Instead, expose  a  start  or  initialize  method  that  starts  the  owned  thread.
	
13. What is ThreadLocal?

	A more formal means of maintaining thread confinement is ThreadLocal, which allows you to associate a per thread  value with a value holding object. Thread-Local provides get and set accessor methods that maintain a separate copy  of  the  value  for  each  thread  that  uses  it,  so  a  get  returns  the  most  recent  value  passed  to  set  from  the  currently  executing thread. 
14. 