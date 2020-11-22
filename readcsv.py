import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import csv
import datetime
import time
from queries import select, insert_update

# Open an example CSV file and insert the values to an empty list
try:
  with open("domains.csv", "rt") as csvfile:
    csvArray = []
    for row in csv.reader(csvfile, delimiter = ' '):
      csvArray.append(row)
except Exception as excp:
  print(excp)

#Function to soup the website got from the example CSV using HTML parser
def soup_function(site):
    req = urllib.request.Request(F"https://{site}", headers = {'User-Agent': 'Mozilla/5.0'})
    try:
      soup = BeautifulSoup(urllib.request.urlopen(req), "html.parser")
    except Exception as exp:
      print(exp)
    return soup

# Get the wesbpage elements such as title, raw body with HTML tags & body without HTML tags and removal of witespaces
def elements(soup):
    global title
    title = soup.title.string
    global body_raw
    body_raw = soup.find("body")
    global body_nospace
    body_nospace = ' '.join(body_raw.get_text().split())

# Simple function to get the current time
def current_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

#Iterate through the domain list
for x in csvArray:
    site = ','.join(x)
    soup = soup_function(site)
    elements(soup)
    st = current_time()
    _SQL_select = (""" select WEBSITE_URL from website.site where website_url = %s""")
    data = None
    data = select(site, st, _SQL_select, 1)
    if data is None:
      st = current_time()
      p = "Insert executed"
      _SQL = ("""INSERT INTO website.site (WEBSITE_URL, WEBSITE_TITLE, SITE_BODY, SITE_HTML) VALUES (%s, %s, %s, %s)""")
      insert_update(site, title, body_nospace, body_raw, st, _SQL, p)
    else:
      st = current_time()
      p = "updated executed"
      _SQL = ("""UPDATE website.site SET WEBSITE_TITLE = %s, SITE_BODY = %s, SITE_HTML = %s where WEBSITE_URL = %s""")
      insert_update(site, title, body_nospace, body_raw, st, _SQL, p)
