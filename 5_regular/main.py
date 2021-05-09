"""
Домашнее задание к лекции 5.«Regular expressions»
Ваша задача: починить адресную книгу, используя регулярные выражения.
Структура данных будет всегда:
lastname,firstname,surname,organization,position,phone,email
Предполагается, что телефон и e-mail у человека может быть только один.
Необходимо:
поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. 
В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой:
 +7(999)999-99-99 доб.9999;
"""
import re
from pprint import pprint
import csv

def read_book(path): # читаем адресную книгу в формате CSV в список contacts_list
    with open(path, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

# TODO 1: выполните пункты 1-3 ДЗ
def edit_book(contacts_list): # причесываем адресную книгу
    phone_book = []     
    title = contacts_list.pop(0)
    for i in contacts_list:
        ls = []
        # ФИО
        pattern = r'(\b[А-Я]\w+)'
        text = ' '.join(i)
        x = re.findall(pattern, text)
        if len(x) >= 3 :
            ls.append(x[0])
            ls.append(x[1])
            ls.append(x[2])
        else:
            x.append(' ')
            ls.append(x[0])
            ls.append(x[1])
            ls.append(x[2])    
        item = i[3] # organization
        ls.append(item)
        item = i[4] # position 
        ls.append(item)    
        item = i[5] # phone   
        pattern = "(\+7|8)+\s*\(?(\d{3})\)?(-*|\s*|.*)(\d{3})(-*|)(\d{2})-*(\d{2})"
        phone = re.sub(pattern, r"+7(\2)\4-\6-\7", item)
        pattern = "\(*(доб\.)\s(\d+)\)*"
        phone = re.sub(pattern, r"\1\2", phone)    
        ls.append(phone)    
        item = i[6] # email
        ls.append(item)
        phone_book.append(ls)
    return phone_book, title

def duble_dict(ls): # ф-я принимает список, возвращает словарь с дублями: {'Мартиняхин': 2, 'Лагунцов': 2}
    d = {}
    for i in ls: # считаем количество вхождений каждого элемета списка
        key = i[0]
        if key in d:
            d[key] += 1
        else:
            d[key] = 1    
    d_double = {} 
    for k, v in d.items(): # Оставляем только повторяющиеся данные
        if v > 1:
            d_double[k] = v
    return d_double

def list_summ(ls1,ls2):  # ф-я принимает 2 списка и объединяет: [a,b,] + [,,c] => [a,b,c]
    ls_summ = []
    for i in range(len(ls1)):
        if ls1[i] >= ls2[i]:
            ls_summ.insert(i, ls1[i])
        elif ls1[i] < ls2[i]:
            ls_summ.insert(i, ls2[i])    
    return ls_summ

def list_united(d, phone_book):# ф-я принимает словарь дублей и список, возвращает список новых (объединенных) списков
    ls_new = []
    for i in d.keys(): 
        ls = []        
        for j in phone_book: 
            if i in j:                
                ls.append(j)
        ls_new.append(list_summ(ls[0],ls[1]))  
    return ls_new

def del_double(dd, phone_book): # удаляем все строки упомянутые в словаре дублей     
    for i in phone_book:    
        for j in dd.keys():
            if j in i:
                phone_book.remove(i)
    for i in phone_book:    # еще один проход, с первого раза все удаляется ¯\_(ツ)_/¯
        for j in dd.keys():
            if j in i:
                phone_book.remove(i)

# TODO 2: сохраните получившиеся данные в другой файл
def write_book(path, phone_book, title): # запись книги в файл
    phone_book.insert(0, title)
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')  
        datawriter.writerows(phone_book)

# чтение файла в contacts_list:
path = "phonebook_raw.csv"
contacts_list = read_book(path)
# редактируем, получаем красивую книгу и отдельно титульник:
phone_book, title = edit_book(contacts_list)
# получаем дубли в виде словаря
dd = duble_dict(phone_book) 
# сложение повторяющихся списков
ls_new = list_united(dd, phone_book) 
# удаление дублей
del_double(dd, phone_book) 
# добавляем объединенные списки вместо повторяющихся неполных
for i in ls_new:    
    phone_book.append(i)
# записываем новую книгу в файл:
phone_book.sort()
path = "phonebook.csv"
write_book(path, phone_book, title)

