from wiki import Wiki
from hash_summ import hash

# Задание № 1
x = Wiki('countries.json')
for i in x:
    url = f'https://en.wikipedia.org/wiki/{i["name"]["common"]}' 
    ls = url.split()
    url = ('_').join(ls)           
    out_file = open('out.txt', 'a', encoding = 'utf-8')
    out_file.write(f'{i["name"]["common"]:45} - {url}\n')       
    out_file.close() 
    
# Задание № 2
hash_summ = hash('README.md')
for i in hash_summ:
    print(i)
