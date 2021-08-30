from bs4 import BeautifulSoup
import collections
import requests


def parser(url):
    r = requests.get(url).text

    end_dict = {}

    all_tags = collections.Counter()
    soup = BeautifulSoup(r, 'html.parser')
    nested = 0
    """Получим все теги которые есть на странице"""
    for tag in soup.find_all(True, recursive=True):
        all_tags[tag.name] += 1
        nested += 1
    """Для каждого полученого тега найдем количество вложенных"""
    for item in list(all_tags):
        list_of_double_tags = soup.find_all(item)
        tag_counter = 0
        every_double_tag = 0
        for every_double_tag in range(len(list_of_double_tags)):
            """Функция find_all возвращает массив элементов(в нашем случае повторяющиеся теги),
            поэтому нужно искать вложенные теги для каждого повторяющегося элеметна"""
            for tag in soup.find_all(item)[every_double_tag].find_all(True, recursive=True):
                tag_counter += 1
        end_dict.update(
            {
                item: {
                    'count': every_double_tag + 1,
                    'nested': tag_counter
                }
            }
        )
    return end_dict
