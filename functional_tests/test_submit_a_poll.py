import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SubmitAPollTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_question_for_poll(self):
        self.browser.get("http://localhost:8000")
        self.assertEqual(self.browser.title, 'Funny polls')
        self.assertEqual(self.browser.find_element('tag name', 'h1').text, "Funny polls")
        yes_radio_button = self.browser.find_element(value='ans1')
        yes_radio_button.send_keys(Keys.ENTER)
        submit_button = self.browser.find_element(value='save_poll')
        submit_button.send_keys(Keys.ENTER)

        # TODO verify the question, pie chart and total count





