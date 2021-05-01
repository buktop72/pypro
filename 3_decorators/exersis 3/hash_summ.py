"""
2.Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
"""

from hashlib import md5
from logger_path import logger_path

# добавлен декоратор сохраняющий логи в указанный файл
@logger_path('log3.txt')
def hash (path: str):
    with open(path, encoding ='utf-8') as file:
        for line in file:        
            yield md5(line.encode()).hexdigest()



   





