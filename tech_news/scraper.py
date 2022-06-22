import requests
from parsel import Selector
import time


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
def scrape_noticia(html_content):
    selector = Selector(html_content)
    posts = []
    for news in selector.css('.entry-preview'):
        url = news.css('span > a.url.fn.n::attr(href)').get()
        author = news.css('span > a.url.fn.n::text').get()
        title = news.css('h2.entry-title > a::text').get()
        date = news.css('li.meta-date::text').get()
        posts.append({
            'url': url,
            'title': title,
            'timestamp': date,
            'writer': author,
            })

    return posts


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    html_page = fetch('https://blog.betrybe.com/page/2/')
    content = scrape_noticia(html_page)
    print(content)
