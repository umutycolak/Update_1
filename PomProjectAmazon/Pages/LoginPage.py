from PomProjectAmazon.Locators.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.mail_textbox_id = Locators.mail_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id

    def enter_mail(self, mail):
        self.driver.find_element_by_id()(Locators.mail_textbox_id).sendkeys(mail)

    def enter_password(self, password):
        self.driver.find_element_by_id()(Locators.password_textbox_id).sendkeys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()
