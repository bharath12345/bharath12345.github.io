#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Bharadwaj'
SITENAME = "Bharadwaj's Blog"
SITEURL = ''
SITE_DESCRIPTION = 'thoughts, musings, writings'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/bharath12345'),
    ('LinkedIn', 'https://www.linkedin.com/in/bharadwaj'),
)

DEFAULT_PAGINATION = 5

# Pagination URLs
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# URL settings to match Jekyll structure
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PATH_METADATA = '(?P<path_no_ext>.*)\..*'

# Static paths
STATIC_PATHS = ['images', 'resources', 'extra']

# Copy extra files to root
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Theme settings
THEME = 'themes/custom'

# Plugins
PLUGINS = ['pelican.plugins.webassets']

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
            'toc_depth': '2-6',
        },
    },
    'output_format': 'html5',
}

# Author info
AUTHOR_EMAIL = 'bharath12345@gmail.com'
GITHUB_URL = 'https://github.com/bharath12345'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Drafts
WITH_FUTURE_DATES = False

# Direct templates
DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'search']
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}
