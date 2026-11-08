import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение значения счетчика Выполнено за все время')
    def get_all_time_counter_value(self):
        element = self.find_element_with_wait(OrderFeedPageLocators.COUNTER_ALL_TIME)
        return int(element.text)
    
    @allure.step('Получение значения счетчика Выполнено за сегодня')
    def get_today_counter_value(self):
        element = self.find_element_with_wait(OrderFeedPageLocators.COUNTER_TODAY)
        return int(element.text)

    @allure.step('Ожидание появления заказа в разделе "В работе"')
    def wait_order_at_work_section(self, order_number):
        locator = (
            By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady')]//li[text()='{order_number}']"
        )
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
        