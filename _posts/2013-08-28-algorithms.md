---
layout: post
title: "Algorithms"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

1. What are the well-known order of classifications for algorithms? Give an example for each.
    * Constant - time taken is 'c' which is unrelated to N: assignment statements, arithmetic operations (not in a for loop)
    * Logarithmic - time taken is proportional to log N: Binary Search
    * Linear - time taken is proportional to N: addition in a for loop
    * Linearithmic - time taken is proportional to NlogN: Mergesort, Quicksort
    * Quadratic - time taken is proportional to N-square - nested for loops, selection sort
    * Cubic - time taken is proportional to N-cube: three nested for loops
    * Exponential - time taken is proportional to 2-to-the-power-of-N (or some x-to-the-power-of-N)

2. Plot of problem-size vs. time for these well known order of classifications?
(todo: show the plot)

3. Why develop a faster algorithm?
    * lesser strain on computing resources
    * the faster algorithm enables us to address much larger problems

4. How do you calculate the performance of a program you have designed/written?
    * Develop an input generator that produces inputs that model the scaling inputs expected in practice (N, 2N, 10N, 20N, 100N etc)
    * Run the program to calculate the ratio of each running time with the previous
    * Put the numbers on a graph to know the "order of growth"

5. What is the number of bytes needed to represent a machine address on a 64-bit system?
8 bytes

6. If 'int' primitive type takes 4 bytes in Java, what does the boxed Integer take?
24 bytes

7. Memory for char in Java?
2 bytes

8. Memory for Date compared to date stored as long?
Date object - 32 bytes
long date - 4 bytes

9. Memory for array of size N?
int array - 24 + 4N
char array - 24 + 2N and so on

10. Memory for two-dimensional M-by-N array of double?
24 bytes (overhead for the array of arrays) plus 8 M bytes (references to the row arrays) plus M times 16 bytes (overhead from the row arrays) plus M times N times 8 bytes (for the N double values in each of the M rows) for a grand total of 8NM + 32M + 24 ~ 8NM bytes.

11. Does int[] a = new int[N] count as N array accesses (to initialize entries to 0)?
Most likely yes, so we make that assumption in this book, though a sophisticated compiler implementation might try to avoid this cost for huge sparse arrays.
