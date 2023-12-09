import pytest
from .pages.product_page import ShellcodersHandbookPage


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ShellcodersHandbookPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code_for_parametrize()
    page.book_title_should_be_in_message()
    page.basket_cost_should_be_equal_to_product_price()
