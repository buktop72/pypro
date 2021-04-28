from wiki import wiki
from hash_summ import hash

# Задание № 1
wiki('countries.json')

# Задание № 2
hash_summ = hash('README.md')
for i in hash_summ:
    print(i)