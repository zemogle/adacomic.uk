AUTHOR = 'Edward Gomez'
SITENAME = "Ada's Adventures in Science"
# SITEURL = 'https://www.adacomic.uk'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PATH_METADATA = '(?P<path_no_ext>.*)\..*'
# PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'news/'
ARTICLE_SAVE_AS = 'news/{slug}/index.html'

ARCHIVES_SAVE_AS = 'news/index.html'

LANDING_PAGE_TITLE = "Ada's Adventures in Science"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True