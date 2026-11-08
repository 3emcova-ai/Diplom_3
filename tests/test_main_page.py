import allure

from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверяем переход на страницу «Лента Заказов»')
    @allure.description('Клик по кнопке «Лента Заказов» (с главной страницы) открывает страницу "Лента заказов"')
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        assert main_page.is_order_feed_opened()

    @allure.title('Проверяем переход на страницу «Конструктор»')
    @allure.description('Клик по кнопке «Конструктор» (со страницы Ленты заказов) открывает страницу "Конструктор"')
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        assert main_page.is_order_feed_opened()
        main_page.click_constructor_button()
        assert main_page.is_constructor_opened()

    @allure.title('Проверяем появления всплывающего окна с деталями при клике на ингредиент')
    @allure.description('Переключаемся на таб Соусы, кликаем соус «Традиционный галактический», октрылось модальное окно')
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_sauces_tab()
        main_page.click_galactic_sauce()
        assert main_page.is_ingredient_modal_opened(), "Модальное окно с деталями соуса не открылось"
 
    @allure.title('Проверяем закрытие всплывающего окна кликом на крестик')
    @allure.description('Открываем окно с деталями соуса, кликаем по крестику, модальное окно закрылось')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_sauces_tab()
        main_page.click_galactic_sauce()
        assert main_page.is_ingredient_modal_opened(), "Модальное окно с деталями соуса не открылось"
        main_page.click_modal_close_button()
        assert main_page.is_modal_closed(), "Модальное окно с деталями соуса не закрылось"

    @allure.title('Проверяем увеличение счетчика ингредиента при добавлении ингредиента')
    @allure.description('Перетаскиваем ингредиент в корзину, счетчик ингредиента увеличился')
    def test_add_ingredient_changes_counter(self, driver):
        main_page = MainPage(driver)
        main_page.drag_mineral_rings_to_basket()
        assert main_page.get_ingredient_counter_value() == '1', "Счетчик ингредиента не изменился"
        main_page.drag_mineral_rings_to_basket()
        assert main_page.get_ingredient_counter_value() == '2', "Счетчик ингредиента не изменился"
