from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, 'i.icon-user')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a[href="/en-gb/basket/"]')


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p a')
    ITEM_LIST = (By.CSS_SELECTOR, '#basket_formset')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name = "registration_submit"]')
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3)>div>p")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_TITLE = (By.CSS_SELECTOR, "#content_inner article>div:first-child>div.product_main>h1")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3)>div>p>strong")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child div:nth-child(2)>strong")
    WATCH_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a[href='/ru/basket/']")
