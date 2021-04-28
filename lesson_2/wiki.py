"""
1.Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.
"""
import json
import requests
class wiki:
    def __init__ (self, path: str):
        self.path = path      
        file = open(self.path, encoding ='utf-8')        
        data = json.load(file)
        for i in data:
            url = f'https://en.wikipedia.org/wiki/{i["name"]["common"]}' 
            ls = url.split()
            url = ('_').join(ls)           
            out_file = open('out.txt', 'a', encoding = 'utf-8')
            out_file.write(f'{i["name"]["common"]:45} - {url}\n')       
            out_file.close() 
        file.close()        

if __name__ == '__main__':
    wiki_country = wiki('countries.json')










