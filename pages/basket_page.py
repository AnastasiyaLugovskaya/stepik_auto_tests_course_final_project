from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), 'Нет текста о пустой корзине'

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_LIST), 'В корзине присутствуют товары'

    def should_be_empty_basket(self):
        self.should_be_empty_basket_message()
        self.should_not_be_product_in_basket()
