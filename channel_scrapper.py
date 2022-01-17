from bs4 import BeautifulSoup as BS
from urllib.request import urlopen, Request

# channel search query
url = 'https://www.youtube.com/results?search_query=[keyword]&sp=EgIQAg%253D%253D'
keyword = "enter_your_keyword_you_want_to_search_for"
url = url.replace('[keyword]', keyword)
useragent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'

request = Request(url, headers={'ACCEPT-LANGUAGE': 'en-US,en;q=0.5'})
site = urlopen(request)
site = site.read()
data = BS(site,'lxml')

# file for reference
f = open('t.html','bw')
f.write(site)
f.close()


resultsList = data.find("ol", class_="item-section")
counter = 0
for li in resultsList:
    if(li.name == 'li'):
        h3 = li.find('h3', class_='yt-lockup-title')
        name = h3.a.get('title')
        href = h3.a.get('href')
        ul = li.find('ul', class_='yt-lockup-meta-info')
        videos = ul.text.strip()

        description = li.find('div', {'dir':'ltr'})
        print(name, videos)
        if(description != None):
            print(description.text.strip(), end="\n\n")

'''
temp2 = data.find_all('div',class_='ytd-channel-name')
temp1.extend(temp2)
channels = set(temp1)
print(channels)
'''
