from tech_news.database import find_news
from collections import Counter


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
    results = find_news()

    list = {}
    for news in results:
        if not list.get(news['category']):
            list[news['category']] = 0
        list[news['category']] += 1
    key_value = Counter(list).most_common(5)
    list_names = []
    for tuple in key_value:
        list_names.append(tuple[0])
    return list_names


if __name__ == '__main__':
    content = top_5_categories()
    print(content)
