AUTHOR = 'Sam'
SITENAME = 'Blog de Sam Des Bois'
SITEURL = ''
SITELOGO = '/images/44069150_10156839528988653_7117737592409292800_n.jpg'

THEME = "../"
PATH = "content"
OUTPUT_PATH = "blog/"

ROBOTS = "index, follow"

THEME = 'flex'
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False
HOME_HIDE_TAGS = True

# Locale config
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
OG_LOCALE = 'fr_FR'
LOCALE = ('fr_FR.UTF-8')
I18N_TEMPLATES_LANG = 'fr_FR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugin image-process
#IMAGE_PROCESS = {
#    "article-image": ["scale_in 300 300 True"],
#    "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
#}

# Blogroll
LINKS = (
    ("Home", "/index.html"),
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/profile.php?id=618863652'),
          ('Twitter', 'https://twitter.com/SamDesBois'),)

# Miscellaneous
DEFAULT_PAGINATION = 10
DISABLE_URL_HASH = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Ajouté par moi.

# Paramètres
# STATIC_PATHS = []

# # Isso comments integration
# ISSO_URL = "comments.samdesbois.eu"
# # ISSO_EMBED_JS_PATH = '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/isso/js/embed.dev.js'
# ISSO_OPTIONS = {
#     'avatar': 'false',
#     'gravatar': 'true',
#     'reply-to-self': 'true',
#     'reply-notifications': 'true',
# }
