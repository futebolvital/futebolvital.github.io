#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Raphael Campos'
SITENAME = 'Futebol Vital' 
SITESUBTITLE = 'Amizade e Futebol'
#SITEURL = 'http//futebolvital.github.io/'
SITELOGO = '/vital.jpg'
SITEDESCRIPTION = 'Futebol Vital'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

COPYRIGHT_YEAR = 2018

THEME = "themes/Flex"
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'

#ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
#if {name}
    #ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{name}/'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
#if {name}
    #ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{name}/'index.html'

#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives', 'authors'))
#PAGINATED_DIRECT_TEMPLATES = (('blog',))
#TEMPLATE_PAGES = {'index.html',}

# Default theme language.
I18N_TEMPLATES_LANG = 'br'
#MAIN_LANG = 'en'
# Your language.
DEFAULT_LANG = 'br'
LOCALE = 'pt_BR.utf8'
OG_LOCALE = 'pt_BR.utf8'

MENUITEMS = {
    'Arquivos': '/arquivos.html',
    'Categorias': '/categorias.html',
    'Tags': '/tags.html',
}

#I18N_SUBSITES = {
#    'en': {
#        'SITESUBTITLE': 'Footebal and Friendship',
#        'SITEDESCRIPTION': 'Vital\'s Football',
#        'LOCALE' : 'en_US.utf8',
#        'OG_LOCALE' : 'en_US.utf8',
#        'MENUITEMS': {
#                'Archives': '/arquivos.html',
#                'Categories': '/categorias.html',
#                'Tags': '/tags.html',
#            }
#        },
#    }

#DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Get Pelican', 'http://getpelican.com/'),
        # ('Python.org', 'http://python.org/'),
        # ('Jinja2', 'http://jinja.pocoo.org/'),
        # ('You can modify those links in your config file', '#'),
        )

SOCIAL = (
          ('facebook', 'https://www.facebook.com/groups/625677687525465/'),
          ('github', 'https://github.com/futebolvital'),
          )


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# mapping: language_code -> settings_overrides_dict

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


DEFAULT_CATEGORY = 'Futebol'
USE_FOLDER_AS_CATEGORY = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
TYPOGRIFY = True
DATE_FORMATS = {
    'br': ('pt_BR.utf8','%a, %d de %B de %Y'),
}

#DISQUS_SITENAME='raphaelncampos'
GITHUB_URL='https://github.com/futebolvital'

PLUGIN_PATHS = ['/home/rcampos/git/pessoal/pelican-plugins']
PLUGINS = [ 
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code']
        #    'liquid_tags.include_code', 'liquid_tags.notebook']
