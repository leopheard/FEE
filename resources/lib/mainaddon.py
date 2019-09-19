import requests
import re
from bs4 import BeautifulSoup

url1 = "https://wordsandnumbers.libsyn.com/rss" #WORDSANDNUMBERS
url2 = "http://feeaudioxp.libsyn.com/rss" #AUDIOEXPERIENCE
url3 = "https://feecast.libsyn.com/rss" #FEECAST

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
#get_soup1("https://wordsandnumbers.libsyn.com/rss")

def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("http://feeaudioxp.libsyn.com/rss")

def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
get_soup3("http://feecast.libsyn.com/rss")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://fee.org/media/27638/words-numbers.jpg?mode=crop&width=250&height=250",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/54/a9/24/54a9246c-b68c-9f6f-6ebf-ab9ef46f03ee/mza_1457869927458728605.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {

                'url': link,
                'title': title,
                'thumbnail': "https://fee.org/media/28254/feecast-square-thumbnail-1400.png?mode=crop&width=250&height=250",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
