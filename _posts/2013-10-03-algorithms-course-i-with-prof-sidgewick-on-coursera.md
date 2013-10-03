---
layout: post
title: "Algorithms Course I With Prof Sidgewick on Coursera"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

1. Why study Algorithms and Data Structures? Why are they important?
Computers, no matter how powerful, have space and time constraints. Poorly thought through implementations for computing problems can take years to compute even when computing resources are massive. For example -

![image](http://bharathwrites.in/images/algorithms/timecompare.png)

2. Why learn, re-learn algorithms?

* The primary reason to do so is that we are faced, all too often, with completely new computing environments (hardware and software) with new features that old implementations may not use to best advantage
* As a professional, it is a crime to use tools without their thorough understanding. So as Java programmers, to use HashMap and TreeSet without the knowledge of the underlying resource utilisation and performance impact is…
* Intellectually satisfying

3. How do you measure how long will your program take to run?
* Repeated runs in thousands to find the mean and standard-deviation
* Run it for different quantum's of input data 'N' - find mean and std-dev for different N after thousands of runs
* Find a relationship between N and time-taken by plotting on a graph - is the graph linear? hyperbolic? logarithmic? 

4. Why measure how long programs take to run?
Knowing the order of growth of the running time of an algorithm provides precisely the information that you need to understand limita- tions on the size of the problems that you can solve. Developing such understanding is the most important reason to study performance.

4. What are big-O and big-Omega notations? Why are they needed?
big-O is for the upper bound. big-Omega is for the lower bound. (there is also a big-Theta that is a little more involved idea). The running times of a great many programs depend only on a small subset of their instructions - so when running time of algorithms are proportional to squares(N<sup>2</sup>) or cubes(N<sup>3</sup>) or exponentials(2<sup>N</sup>) of input data counts (N), we know that these algorithms will not scale for large inputs (N). Only when running times of algorithms are proportional to linear(N), linearithmic(NlogN) or logarithmic(logN) or constant can they be expected to scale for large inputs.

4. Then why is big-O not useful for predicting performance or for comparing algorithms?
The primary reason is that it describes only an upper bound on the running time. Actual performance might be much better. The running time of an algorithm might be both O(N2) and ~ a N log N. As a result, it cannot be used to justify tests like our doubling ratio test (see Proposition C on page 193). 

5. What is the base of log when we are talking about complexities of algorithms? Why?
Base-2. In terms of Big-O, the base doesn't matter because the change of base formula implies that it's only a constant factor difference. That is logarithms from base 10 or base 2 or base e can be exchanged (transformed) to any other base with the addition of a constant. The critical thing to understand is that logarithms (of any base) increase slowly with the increase of N. However, observe this table of log values… (with respect to complexity of algorithms, the value of N can never be fractional or negative anyway...)

![image](http://bharathwrites.in/images/algorithms/log.png)

6. What does Java Arrays.sort() implement?
Mergesort till Java6. TimSort from Java7 onwards...

7. Order of growth graph?
Here is the log-log plot (both size(N) x-axis and time(T) y-axis are in logarithms)
![image](http://bharathwrites.in/images/algorithms/orderofgrowth.png)

8. Example of each -

constant time - assignment statement
logarithmic - binary search
linear - find the maximum value
linearithmic - merge sort
quadratic - double for/while loop
cubic - triple for/while loop
exponential - brute force search

9. Why develop faster algorithms?
Faster algorithms help us to address larger problems

10. Why study memory utilisation of Java programs?
if you have 1GB of memory on your computer (1 billion bytes), you cannot fit more than about 32 mil- lion int values or 16 million double values in memory at any one time.

11. How many bytes in memory are required to store a reference to a Java Object?
4 bytes on a 32 bit system. 8 bytes on a 64 bit system

12.  
