AUTHOR = 'Shane Jackson'
SITENAME = 'Shane Jackson: Data Analyst'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

#Themes - flex options
THEME = "themes/Flex"
SITETITLE = "Shane Jackson: Data Analyst"
SITESUBTITLE = "Examples of my work"
SITEDESCRIPTION = "Examples of my work"
SITELOGO = SITEURL + "images/me.jpg"
HOME_HIDE_TAGS = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("My work", "/my-work"),
    ("About", "/about-me"),
)

#MENU

MAIN_MENU = False

MENUITEMS = (
    ("About", "/about-me"),
    ("My work", "/my-work"),
     )

SOCIAL = (
        ("github", "https://github.com/shanej90"),
        ("linkedin", "https://www.linkedin.com/in/shanejackson294/"),
        ("twitter", "https://twitter.com/jacksonshane90"), 
     )

GITHUB_CORNER_URL = "https://github.com/shanej90/shanej90.github.io"

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
