#oluşturan: büşra şahin
#oluşturma tarihi: 01.05.2019

from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://www.amazon.com/")


sign_in = browser.find_element_by_id('nav-link-accountList')
sign_in.click()

username = browser.find_element_by_name("email")
password = browser.find_element_by_name("password")

username.send_keys("busra.sahin@useinsider.com")
password.send_keys("bsahininsider145")

login = browser.find_element_by_xpath("//*[@id='signInSubmit']")
login.click()

field_keywords = browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
field_keywords.click()
field_keywords.send_keys("Samsung")

submit = browser.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input")
submit.click()


if(browser.current_url.find("Samsung")>-1):

    submit = browser.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[7]/div/div/div/ul/li[3]/a")
    submit.click()
    if(browser.current_url.find("page=2")>-1):


        urun = browser.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
        urun.get_attribute("productTitle")
        urun.click()

        urun1 = browser.find_element_by_id('productTitle').text

        submit = browser.find_element_by_xpath("//*[@id='add-to-wishlist-button-submit']")
        submit.click()
        time.sleep(3)
        submit = browser.find_element_by_xpath("//*[@id='WLHUC_viewlist']/span/span")
        submit.click()


        urun2 = browser.find_element_by_css_selector('.a-size-base .a-link-normal').text


try:
        assert urun1 == urun2

        submit = browser.find_element_by_xpath("//*[@id='a-autoid-7']/span/input")
        submit.click()
        print("ürün silindi")
        time.sleep(5)

except Exception as e:
         print("Hatalı eşleşme")


time.sleep(5)
browser.close()






