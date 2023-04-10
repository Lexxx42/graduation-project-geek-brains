# Поиск элементов с помощью Selenium WebDriver

## Поиск элементов с помощью Selenium

Для поиска элементов на странице в Selenium WebDriver используются несколько стратегий, позволяющих искать по атрибутам
элементов, текстам в ссылках, CSS-селекторам и XPath-селекторам. Для поиска Selenium предоставляет метод find_element,
который принимает два аргумента - тип локатора и значение локатора. Существуют следующие методы поиска элементов:

+ `find_element(By.ID, value)` - поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем
  элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он
  наиболее стабильный;
+ `find_element(By.CSS_SELECTOR, value)` - поиск элемента с помощью правил на основе CSS. Это универсальный метод
  поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если
  find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот
  метод в ваших тестах;
+ `find_element(By.XPATH, value)` - поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск
  элементов;
+ `find_element(By.NAME, value)` - поиск по атрибуту name элемента;
+ `find_element(By.TAG_NAME, value)` - поиск элемента по названию тега элемента;
+ `find_element(By.CLASS_NAME, value)` - поиск по значению атрибута class;
+ `find_element(By.LINK_TEXT, value)` - поиск ссылки на странице по полному совпадению;
+ `find_element(By.PARTIAL_LINK_TEXT, value)` - поиск ссылки на странице, если текст селектора совпадает с любой частью
  текста ссылки.

Например, мы хотим найти кнопку со значением id="submit_button":

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit")
```

Обратите внимание, что мы импортировали класс By, который содержит все возможные локаторы.

Если страница у вас загрузилась, но дальше ничего не происходит, вернитесь обратно в консоль, в которой вы запускали ваш
скрипт. Скорее всего, вы увидите там ошибку NoSuchElementException. Она будет выглядеть следующим образом:

```
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element:
{"method":"id","selector":"submit"}
```

Ошибка очевидна: мы неправильно указали локатор — значит, кнопки с таким id на странице нет.

Исправим локатор, чтобы наш код проходил без ошибок:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
```

### Поиск нескольких элементов

Вы можете столкнуться с ситуацией, когда на странице будет несколько элементов, подходящих под заданные вами параметры
поиска. В этом случае WebDriver вернет вам только первый элемент, который встретит во время поиска по HTML. Если вам
нужен не первый, а второй или следующие элементы, вам нужно либо задать более точный селектор для поиска, либо
использовать методы `find_elements`, которые мы рассмотрим чуть позже.

