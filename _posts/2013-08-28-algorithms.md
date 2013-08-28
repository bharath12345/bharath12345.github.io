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