#2.Написать декоратор из п.1, но с параметром – путь к логам.
from datetime import datetime

def logger_path(path :str):
    def logger(function):    
        def new_func(*args, **kwargs):
            result = function(*args, **kwargs)
            file = open(path, 'a', encoding = 'utf-8')
            file.write(f'{datetime.now()} - function: {function.__name__} - arguments: {args} {kwargs} - result: {result}\n')       
            file.close()        
            return result        
        return new_func
    return logger