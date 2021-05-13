"""
Необходимо парсить страницу со свежими статьями на Хабре (https://habr.com/ru/all/) 
и выбирать те статьи, в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта). 
Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы). 
Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.
Шаблон кода:
# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
# Ваш код
"""
import requests
from bs4 import BeautifulSoup

def scrap(keywords, url):
    disaire_hub = set(keywords)
    request = requests.get(url)
    if not request.ok:
        raise ValueError('Site not found')
    soup = BeautifulSoup(request.text, 'html.parser') # экземпляр класса BS, HTML
    for article in soup.find_all('article'):
        title = article.find('h2', class_="post__title") # Получаем заголовки статей
        title_set = set()
        for i in title.text.strip().split():
            title_set.add(i.lower().strip(':".,!?()«»'))  # преобразуем в нижний регистр и избавляемся от спецсимволов
        tags = article.find_all('ul', class_="post__hubs inline-list") # Получаем список тэгов статей
        tags_set = set()
        for i in tags: # преобразуем в множество
            for j in i.text.split():
                tags_set.add(j.lower().strip(':".,!?()«»')) # преобразуем в нижний регистр и избавляемся от спецсимволов    
        text_block = [t.text for t in article.find_all('p')] # получаем текст блока   
        text_set = set()
        for i in text_block: 
            for j in i.split():
                text_set.add(j.lower().strip(':".,!?()«»')) # преобразуем в нижний регистр и избавляемся от спецсимволов 
        text_set = text_set | tags_set | title_set # объединение всех множеств одного блока
        if disaire_hub & text_set:            
            href = article.find('h2', class_="post__title").find('a').attrs.get('href') 
            print('Совпадение по тэгу ', str(disaire_hub & text_set)) 
            print(article.find('span', class_="post__time").text)
            print(title.text.strip())
            print(href)
            print()

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    url = 'https://habr.com/ru/all/'
    scrap(KEYWORDS, url)