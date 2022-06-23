from tech_news.database import search_news
import locale
import datetime


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
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        date_convert = datetime.datetime.strptime(date, '%Y-%m-%d')
        format_date = date_convert.strftime('%-d-%B-%Y').replace('-', ' de ')

        results = search_news(
            {'timestamp': {'$regex': str(format_date), '$options': 'i'}}
        )
        list = []
        for news in results:
            news_tuple = tuple([news['title'], news['url']])
            list.append(news_tuple)
        return list
    except ValueError:
        raise ValueError("Data inválida")


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

