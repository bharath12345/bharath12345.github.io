---
layout: layout
title: "Index by Tags"
category: posts
published: true
tags: test
categories: test
tweetfb: false
disqus: false
---

# Index by Tags

<ul class="listing">
    {% for post in site.posts %}
        {% for tag in page.tags %}
            {% if tag == page.tag %}
                <li><a href="{{ tag }}">{{ tag }}</a></li>
            {% endif %}
        {% endfor %}
    {% endfor %}
</ul>

