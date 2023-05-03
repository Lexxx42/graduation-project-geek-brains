# PyTest — маркировка

## Маркировка тестов часть 1

При работе с большим количеством тестов может быть полезно распределить их по категориям, а не только по именам. Вот где
вступает в действие маркировка тестов. Отмечая тесты определенными категориями, такими как «smoke» для критических
тестов или «regression» для регрессионных тестов, выполняемых перед выпуском, мы можем выборочно запускать тесты на
основе их категории. Кроме того, у нас могут быть тесты, специфичные для определенного браузера, например Internet
Explorer 11, и мы можем захотеть запустить эти тесты только в этом браузере.
PyTest предоставляет тестовую маркировку или метки для
этой цели. Чтобы пометить тест, вы можете использовать декоратор, например @pytest.mark.mark_name, где «mark_name» —
любая выбранная вами строка.

Разделим тесты в одном из предыдущих примеров на smoke и regression.

> test_fixture8.py:

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print("smoke test")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("regression test")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
```

Вы можете выполнить тест с нужной меткой, передав параметр `-m`, а затем нужную метку в командной строке.

```shell
pytest -s -v -m smoke test_fixture8.py
```

Должен запуститься только тест с маркировкой smoke.

При этом вы увидите уведомление с предупреждениями:

<img src="img/marking_warnings.png" width="800" height="400" alt="marking warnings">

В последних версиях PyTest настоятельно рекомендуется явно регистрировать метки перед использованием, чтобы избежать
опечаток. Пометка теста несуществующей меткой может привести к тому, что он будет пропущен во время тестов. Вот почему
появляется предупреждение.

## Как регистрировать метки?

Создайте файл `pyproject.toml` в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

```
[tool.pytest.ini_options]

markers = [
    "smoke: marker for smoke tests",
    "regression: marker for regression tests"
]
```

Запустите тесты повторно, предупреждений быть не должно.

Маркировать можно не только методы, но и сразу целые классы. В этом случае маркоровка будет применена ко всем тестовым
методам этого класса.
