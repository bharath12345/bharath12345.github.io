---
layout: layout
title: "Index of Posts by Date"
category: posts
published: true
tags: []
categories: []
tweetfb: false
disqus: false
---

# Index of Posts by Date

<ul class="listing">
    {% for post in site.posts %}
    <li>
        <span>{{ post.date | date: "%B %e, %Y" }}</span>
        <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endfor %}
</ul>
