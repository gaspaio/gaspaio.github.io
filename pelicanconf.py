#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rodolfo Ripado'
SITENAME = 'Gaspaio (a.k.a. Rodolfo Ripado)'
SITEURL = 'http://gaspaio.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/in/rodolforipado'),
          ('Github', 'https://github.com/gaspaio'),
          ('Twitter', 'https://twitter.com/gaspaio'))

DEFAULT_PAGINATION = 20

DEFAULT_METADATA = {
    'status': 'draft',
}

THEME = "themes/pelican-sober"

PELICAN_SOBER_ABOUT = "Web architecture, automation, python, nodejs, data science, machine learning."
PELICAN_SOBER_HEADER_LINKS = [("CV", "cv.fr.pdf")]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/cv.fr.pdf': {'path': 'cv.fr.pdf'},
}

OUTPUT_RETENTION = ['prez']

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math"]
