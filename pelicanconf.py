#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Nikhil Garg'
SITENAME = u'Personal Space'
SITEURL = 'http://nikhil003.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
if os.name == 'nt':
    THEME = 'C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-themes\\bootlex'
else:
    THEME='/Users/nikhil/Documents/pelican_theme/bootlex'
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }
if os.name == 'nt':
    PLUGIN_PATHS = ['C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-plugins']
else:
    PLUGIN_PATHS = ['/Users/nikhil/Documents/pelican_plugins']
PLUGINS = ['extract_toc','render_math','better_figures_and_images']
MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']

DEFAULT_PAGINATION = 2

if os.name == 'nt':
    ARTICLE_URL = '{slug}\\'
    ARTICLE_SAVE_AS = '{slug}\\index.html'
    PAGE_URL = '{slug}\\'
    PAGE_SAVE_AS = '{slug}\\index.html'
else:
    ARTICLE_URL = '{slug}/'
    ARTICLE_SAVE_AS = '{slug}/index.html'
    PAGE_URL = '{slug}/'
    PAGE_SAVE_AS = '{slug}/index.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
