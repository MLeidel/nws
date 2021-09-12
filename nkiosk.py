# nkiosk.py
# see nws.py
# to launch use: 
#   gnome-terminal --profile=news1 --geometry=88x40+100+100 -e python3 path/nkiosk.py

from bs4 import BeautifulSoup
from termcolor import cprint, os
import requests, textwrap, time

nurls = [
'http://feeds.washingtonpost.com/rss/rss_powerpost',
'http://feeds.washingtonpost.com/rss/rss_blogpost',
'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
'http://rss.nytimes.com/services/xml/rss/nyt/US.xml',
'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml']

inx = 0
nfeeds = 5  # number of xml urls in nurls list
nitems = 7  # max number of news items to print
wdesc = 80  # width of description text for console
sec = 10    # seconds per each of TEN tics (eg 10 x 10 = 100 seconds)

while True:
  r = requests.get(nurls[inx])
  inx += 1
  if inx == nfeeds:
    inx = 0

  data = r.text
  soup = BeautifulSoup(data, "xml")

  os.system('clear')
  obj = soup.find('title')
  cprint(obj.getText(), 'green', attrs=['bold', 'reverse'])

  item = soup.find_all('item')

  for i in range(0, min(nitems, len(item))): 
    ttl = item[i].find('title').getText()
    shoup = BeautifulSoup(ttl, "lxml")
    s = textwrap.fill(shoup.getText(), wdesc)
    cprint(s, 'yellow')
    # Descriptions
    desc = item[i].find('description').getText()
    shoup = BeautifulSoup(desc, "lxml")
    s = shoup.getText()
    print(textwrap.fill(s,wdesc))
    # cprint(item[i].find('link').getText(), 'white')
    print()

  for t in range(9, 0, -1):
    print("             \r", end='', flush=True)
    print('.' * t + '\r', end='', flush=True)
    time.sleep(sec)
