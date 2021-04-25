from application import *
from application.DB import *

calc = salary.calculate_salary
get = people.get_employees

def dirty():
    # print(dir(salary))
    # print(dir(people))
    # salary.calculate_salary()   
    # people.get_employees()
    calc()
    get()

if __name__ == '__main__':
    dirty()
