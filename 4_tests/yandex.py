import requests
from pprint import pprint
class YaDisk:
    # Создание списка уже существующих папок (ls_dir):
    def list_dir(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': '/'}
        with open('ya_token.txt') as f:
            self.token = f.read().strip()
        headers = {"Authorization": self.token}
        resp = requests.get(url, params=params, headers=headers)        
        ls_dir = []
        for i in resp.json()['_embedded']['items']:
            ls_dir.append(i['name'])
        return ls_dir
    # создание папки
    def mk_dir(self, dir, ls_dir):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": dir}
        # получаем токен яндекс-диск из файла:
        with open('ya_token.txt') as f:
            self.token = f.read().strip()
        headers = {"Authorization": self.token}
        resp = requests.put(url, params=params, headers=headers)
        return(resp.status_code)

if __name__ == '__main__':
    dir_name = 'Test_dir' # имя создаваемой папки
    up_disk =YaDisk() # экземпляр класса YaDisk
    ls_dir = up_disk.list_dir() # список существующих папок и файлов
    up_disk.mk_dir(dir_name, ls_dir) # создание папки
