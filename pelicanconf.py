#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick Flynn'
SITENAME = "Patrick's Website"
TAGLINE = 'Random thoughts...'
SITESUBTITLE = 'Computers and life...'

DELETE_OUTPUT_DIRECTORY = True

THEME="./theme"
PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 5

ARTICLE_PATHS = [
    'july2020', 'august2020', 'september2020', 'october2020', 'december2020',
    'january2021', 'february2021', 'march2021', 'april2021', 'june2021',
]

STATIC_PATHS = [ 'internal', 'pdfs' ]

INDEX_SAVE_AS = 'blog_index.html'

CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# additional menu items
MENUITEMS = (
    #('Blog', INDEX_SAVE_AS),
    ('Home', '/index.html'),
    ('Blog', '/blog_index.html'),
    ('Projects', '/pages/projects.html'),
    ('Resume', '/resume.html'),
    ('Contact', '/pages/contact-me.html'),
    ('GitHub', 'https://github.com/patrickf2000'),
)

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_ANALYTICS="UA-213498014-7"

