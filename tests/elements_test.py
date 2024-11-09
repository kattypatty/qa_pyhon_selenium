import time
from pages.elements_page import TextBoxPage
from pages.base_page import BasePage

class TestElements:

    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open_url()

            # full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # output_full_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_fields()
            # assert full_name == output_full_name
            # assert email == output_email
            # assert current_address == output_cur_address
            # assert permanent_address == output_per_address

            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_fields()
            assert input_data == output_data
            time.sleep(10)

