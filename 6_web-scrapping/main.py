"""
Необходимо парсить страницу со свежими статьями на Хабре (https://habr.com/ru/all/) 
и выбирать те статьи, в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта). 
Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы). 
Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.
Шаблон кода:
# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
# Ваш код
Дополнительное (необязательное) задание
Улучшить скрипт так, чтобы он анализировал не только preview-информацию статьи, но и весь текст статьи целиком.
Для этого потребуется получать страницы статей и искать по тексту внутри этой страницы.
"""
import requests
from bs4 import BeautifulSoup
import re

def scrap(keywords, url):
    disaire_hub = set(keywords)
    request = requests.get(url)
    if not request.ok:
        raise ValueError('Site not found')
    soup = BeautifulSoup(request.text, 'html.parser') # экземпляр класса BS, HTML
    for article in soup.find_all('article'):
        title = article.find('h2', class_="post__title") # Получаем заголовки статей
        # print(title.text)
        title_set = set()
        for i in title.text.strip().split():
            title_set.add(re.search('\w*', i).group(0).lower())  # преобразуем в нижний регистр и избавляемся от спецсимволов
        tags = article.find_all('ul', class_="post__hubs inline-list") # Получаем список тэгов статей
        tags_set = set()
        for i in tags: # преобразуем в множество
            for j in i.text.split():
                tags_set.add(re.search('\w*', j).group(0).lower()) # преобразуем в нижний регистр и избавляемся от спецсимволов    
        text_block = [t.text for t in article.find_all('p')] # получаем текст блока   
        text_set = set()
        for i in text_block: 
            for j in i.split():
                text_set.add(re.search('\w*', j).group(0).lower()) # преобразуем в нижний регистр и избавляемся от спецсимволов
# Дополнительное задание       
        href_page = article.find('a', class_="btn btn_x-large btn_outline_blue post__habracut-btn").attrs.get('href') # ссылка на страницу
        request_page = requests.get(href_page)
        if not request_page.ok:
            raise ValueError('Site not found')
        soup_page = BeautifulSoup(request_page.text, 'html.parser') # экземпляр класса BS, HTML
        text_page = soup_page.find_all('p') # Получаем параграфы статьи
        text_page_set = set()
        for i in text_page: 
            for j in i.text.split(): 
                text_page_set.add(re.search('\w*', j).group(0).lower()) # преобразуем в нижний регистр, избавляемся от спецсимволов, добавляем в set

        text_set = text_set | tags_set | title_set | text_page_set # объединение всех множеств одного блока
        if disaire_hub & text_set:            
            href = article.find('h2', class_="post__title").find('a').attrs.get('href') 
            print('Совпадение по тэгу ', str(disaire_hub & text_set)) # тэг
            print(article.find('span', class_="post__time").text) # время
            print(title.text.strip()) # заголовок
            print(href, '\n')   # ссылка

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    url = 'https://habr.com/ru/all/'
    scrap(KEYWORDS, url)