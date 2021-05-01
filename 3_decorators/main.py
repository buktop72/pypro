"""
1.Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, 
с которыми вызвалась и возвращаемое значение.
2.Написать декоратор из п.1, но с параметром – путь к логам.
3.Применить написанный логгер к приложению из любого предыдущего д/з.
"""
from logger import logger
from logger_path import logger_path

@logger
def fibonachi(n):
    ls = [0 , 1]
    for i in range(n):
        ls.append(ls[i]+ ls[i+1])        
    return ls[n]

@logger_path('logs2.txt')
def sqrt(a :float, b :float, c :float):
    result = []
    d = b**2 - 4*a*c        
    if d >= 0:
        x1 = (-1*b + d**0.5) / (2*a)              
        result.append(x1)
        x2 = (-1*b - d**0.5) / (2*a)
        result.append(x2)                 
    return result

if __name__ == '__main_':
    main()

# последовательность Фибоначи (последний элемент) (logs.txt)
fibonachi(200)
# нахождение корней квадратного уравнения (logs2.txt)
sqrt(3, 8, -11)











