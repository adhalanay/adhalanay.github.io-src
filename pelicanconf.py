#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrei Halanay'
SITENAME = u'My Web Site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'
DEFAULT_DATE = 'fs'
STATIC_PATHS = ['pdf','imagini']
THEME = "/home/andrei/repozitorii/elegant"
#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['render_math', 'gravatar']
TYPOGRIFY = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#('Another social link', '#'),)

LANDING_PAGE_ABOUT = {'title' : 'Teme şi altele',
        'details': 'e-mail:halanay@fmi.unibuc.ro'}

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
