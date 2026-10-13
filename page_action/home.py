from playwright.sync_api import Page


class Home:
    def __init__(self, page:Page):
        self.page = page

    def type_in_chat(self, input_text: str):
        input_element = self.page.get_by_placeholder("What would you like to know?")
        input_element.fill(input_text)

    def click_submit_button(self):
        button_element = self.page.get_by_role("button", name="submit")
        button_element.click()

    def click_cancel_button(self):
        button_element = self.page.get_by_text("cancel?")
        button_element.click()

    def click_retry_button(self):
        button_element = self.page.get_by_text("retry?")
        button_element.click()

    def click_link(self, link_text:str):
        a_elements = self.page.get_by_role("link")
        link_element = a_elements.get_by_text(link_text).first
        link_element.click()
