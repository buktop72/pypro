"""
2.Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
"""
from hashlib import md5

def hash (path: str):
    with open(path, encoding ='utf-8') as file:
        for line in file:        
            yield md5(line.encode()).hexdigest()

if __name__ == '__main__':
    hash_summ = hash('README.md')
    for i in hash_summ:
        print(i)





