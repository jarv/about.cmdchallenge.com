#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jarv'
SITENAME = u'cmdchallenge'
SITEURL = 'https://about.cmdchallenge.com'
FEED_RSS = 'rss.xml'

PATH = 'content'
GOOGLE_ANALYTICS_ID = ''
TIMEZONE = 'US/Eastern'
THEME = 'cmdchallenge'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SUMMARY_MAX_LENGTH = 1000

DEFAULT_PAGINATION = 5
STATIC_PATHS = ['extra', 'static']
ARTICLE_EXCLUDES = ['extra', 'static']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }
EMAIL = 'info@cmdchallenge.com'
SOCIAL = [
        ('twitter', 'https://twitter.com/thecmdchallenge')
        ]

LOAD_CONTENT_CACHE = False
RESPONSIVE_IMAGES = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
