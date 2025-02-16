# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://shanej90.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Set the path to your Flex theme
THEME = 'themes/Flex'
SITETITLE = "Shane Jackson: Data Analyst"
SITESUBTITLE = "Examples of my work"
SITEDESCRIPTION = "Examples of my work"
SITELOGO = SITEURL + "images/me.jpg"
HOME_HIDE_TAGS = True

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

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
