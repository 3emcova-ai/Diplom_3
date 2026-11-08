import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента на странице')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу (с обходом перекрытий)')
    def click_element_with_wait(self, locator):
        element = self.find_element_with_wait(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидание исчезновения элемента со страницы')
    def wait_for_element_invisible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
   
    @allure.step('Ожидание исчезновения оверлея модального окна')
    def wait_for_overlay_invisible(self):
        from locators.main_page_locators import MainPageLocators
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))
        except:
            pass

    def send_keys(self, locator, text):
        field = self.find_element_with_wait(locator)
        try:
            field.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", field)
        field.send_keys(text)

    @allure.step('Перетаскивание элемента (для Firefox)')
    def drag_and_drop_js(self, ingr_locator, basket_locator):
        self.find_element_with_wait(ingr_locator)
        self.find_element_with_wait(basket_locator)
        element_from = self.driver.find_element(*ingr_locator)
        element_to = self.driver.find_element(*basket_locator)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)
