#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick Flynn'
SITENAME = "Patrick Flynn's Website"
SITEURL = ''
TAGLINE = 'Random thoughts...'

THEME="./theme"
PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_PATHS=['july2020', 'august2020', 'september2020', 'october2020', 'december2020']
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
MENUITEMS = (
    ('GitHub', 'https://github.com/patrickf2000'),
    ('LinkedIn', 'https://www.linkedin.com/in/patrick-flynn4664/'),
)

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_ANALYTICS="UA-G-5NP3VXCK9F-Y"
