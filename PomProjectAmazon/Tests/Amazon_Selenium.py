from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PomProjectAmazon.Pages.LoginPage import LoginPage
from PomProjectAmazon.Locators.Locators import Locators


driver = webdriver.Chrome('C:/Users/User/Desktop/Webdriver/chromedriver.exe')
driver.get('https://www.amazon.com/')


def wait(by, zaman):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, zaman)))


driver.find_element_by_id('nav-link-accountList').click()


class LoginTest(unittest.TestCase):

    def test_login_valid(self):
        login = LoginPage(driver)
        login.driver.enter_mail("busra.sahin@useinsider.com")
        login.enter_password("bsahininsider145")
        login.click_login()


def search(arama):
    assert search_term, arama


search_term = driver.find_element_by_id('nav-input').text
search('"Samsung"')
driver.find_element_by_css_selector(Locators.search_text).click()
driver.input_click.click()

assert driver.find_element_by_css_selector.text, '2'

product1 = driver.product_element_text[2]
product_name = product1.text
product1.click()

driver.wishlist_button.click()

wait(By.CSS_SELECTOR, '.hucInfoTable a')

driver.icon_click.click()

hover_element = wait(By.ID, 'nav-link-accountList')
hover = ActionChains(driver).move_to_element(hover_element)
hover.perform()

wait(By.LINK_TEXT, 'Shopping List').click()

product2 = driver.product2_text.text

assert product_name, product1
driver.delete_click.click()

driver.close()
