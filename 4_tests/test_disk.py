# Задача №2 Автотест API Яндекса
import pytest
from yandex import YaDisk

class Test_Yadisk:
    def setup_class(self):
        print("method setup_class")
    def setup(self):
        print("method set_up")

    @pytest.mark.parametrize("dir_name",[
        ('Test_dir'),
        ('New_dir'),
        ('')])
    def test_mkdir(self, dir_name):               
        up_disk =YaDisk() # экземпляр класса YaDisk
        ls_dir = up_disk.list_dir() # список существующих папок и файлов        
        assert up_disk.mk_dir(dir_name, ls_dir) == 201, 'Ошибка создания папки!!!'
        print("Тест *создание папки*")

    def teardown(self):
        print("teardown")
    def teardown_class(self):
        print("metod_teardown")   



