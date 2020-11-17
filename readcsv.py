import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import csv
import datetime
import time
from queries import select, update, insert

# Open an example CSV file and insert the values to an empty list
try:
  with open("####", "rt") as csvfile:
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
    data = select(site, st)
    if len(data) == 0:
      st = current_time()
      insert(site, title, body_nospace, body_raw, st)
    else:
      st = current_time()
      update(site, title, body_nospace, body_raw, st)