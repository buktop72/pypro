import pytest
from secretary import * 

class Test_secretary:
    def setup_class(self):
        print("method setup_class")
    def setup(self):
        print("method set_up")

    @pytest.mark.parametrize("num, tp, name, shelf, result",[
        ('555', 'invoice', 'Петр Петров', '1', '1'),
        ('4567', 'passport', 'Иван Зуев', '3', '3'),
        ('234-54', 'insurance', 'Егор Быков', '4', '4')])
    def test_add_new_doc(self, num, tp, name, shelf, result):
        assert add_new_doc(num, tp, name, shelf) == result, 'Error'
        print("Тест *добавление нового документа*")

    @pytest.mark.parametrize("num, result", [
        ('555', '1'),
        ('4567', '3'),
        ('234-54', '4')])
    def test_get_doc_shelf(self, num, result):
        assert get_doc_shelf(num) == result, 'Error'
        print("Тест *номер полки документа*")

    @pytest.mark.parametrize("num, result",[
        ('555', 'Петр Петров'),
        ('4567', 'Иван Зуев'),
        ('234-54', 'Егор Быков')])    
    def test_get_doc_owner_name(self, num, result):
        assert get_doc_owner_name(num) == result, 'Error'
        print("Тест *владелец документа по его номеру*") 

    @pytest.mark.parametrize("num, result", [
        ('555', ('555', True)),
        ('4567', ('4567', True)),
        ('234-54', ('234-54', True))])
    def test_delete_doc(self, num, result):
        assert delete_doc(num) == result, 'Error'
        print("Тест *удаление документа*")

    def teardown(self):
        print("teardown")
    def teardown_class(self):
        print("metod_teardown")   






