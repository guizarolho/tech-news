import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    results = search_news({'title': {'$regex': title, '$options': 'i'}})
    list = []
    for news in results:
        news_tuple = tuple([news['title'], news['url']])
        list.append(news_tuple)
    return list


pt_month = {
    'Jan': 'janeiro',
    'Feb': 'fevereiro',
    'Mar': 'março',
    'Apr': 'abril',
    'May': 'maio',
    'Jun': 'junho',
    'Jul': 'julho',
    'Aug': 'agosto',
    'Sep': 'setembro',
    'Oct': 'outubro',
    'Nov': 'novembro',
    'Dec': 'dezembro'
}


def date_locale(date):
    date_convert = datetime.datetime.strptime(date, '%Y-%m-%d')
    format_date = date_convert.strftime('%-d-%b-%Y').split('-')
    month = pt_month[format_date[1]]

    return f'{format_date[0]} de {month} de {format_date[2]}'


# Requisito 7
def search_by_date(date):
    try:
        date_br = date_locale(date)

        results = search_news(
            {'timestamp': {'$regex': str(date_br), '$options': 'i'}}
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


if __name__ == '__main__':
    results = search_by_date('2021-04-04')
    print(results)
