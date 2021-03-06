import requests
import time
from bs4 import BeautifulSoup
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
            )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    nodes = selector.xpath('//h2[has-class("entry-title")]').css(
        "a::attr(href)").getall()
    return nodes


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    nodes = selector.css('.current + .page-numbers::attr(href)').get()
    return nodes


# Requisito 4
# p.get_text in beautiful soup
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    author = selector.css('span > a.url.fn.n::text').get()
    title = selector.css('h1.entry-title::text').get()
    date = selector.css('li.meta-date::text').get()
    tags = selector.css('a[rel="tag"]::text').getall()
    comments = selector.css('div.comment-body').getall()
    paragraph = selector.css('script ~ p').get()
    soup = BeautifulSoup(paragraph, 'html.parser')
    post_category = selector.css('.label::text').get()

    return ({
        'url': url,
        'title': title,
        'timestamp': date,
        'writer': author,
        'comments_count': len(comments),
        'summary': soup.get_text(),
        'tags': tags,
        'category': post_category
    })


# Requisito 5
def get_tech_news(amount):
    BASE_URL = 'https://blog.betrybe.com'
    CURRENT = 1
    content = fetch(BASE_URL)
    url_list = scrape_novidades(content)[0:amount]

    while len(url_list) != amount:
        CURRENT = CURRENT + 1
        limit = amount - len(url_list)
        page_content = fetch(BASE_URL + f'/page/{CURRENT}/')
        new_links = scrape_novidades(page_content)[0:limit]
        url_list.extend(new_links)

    detailed = []
    for url in url_list:
        html_text = fetch(url)
        news = scrape_noticia(html_text)
        detailed.append(news)

    create_news(detailed)
    return detailed


if __name__ == '__main__':
    content = get_tech_news(5)
    print(content)
    print(len(content))
