from selenium.webdriver.common.by import By

link = 'https://demoqa.com/'


def test_guest_should_see_elements_card_on_the_main_page(browser):
    browser.get(link)
    browser.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][.//h5[text()="Elements"]]')


def test_guest_should_see_join_now_button_on_the_main_page(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#join_now')
