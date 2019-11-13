# Ranorex Webtestit Page Object File

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPo:
    # Additional data: {"img":"screenshots/004d81ec-a409-83e5-562c-7ca68d290b81.png"}
    _test_automation_for_all = (By.CSS_SELECTOR, "main h1")
    """
    NOTE: Use Ranorex Selocity or the Elements Panel to generate element code
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    def get__test_automation_for_all_text(self):
        _test_automation_for_all_text = self.wait.until(
            EC.visibility_of_element_located(
                self._test_automation_for_all)).text

        return _test_automation_for_all_text

    """
    NOTE: Drag elements from the Elements panel into the code editor to
    generate methods. Drag elements into existing methods to add steps.
    """
