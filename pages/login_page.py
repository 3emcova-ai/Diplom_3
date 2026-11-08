import allure

from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вход в личный кабинет')
    def login(self, email, password):
        self.click_element_with_wait(MainPageLocators.ACCOUNT_BUTTON)
        self.send_keys(LoginPageLocators.EMAIL_FIELD, email)
        self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element_with_wait(LoginPageLocators.LOGIN_BUTTON)
