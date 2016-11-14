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
DEFAULT_DATE_FORMAT = ('%B %d %Y')

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
TRANSLATION_FEED_ATOM = None
if os.name == 'nt':
    FEED_ALL_ATOM = 'feeds\\all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds\\%s.atom.xml'
    TAG_FEED_ATOM = 'feeds\\tags\\%s.atom.xml'
else:
    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
    TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'

if os.name == 'nt':
    THEME = 'C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-themes\\aboutwilson'
else:
    THEME='/Users/nikhil/Documents/pelican_theme/aboutwilson'
# Blogroll

LINKS = ()

# Social widget
SOCIAL = ()

# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }
if os.name == 'nt':
    PLUGIN_PATHS = ['C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-plugins']
else:
    PLUGIN_PATHS = ['/Users/nikhil/Documents/pelican_plugins']

#PLUGINS = ['extract_toc','render_math','better_figures_and_images']

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','toc']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
PAGE_PATHS = ['pages',]