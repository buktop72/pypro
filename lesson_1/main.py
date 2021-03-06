"""
1. Разработать структуру программы "Бухгалтерия".
main.py;
директория application:
-- salary.py;
-- директория db:
--- people.py;
main.py - основной модуль для запуска программы.
В модуле salary.py функция calculate_salary.
В модуле people.py функция get_employees.
2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
if __name__ == '__main__':
Сами функции реализовать не надо. Достаточно добавить туда какой-либо вывод.
3. Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
4. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции 
(необязательное задание)
"""

from datetime import date
from application import salary as s
from application.DB import people as p

def main():
    # print(dir(s),dir(p))
    print(date.today())
    s.calculate_salary()
    p.get_employees()

if __name__ == '__main__':
    main()


