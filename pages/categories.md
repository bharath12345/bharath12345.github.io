---
layout: layout
title: "Index by Categories"
category: posts
published: true
tags: test
categories: test
tweetfb: false
disqus: false
---

# Index by Categories

<ul class="listing">
    {% for post in site.categories %}
        {% for category in post.category %}
            {% if category == post.category %}
                <li><a href="{{ category }}">{{ category }}</a></li>
            {% endif %}
        {% endfor %}
    {% endfor %}
</ul>
