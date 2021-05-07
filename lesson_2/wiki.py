"""
1.Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.
"""
import json
import requests

class Wiki:
    def __init__ (self, path: str):
        self.path = path
        self.item = -1     
        file = open(self.path, encoding ='utf-8')        
        self.data = json.load(file)        
    def __iter__(self):
        return self

    def __next__(self):
        self.item += 1
        if self.item >= len(self.data):  # условие выход из цикла
            raise StopIteration  # выход из цикла 
        return (self.data[self.item])  # в цикле for i in Wiki() self.data[self.item] подставится в i


if __name__ == '__main__':
    pass
