# nws.py
# Reads news RSS (xml) feeds. 
# Feed KEYS and URLS are maintained in a shelve file.
# Shelve file is managed with command-line arguments
# Outputs the first n-items: title, link, description
# Demostrates:
#   - Web scraping (xml)
#   - Applying color to terminal output
#   - List serialization with Shelve
#   - Text formating
#   - logging
#   - Downloading webpage source text

from bs4 import BeautifulSoup
from termcolor import cprint
import requests, shelve, sys, textwrap
#import logging

#logging.basicConfig(filename='log.txt', level=logging.DEBUG, 
#   format='%(asctime)s - %(levelname)s - %(message)s')

#logging.debug('########## Start program ##########')

nitems = 6  # max number of news items to print
wdesc = 72  # width of description text for console

shelveFile = "urls.she"
sf = shelve.open(shelveFile)

args = sys.argv
#logging.debug("argv length = " + str(len(args)) + " - " + str(args))

if len(args) == 1:
    print("\nargs:\n add KEY URL\n del KEY")
    print(" list [all]")
    print(" KEY")
    exit()

if len(args) > 1:   # there is a command 'add', 'del', 'list', or KEY
    if args[1].lower() == 'list':
        if len(args) > 2:
            print()
            for i in list(sf.keys()):
                print( i + "\n" + sf[i])
        else:
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

data = r.text
soup = BeautifulSoup(data, "xml")

obj = soup.find('title')
cprint("\n" + obj.getText() + "\n", 'green', attrs=['bold', 'reverse'])

item = soup.find_all('item')
for i in range(0, min(nitems, len(item))): 
    ttl = item[i].find('title').getText()
    shoup = BeautifulSoup(ttl, "lxml")
    cprint(shoup.getText(), 'cyan')
    cprint(item[i].find('link').getText(), 'blue')
    desc = item[i].find('description').getText()
    # REMOVE COMMENTS TO PRINT DESCRIPTIONS
    #shoup = BeautifulSoup(desc, "lxml")
    #s = shoup.getText()
    #print(textwrap.fill(s,wdesc))
    print()

print()
exit()
