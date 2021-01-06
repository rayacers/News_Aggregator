import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as BSoup
from news import News
import json

# scrape news resource from swissinfo focus page
def scrape_swissinfo():
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    base_url = "https://www.swissinfo.ch"
    url = base_url + "/eng/latest-news"

    content = session.get(url).content
    soup = BSoup(content, "html.parser")
    swissinfo_news = soup.find_all('article')

    news_aggregate = []

    for article in swissinfo_news:
        # news = News()
        news = {}
        main = article.find('a')
        news['title'] = main.find('h3').getText()
        news['link'] = base_url + main['href']
        news['content'] = main.find('p').getText().split(sep = '\n')[-1]
        news['image'] = base_url + main.find('img')['src']
        news['source'] = 'swissinfo'
        news['time'] = main.find('time')['datetime']
        news_aggregate.append(news)

    return news_aggregate

def scrape_ettoday():
    session = HTMLSession()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    base_url = "https://www.ettoday.net"
    url = base_url + "/news/focus/焦點新聞/"

    content = session.get(url).content
    soup = BSoup(content, "html.parser")
    ettoday_news = soup.find('div', {'class': "block block_1 infinite_scroll"}).find_all('div', {"class": "piece clearfix"} )
    
    news_aggregate = []
    
    for article in ettoday_news:
        
        news = {}
        news['title'] = article.find('h3').find('a').getText()
        news['link'] = base_url + article.find('a')['href']
        news['content'] = article.find('p').getText()
        news['image'] = article.find('img')['data-original']
        news['source'] = 'ettoday'
        news['time'] = 'none'
        news_aggregate.append(news)
    
    return news_aggregate
    

def scrape_nytimes():
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    base_url = "https://www.nytimes.com"
    url = base_url + "/section/world"
 
    content = session.get(url).content
    soup = BSoup(content, "html.parser")
    nytimes_news = soup.find_all('div', {"class": "css-1l4spti"} )

    news_aggregate = []
    for article in nytimes_news:

        news = {}
        news['title'] = article.find('h2').getText()
        news['link'] = base_url + article.find('a')['href']
        news['content'] = article.find('p').getText()
        news['image'] = article.find('img')['src']
        news['source'] = 'nytimes'
        news['time'] = 'none'
        news_aggregate.append(news)
    
    return news_aggregate

if __name__ == '__main__':
    news_aggregate = scrape_ettoday()
    print(news_aggregate[0])