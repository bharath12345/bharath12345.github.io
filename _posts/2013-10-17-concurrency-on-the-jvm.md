---
layout: post
title: "Concurrency on the JVM"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

*ToDo: Time taken's should be average of at least 30 runs*

1. **Sequential, Network IO Intensive Application**
	
	* Filename: SequentialNAV
	* Time Taken: 20-23 seconds
	* Task: For a given set of 40 stock symbols along with the quantity of stocks held, gets the stock price from Yahoo! Finance and computes the Net Asset Value (NAV)
	
2. **Concurrent, Network IO Intensive Application**

	* Filename: ConcurrentNAV
	* Time Taken: < 1 second
	* Task: Computes the NAV by requesting the stock quotes in parallel. Uses Java ExecutorService with a pool size of 40 on my 4 CPU system (pool size computed using the formula discussed in the book)
	 
3. **Sequential, Compute Intensive Application**

	* Filename: SequentialPrimeFinder
	* Time Taken: 6-7 seconds
	* Task: Finds prime numbers in a given range. I set the range as 1 to 9,000,000 (9 Million)

4. **Concurrent, Compute Intensive Application**

	* Filename: ConcurrentPrimeFinder
	* Time Taken: 1.5 to 3 seconds
	* Task: Break the range into configurable number of parts where each part has a upper and lower bound. Run all the parts concurrently using ExecutorService where the pool size is configurable. I set the number of parts and pool size both to be 100. So the range 1 to 9-Million would be broken into 100 parts like [{1 to 90000}, {90001 to 180000} and so on]. Each part is run on a separate thread of the ExecutorService pool. This method is inefficient because the smaller ranges get computed faster than the ranges with bigger numbers… one can fine tune the algorithm to further better the performance
	
5. **Sequential, Disk IO Intensive Application**

	* Filename: TotalFileSizeSequential
	* Time Taken: Around 120 seconds
	* Task: Computes the aggregate file size of all files in a directory. On my MacBookPro, I ran it on my collection of books! (books with accompanying source code in many cases)
	
6. **Concurrent, Disk IO Intensive Application with large thread tasks**

	* Filename: NaivelyConcurrentTotalFileSize
	* Time Taken: Times out due to the deep hierarchy and "pool induced deadlock"
	* Task: For each file or subdirectory, create a task for finding its size and schedule it on the pool. Once tasks are scheduled for all files and subdirectories under a directory, wait for their size to be returned through the Future objects. To compute the total size for a directory, iterate over futures. Recursively schedule more tasks on the executor service pool, as long as there are more directories and files to visit. Use Java's Callable() interface's call() in the ExecutorService's submit() to schedule tasks for the pool. And use the Future object's get() method to retrieve the result. Program uses a fixed thread pool of 100

7. **Concurrent, Disk IO Intensive Application with smaller thread tasks**

	* Filename: ConcurrentTotalFileSize
	* Time Taken: Around 80 seconds
	* Task: To solve the timeout problem, make a change to decrease each task's compute - each task to return a list of subdirectories it finds, instead of the full size for a given directory. This will prevent holding threads for any period longer than simply fetching the immediate subdirectories and total the size of files in their directories.

8. **Concurrent, Disk IO Intensive Application with CountDownLatch and Atomic variables to simplify code**

	* Filename: ConcurrentTotalFileSizeWLatch
	* Time Taken: 28 seconds!!
	* Task: Use CountDownLatch and AtomicLong to simplify code

9. **Concurrent, Disk IO Intensive Application with Blocking Queues**

	* Filename: ConcurrentTotalFileSizeWQueue
	* Time Taken: 40 seconds
	* Task: Using a AtomicLong to hold the running file size leads to synchronisation bottleneck. Eliminate this by introducing a blocking-queue which holds the computed directory sizes. The main thread removes items from this queue as they appear to compute the running sum.

10. **Concurrent, Disk IO Intensive Application with Fork-Join**

	* Filename: FileSize
	* Time Taken: 30 seconds
	* Task: Recursively find directory size using an implementation of ForkJoin's RecursiveTask interface
	
11. 	