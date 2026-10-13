from playwright.sync_api import Page

class Navigation:
    def __init__(self, page:Page):
        self.page = page

    def click_navigate_button(self):
        to_open = self.page.get_by_role("button", name="Open navigation button.")
        if to_open != None:
            to_open.click()
            return

        to_close = self.page.get_by_role("button", name="Close navigation button.")
        if to_close != None:
            to_close.click()

    def click_button_with_text(self, text: str):
        all_buttons = self.page.get_by_role('button')
        all_buttons.get_by_text(text).click()
