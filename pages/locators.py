from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    WATCH_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a[href='/ru/basket/']")
    BOOK_TITLE = (By.CSS_SELECTOR, "#content_inner article>div:first-child>div.product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child div:nth-child(2)>strong")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3)>div>p")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3)>div>p>strong")
