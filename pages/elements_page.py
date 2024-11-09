import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):

        # filling the visible fields
        # next() means only one iteration per field
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\r\n", " ").replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\r\n", " ").replace("\n", " ")

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    def check_filled_fields(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1].replace("\r\n", " ").replace("\n", " ")
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1].replace("\r\n", " ").replace("\n", " ")

        return full_name, email, current_address, permanent_address





