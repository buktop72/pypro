from selenium import webdriver
import selenium
import time

def disk_login(user_login, password):
    result = False
    driver = webdriver.Chrome("C:\\bin\Chromedriver.exe")
    driver.get("https://passport.yandex.ru/auth/")
    time.sleep(3)

    element = driver.find_elements_by_name("login")
    element[0].send_keys(user_login)
    element[0].send_keys('\n')
    time.sleep(3)

    element = driver.find_elements_by_name("passwd")    
    element[0].send_keys(password)
    element[0].send_keys('\n')
    time.sleep(3)

    user_account = driver.find_element_by_class_name("user-account__name")
    if user_account:
        result = True
    time.sleep(3)
    driver.close()
    return result

if __name__ == '__main__':
    x = disk_login('userlogin', 'password')
    print(x)
