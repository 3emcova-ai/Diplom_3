import allure

from data import UserData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeedPage:

    @allure.title('Проверяем увеличение счетчика "Выполнено за все время" при создании заказа')
    @allure.description('Логинимся, создаем заказ, переходим в Ленту заказов, счетчик за все время увеличился.')
    def test_all_time_counter_changes_after_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_order_feed_button()
        assert main_page.is_order_feed_opened(), "Не удалось открыть Ленту заказов"
        old_value = order_feed_page.get_all_time_counter_value()
        login_page.login(UserData.EMAIL, UserData.PASSWORD)
        main_page.click_constructor_button()
        main_page.create_order_and_get_number()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_all_time_counter_change(old_value)
        new_value = order_feed_page.get_all_time_counter_value()
        assert new_value > old_value, "Счетчик 'Выполнено за все время' не увеличился"

    @allure.title('Проверяем увеличение счетчика "Выполнено за сегодня" при создании заказа')
    @allure.description('Логинимся, создаем заказ, переходим в Ленту заказов, счетчик за сегодня увеличился.')
    def test_today_counter_changes_after_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_order_feed_button()
        assert main_page.is_order_feed_opened(), "Не удалось открыть Ленту заказов"
        old_value = order_feed_page.get_today_counter_value()
        login_page.login(UserData.EMAIL, UserData.PASSWORD)
        main_page.click_constructor_button()
        main_page.create_order_and_get_number()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_today_counter_change(old_value)
        new_value = order_feed_page.get_today_counter_value()
        assert new_value > old_value, "Счетчик 'Выполнено за сегодня' не увеличился."  

    @allure.title('Проверяем появление номера заказа в разделе «В работе»')
    @allure.description('Создаем заказ, запоминаем номер, проверяем отображение в разделе «В работе»')
    def test_order_added_at_work_section(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page.login(UserData.EMAIL, UserData.PASSWORD)
        main_page.click_constructor_button()
        raw_number = main_page.create_order_and_get_number() 
        formatted_number = f"{int(raw_number):06d}"
        main_page.click_order_feed_button()
        assert main_page.is_order_feed_opened(), "Не удалось открыть Ленту заказов"
        assert order_feed_page.wait_order_at_work_section(formatted_number), \
            f"Заказ не появился в разделе 'В работе'"
              