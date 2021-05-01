"""
1.Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, 
с которыми вызвалась и возвращаемое значение.
"""
from datetime import datetime

def logger(function):    
    def new_func(*args, **kwargs):
        result = function(*args, **kwargs)
        file = open('logs.txt', 'a', encoding = 'utf-8')
        file.write(f'{datetime.now()} - function: {function.__name__} - arguments: {args} {kwargs} - result: {result}\n')       
        file.close()        
        return result        
    return new_func