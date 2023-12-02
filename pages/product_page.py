from .base_page import BasePage
from .locators import ProductPageLocators


class ShellcodersHandbookPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Кнопка 'Добавить в корзину' не найдена"

    def basket_cost_should_be_equal_to_product_price(self):
        self.should_be_successful_message()
        cost = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert cost == price, f"Цены не совпадают! Стоимость корзины = {cost}, цена товара = {price}"

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_successful_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            "Нет сообщения об успешном добавлении товара"

    def book_title_should_be_in_message(self):
        self.should_be_successful_message()
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_MESSAGE).text
        assert title in message, "Название книги не содержится в сообщении"

    def should_be_basket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), \
            "Нет сообщения о стоимости корзины"
