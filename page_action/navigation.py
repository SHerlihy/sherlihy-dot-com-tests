from playwright.sync_api import Page

class Navigation:
    def __init__(self, page:Page):
        self.page = page

    def click_navigate_button(self):
        to_open = self.page.get_by_role("button", name="Open navigation button.")
        if to_open.count() > 0:
            to_open.click()
            return

        to_close = self.page.get_by_role("button", name="Close navigation button.")
        to_close.click()

    def click_link_with_text(self, text: str):
        all_links = self.page.get_by_role('link')
        all_links.get_by_text(text).click()

    def click_info_copy_button(self, key_information:str):
        key_information_element = self.page.get_by_text(key_information).first

        key_information_element.locator(
            "xpath=following::*[self::button][1]"
        ).click()
