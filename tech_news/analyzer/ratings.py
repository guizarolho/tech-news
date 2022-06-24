from tech_news.database import find_news


# Requisito 10
def top_5_news():
    results = find_news()

    def by_title(e):
        return e['title']
    news_sorted = sorted(results, key=by_title)

    def by_comments(e):
        return e['comments_count']
    news_sorted.sort(reverse=True, key=by_comments)
    list = []
    for news in news_sorted:
        news_tuple = tuple([news['title'], news['url']])
        list.append(news_tuple)
    return list[0:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


if __name__ == '__main__':
    content = top_5_news()
    print(content)
