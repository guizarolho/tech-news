from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    results = search_news({'title': {'$regex': title, '$options': 'i'}})
    list = []
    for news in results:
        news_tuple = tuple([news['title'], news['url']])
        list.append(news_tuple)
    return list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    results = search_news({'tags': {'$regex': tag, '$options': 'i'}})
    list = []
    for news in results:
        news_tuple = tuple([news['title'], news['url']])
        list.append(news_tuple)
    return list


# Requisito 9
def search_by_category(category):
    results = search_news({'category': {'$regex': category, '$options': 'i'}})
    list = []
    for news in results:
        news_tuple = tuple([news['title'], news['url']])
        list.append(news_tuple)
    return list


if __name__ == '__main__':
    results = search_by_tag("Tecnologia")
    print(results)
