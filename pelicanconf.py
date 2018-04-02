#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryan Carney'
SITENAME = u'Ryan Carney'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

THEME = "theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

INDEX_SAVE_AS = 'pages/blog.html'

MENUITEMS = (
    ('Blog', '/pages/blog.html'),
    ('About', '/pages/about.html'),
    )

DEFAULT_METADATA = {
        'status': 'draft',
}

PLUGIN_PATHS = ['./build/pelican-plugins']
PLUGINS = ['pelican_javascript']

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
