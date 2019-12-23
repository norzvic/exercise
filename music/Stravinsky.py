# Scraping discography of Igor Stravinsky from wikipedia

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.request import quote
import re
import os

# Open url
html = urlopen("https://en.wikipedia.org/wiki/List_of_compositions_by_Igor_Stravinsky").read()

