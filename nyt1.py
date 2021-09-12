# nyt.py
# Reads the current New York Times US News RSS feed
# Outputs the first 6 items: title, link, description
#

from bs4 import BeautifulSoup
import requests
from termcolor import cprint

#url = input("Enter a website to extract the URL's from: ")
r  = requests.get("http://feeds.washingtonpost.com/rss/rss_powerpost")
#r  = requests.get("http://feeds.washingtonpost.com/rss/rss_powerpost")


data = r.text
soup = BeautifulSoup(data, "xml")

pubDate = soup.find('pubDate')
print("NYT rss\n" + pubDate.getText() + "\n")

item = soup.find_all('item')
for i in range(0, min(6, len(item))): 
    cprint(item[i].find('title').getText(), 'yellow')
    cprint(item[i].find('link').getText(), 'white')
    desc = item[i].find('description').getText()
    shoup = BeautifulSoup(desc, "lxml")
    print(shoup.getText())
    #print(item[i].find('description').getText())

print()
exit()
'''
<item>
    <title>
        Dartmouth College Professors Investigated Over Sexual Misconduct Allegations
    </title>
    <link>
        https://www.nytimes.com/2017/10/31/us/dartmouth-professors-sexual-misconduct.html?partner=rss&emc=rss
    </link>
    <guid isPermaLink="true">
        https://www.nytimes.com/2017/10/31/us/dartmouth-professors-sexual-misconduct.html
    </guid>
    <atom:link rel="standout" href="https://www.nytimes.com/2017/10/31/us/dartmouth-professors-sexual-misconduct.html?partner=rss&emc=rss"/>
    <media:content url="https://static01.nyt.com/images/2017/11/01/us/01dartmouth1-sub/01dartmouth1-sub-moth.jpg" medium="image" height="151" width="151"/>
    <media:description>
    Dartmouth College in Hanover, N.H., has placed three professors on leave and restricted their access to the campus while allegations of sexual misconduct are investigated.
    </media:description>
    <media:credit>Ian Thomas Jansen-Lonnquist for The New York Times</media:credit>
    <description>
        Three professors from the Department of Psychological and Brain Sciences have been put on paid leave as a criminal investigation is carried out.
    </description>
</item>

termcolor Text Properties:

Text colors:
grey
red
green
yellow
blue
magenta
cyan
white

Text highlights:
on_grey
on_red
on_green
on_yellow
on_blue
on_magenta
on_cyan
on_white

Attributes:
bold
dark
underline
blink
reverse
concealed

'''