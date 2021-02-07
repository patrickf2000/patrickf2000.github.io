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

#PAGE_URL = '{slug}/'
#PAGE_SAVE_AS = '{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_PATHS = [
    'july2020', 'august2020', 'september2020', 'october2020', 'december2020',
    'january2021'
]

INDEX_SAVE_AS = 'blog_index.html'

CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Blog', INDEX_SAVE_AS, INDEX_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
)

# additional menu items
#MENUITEMS = (
#    ( 'Contact Me', 'contact-me.html'),
#    ( 'Projects', 'projects.html'),
#    ('GitHub', 'https://github.com/patrickf2000'),
#)

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_ANALYTICS="UA-213498014-7"

