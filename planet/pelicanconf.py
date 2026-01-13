#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maciej Brencz'
SITENAME = 'Farerska Planeta'
SITEURL = ''

PATH = '../docs'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	('Pelican', 'http://getpelican.com/'),
	('Farerskie Kadry', 'https://farerskiekadry.pl/'),
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# RSS planet
PLUGINS = [
	'pelican_planet',
]

# https://pypi.org/project/pelican-planet/
PLANET_FEEDS = {
        "Anja's blog — My Faroe Islands": "https://the-faroe-islands.com/blog?format=rss",
	"Bloggur hjá Birgir Kruse": "https://birkblog.blogspot.com/feeds/posts/default?alt=rss",
	"Dalsbygd": "https://dalsbygd.blogspot.com/feeds/posts/default?alt=rss",
	"Farerskie kadry": "https://farerskiekadry.pl/feed",
	"Føroyar - Wyspy Owcze Pod Lupą": "https://havnar.blogspot.com/feeds/posts/default?alt=rss",
	"Hagstova - News from Statistics Faroe Islands": "https://hagstova.fo/fo/news/rss.xml",
	"Kringvarp Føroya": "https://kvf.fo/rss/news-english",
	"Kringvarp Føroya - Forsíða": "https://kvf.fo/rss/forsida",
	"Local.fo": "https://local.fo/feed/",
        "The Faroe Islands Podcast": "https://faroepodcast.libsyn.com/rss",
	"Wyspy Owcze Bez Tajemnic": "https://anchor.fm/s/4de2c820/podcast/rss",
	"Hvannrók": "https://www.hvannrok.fo/feed/",
	"Farerskie kadry na Facebooku": "https://macbre.github.io/farerskie-kadry-feed/facebook.xml",
	"Farerskie kadry na Instagramie": "https://macbre.github.io/farerskie-kadry-feed/instagram.xml",
	"Twitter - @ForoysktDaily na ": "https://nitter.cz/ForoysktDaily/rss",
	"Mastodon - @ForoysktDaily": "https://mastodon.social/@ForoysktDaily.rss",
	"Klub Miłośników Wysp Owczych Faroe.pl": "https://faroe.pl/feed/",
	"Farerskie szorty": "https://farerskiekadry.pl/szorty/feed",
	"r/FaroeIslands": "https://www.reddit.com/r/FaroeIslands.rss",
}

PLANET_TEMPLATE = 'planet.html.tmpl'
PLANET_PAGE = '../docs/index.html'

PLANET_MAX_ARTICLES = 50
PLANET_MAX_ARTICLES_PER_FEED = 5

# set up logging
import logging; logging.basicConfig(level=logging.DEBUG)

for name, url in PLANET_FEEDS.items():
	print('1. [{}]({})'.format(name, url))

