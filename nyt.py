# nyt.py
# Reads a news RSS feed. Feed KEYS and URLS are maintained in a shelve file.
# Shelve file is managed with command-line arguments
# Outputs the first 6 items: title, link, description

from bs4 import BeautifulSoup
from termcolor import cprint
import requests, shelve, sys
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('########## Start program ##########')

shelveFile = "urls.she"
sf = shelve.open(shelveFile)

args = sys.argv
logging.debug("argv length = " + str(len(args)) + " - " + str(args))

if len(args) == 1:
    raise Exception("missing args")

if len(args) > 1:   # there is a command 'add', 'del', 'list', or KEY
    if args[1].lower() == 'list':
        print(str(list(sf.keys())))
        exit()
    elif args[1].lower() == 'add':
        sf[args[2]] = args[3]
        print(str(list(sf.keys())))
        exit()
    elif args[1].lower() == 'del':
        del sf[args[2]]
        print(str(list(sf.keys())))
        exit()
    else:
        r = requests.get(sf[args[1]])

#("http://rss.nytimes.com/services/xml/rss/nyt/US.xml")
#("https://news.google.com/news/rss/headlines/section/topic/WORLD?ned=us&hl=en&gl=US")

data = r.text
soup = BeautifulSoup(data, "xml")

obj = soup.find('title')
cprint("\n" + obj.getText() + "\n", 'green', attrs=['bold', 'reverse'])

item = soup.find_all('item')
for i in range(0, min(6, len(item))): 
    cprint(item[i].find('title').getText(), 'cyan')
    cprint(item[i].find('link').getText(), 'blue')
    desc = item[i].find('description').getText()
    shoup = BeautifulSoup(desc, "lxml")
    print(shoup.getText())
    print()

print()
exit()
