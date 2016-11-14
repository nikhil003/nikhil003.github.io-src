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

DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = False
EXPAND_LATEST_ON_INDEX = True
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = 'fs'

if os.name == 'nt':
    THEME = 'C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-themes\\bootstrap2'
else:
    THEME='/Users/nikhil/Documents/pelican_theme/bootstrap2'
# Blogroll

LINKS = ()

# Social widget
SOCIAL = ()

MARKUP = ('md',)

#STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }
if os.name == 'nt':
    PLUGIN_PATHS = ['C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-plugins']
else:
    PLUGIN_PATHS = ['/Users/nikhil/Documents/pelican_plugins']

PLUGINS = ['sitemap','extract_toc','render_math','liquid_tags.notebook','liquid_tags.img']

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','toc']
NOTEBOOK_DIR = 'notebooks'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
PAGE_PATHS = ['pages',]
IGNORE_FILES = ['.ipynb_checkpoints']
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')