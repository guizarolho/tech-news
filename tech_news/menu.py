import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
    )


def get_news():
    number = input('Digite quantas notícias serão buscadas:')
    return get_tech_news(int(number))


def get_date():
    date = input('Digite a data no formato aaaa-mm-dd:')
    return search_by_date(date)


def get_title():
    title = input('Digite o título:')
    return search_by_title(title)


def get_tag():
    tag = input('Digite a tag:')
    return search_by_tag(tag)


def get_category():
    category = input('Qual a categoria:')
    return search_by_category(category)


def end_script():
    return 'Encerrando script'


def switch(option):
    opcoes = {
        '0': get_news,
        '1': get_title,
        '2': get_date,
        '3': get_tag,
        '4': get_category,
        '5': top_5_news,
        '6': top_5_categories,
        '7': end_script
    }
    try:
        return print(opcoes.get(option)())
    except TypeError:
        return print('Opção inválida', file=sys.stderr)


# Requisito 12
def analyzer_menu():
    option = input("""
    Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
    """)

    mensagem = switch(option)
    return mensagem


if __name__ == '__main__':
    analyzer_menu()
