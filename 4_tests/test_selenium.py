#Задача №3. Применив selenium, напишите unit-test для авторизации на Яндексе
import pytest
from selen import disk_login

class Test_Disk_login:
    def setup_class(self):
        print("method setup_class")
    def setup(self):
        print("method set_up")

    @pytest.mark.parametrize("login, password",[
        ('Pavel_Durov', 'Qwerty'),
        ('UserLogin', 'Pa$$w0rd')])
    def test_mkdir(self, login, password):  
        assert disk_login(login, password) == True, 'Неправильная пара логин-пароль!!!'
        print("Тест *Яндекс логин*")

    def teardown(self):
        print("teardown")
    def teardown_class(self):
        print("metod_teardown") 