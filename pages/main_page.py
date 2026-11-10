import allure

from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button(self):
        self.click_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке Лента Заказов')
    def click_order_feed_button(self):
        self.click_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверка открытия Конструктора')
    def is_constructor_opened(self):
        return self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_TITLE).is_displayed()

    @allure.step('Проверка открытия Ленты заказов')
    def is_order_feed_opened(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_TITLE).is_displayed()

    @allure.step('Клик по табу Соусы')
    def click_sauces_tab(self):
        self.click_element_with_wait(MainPageLocators.SAUCES_TAB)

    @allure.step('Клик по соусу Традиционный галактический')
    def click_galactic_sauce(self):
        self.click_element_with_wait(MainPageLocators.SAUCE_GALACTIC)

    @allure.step('Проверка открытия модального окна Детали ингредиента (Соус Традиционный галактический)')
    def is_ingredient_modal_opened(self):
        return self.find_element_with_wait(MainPageLocators.MODAL_SAUCE_GALACTIC).is_displayed()

    @allure.step('Клик по крестику в модальном окне')
    def click_modal_close_button(self):
        self.click_element_with_wait(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Проверка закрытия модального окна')
    def is_modal_closed(self):
        return self.wait_for_element_invisible(MainPageLocators.MODAL_SAUCE_GALACTIC)

    @allure.step('Перетаскивание ингредиента "Хрустящие минеральные кольца" в корзину')
    def drag_mineral_rings_to_basket(self):
        self.drag_and_drop_js(
            MainPageLocators.INGREDIENT_MINERAL_RINGS,
            MainPageLocators.BURGER_BASKET
        )

    @allure.step('Получение значения счетчика ингредиента')
    def get_ingredient_counter_value(self):
        element = self.find_element_with_wait(MainPageLocators.COUNTER_MINERAL_RINGS)
        return element.text

    @allure.step('Создание заказа и получение номера заказа')
    def create_order_and_get_number(self):
        self.drag_and_drop_js(MainPageLocators.BUN_KRATOR, MainPageLocators.BURGER_BASKET)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON)
        self.find_element_with_wait(MainPageLocators.MODAL_ORDER_SUCCESS)
        self.wait_for_text_length(MainPageLocators.ORDER_NUMBER_TEXT, length=5)
        order_number = self.find_element_with_wait(MainPageLocators.ORDER_NUMBER_TEXT).text.strip()
        self.click_element_with_wait(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_overlay_invisible()
        return order_number
        