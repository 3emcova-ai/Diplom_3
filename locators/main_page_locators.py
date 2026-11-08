from selenium.webdriver.common.by import By


class MainPageLocators:
    
    #шапка сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    #раздел Соберите бургер
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    BURGER_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")

    #ингредиенты
    SAUCE_GALACTIC = (By.XPATH, "//p[text()='Соус традиционный галактический']")
    INGREDIENT_MINERAL_RINGS = (By.XPATH, "//p[text()='Хрустящие минеральные кольца']/ancestor::a")
    COUNTER_MINERAL_RINGS = (By.XPATH, "//p[text()='Хрустящие минеральные кольца']/ancestor::a//p[contains(@class, 'counter__num')]")
    
    #модальное окно
    MODAL_SAUCE_GALACTIC = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[text()='Соус традиционный галактический']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    
    #страница Лента заказов
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    