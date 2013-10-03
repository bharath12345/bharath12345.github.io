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

4. What are big-O and big-Omega notations? Why are they needed?
big-O is for the upper bound. big-Omega is for the lower bound. (there is also a big-Theta that is a little more involved idea). The running times of a great many programs depend only on a small subset of their instructions - so when running time of algorithms are proportional to squares(N<sup>2</sup>) or cubes(N<sup>3</sup>) or exponentials(2<sup>N</sup>) of input data counts (N), we know that these algorithms will not scale for large inputs (N). Only when running times of algorithms are proportional to linear(N), linearithmic(NlogN) or logarithmic(logN) or constant can they be expected to scale for large inputs. 

5. What is the base of log when we are talking about complexities of algorithms? Why?
Base-2. In terms of Big-O, the base doesn't matter because the change of base formula implies that it's only a constant factor difference. That is logarithms from base 10 or base 2 or base e can be exchanged (transformed) to any other base with the addition of a constant. The critical thing to understand is that logarithms (of any base) increase slowly with the increase of N. However, observe this table of log values… (with respect to complexity of algorithms, the value of N can never be fractional or negative anyway...)

![image](http://bharathwrites.in/images/algorithms/log.png)

6. What does Java Arrays.sort() implement?
Mergesort till Java6. TimSort from Java7 onwards...

7. Order of growth graph?
Here is the log-log plot (both size(N) x-axis and time(T) y-axis are in logarithms)
![image](http://bharathwrites.in/images/algorithms/orderofgrowth.png)


8. 
