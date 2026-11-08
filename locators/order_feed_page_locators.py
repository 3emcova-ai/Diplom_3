from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    AT_WORK_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
