#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://nikhil003.github.io'
RELATIVE_URLS = False

if os.name == 'nt':
    FEED_ALL_ATOM = 'feeds\\all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds\\%s.atom.xml'
else:
    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
if os.name == 'nt':
    THEME = 'C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-themes\\bootlex'
    PLUGIN_PATHS = ['C:\\Users\\Nikhil\\Documents\\python_setup\\pelican\\pelican-plugins']
else:
    THEME='/Users/nikhil/Documents/pelican_theme/bootlex'
    PLUGIN_PATHS = ['/Users/nikhil/Documents/pelican_plugins']

PLUGINS = ['extract_toc','render_math','better_figures_and_images']
MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']