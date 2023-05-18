import time

# webdriver - это набор команд для управления браузером.
from selenium import webdriver

# By - класс, который позволяет выбрать способ поиска элемента.
from selenium.webdriver.common.by import By

# Инициализация браузера Chrome.
driver = webdriver.Chrome()

# Задержка в 5 секунд, чтобы вы увидили, что происходит в браузере.
# Попробуйте её закомментировать и посмотреть, что из этого выйдет.
time.sleep(5)

# Метод get открывает страницу в браузере.
driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
time.sleep(5)

# Метод find_element() позволяет найти нужный элемент на сайте по указанному локатору (селектору).
# Метод принимает в качестве аргументов способ поиска элемента и значение, по которому будет осуществляться поиск.
# Ищем поле ввода.
username_field = driver.find_element(By.CSS_SELECTOR, '[name="username"]')

# Вводим текст в поле, используя метод send_keys().
username_field.send_keys('Alexander')
time.sleep(5)

# Найдем кнопку, которая отправляет введённый текст.
submit_button = driver.find_element(By.CSS_SELECTOR, '[value="submit"]')

# Скажем драйверу, что нужно кликнуть по кнопке.
# После этой команды мы должны увидеть ввёденные значения в форму.
submit_button.click()
time.sleep(5)

# Мы должны не забыть закрыть окно браузера, но если этого не сделать, то за нас это сделает сборщик мусора Python.
driver.quit()
