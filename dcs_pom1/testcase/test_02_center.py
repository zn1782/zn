
from public.pages.BasePage import BasePage
from public.pages.pages_element import Pages_Element as p

class User_Center(BasePage):

    @classmethod
    def setUpClass(cls) -> None:
        BasePage.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        BasePage.sleep(1)

    def test_02_user_center(self):
        elem = BasePage.find_element(p.user_center)
        BasePage.click(elem)
        BasePage.sleep(2)
        elem2 = BasePage.find_element(p.user_manager)
        BasePage.click(elem2)
        BasePage.sleep(1)
        elem2 = BasePage.find_element(p.iframe)
        BasePage.frame(elem2)
        BasePage.sleep(2)
        elem3 = BasePage.find_element(p.user_add)
        BasePage.click(elem3)
