Title: Index by Categories
Slug: pages/categories

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
