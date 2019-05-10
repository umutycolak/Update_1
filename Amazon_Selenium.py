#oluşturan: büşra şahin
#oluşturma tarihi: 01.05.2019
#guncelleme tarihi: 10.05.2019

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Firefox()

browser.get("https://www.amazon.com/")

browser.find_element_by_id('nav-link-accountList').click()

browser.find_element_by_name("email").send_keys("busra.sahin@useinsider.com")
browser.find_element_by_name("password").send_keys("bsahininsider145")

browser.find_element_by_id('signInSubmit').click()

browser.find_element_by_id('twotabsearchtextbox').send_keys("Samsung")

browser.find_element_by_css_selector('.nav-input').click()

search_term = browser.find_element_by_css_selector('.a-text-bold').text
assert search_term, '"Samsung"'
browser.find_element_by_css_selector('.a-normal a').click()

assert browser.find_element_by_css_selector('.a-selected a').text, '2'

product1 = browser.find_elements_by_css_selector('.a-link-normal .a-text-normal')[2]
product_name = product1.text
product1.click()

browser.find_element_by_id('add-to-wishlist-button-submit').click()

WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".hucInfoTable a")))

browser.find_element_by_css_selector('.a-icon.a-icon-close').click()

element_to_hover_over = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-link-accountList')))
hover = ActionChains(browser).move_to_element(element_to_hover_over)
hover.perform()

WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Shopping List'))).click()

product2 = browser.find_element_by_css_selector('.a-size-base .a-link-normal').text

try:
        assert product_name == product1

        submit = browser.find_element_by_id('a-autoid-7').click()
        print("ürün silindi")
        time.sleep(4)
except Exception as e:
    print("Hatalı eşleşme")

browser.close()