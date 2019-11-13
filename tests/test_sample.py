# Ranorex Webtestit Test File

from utils.base_test import BaseTest
from pageobjects.main_po import MainPo


class TestSample(BaseTest):
    def test_sample_case(self):
        driver = self.get_driver()

        main_po = MainPo(driver)
        main_po.open("https://www.ranorex.com")

        self.assertTrue(main_po.get__test_automation_for_all_text(),
                        "Test Automation for All")
        """
        1. Arrange
        Create a new Page Object instance by right-clicking into
        the code editor and selecting "Instantiate Page Object"
        at the bottom of the context menu
        """
        """
        2. Act
        Call an existing action from your Page Object instance
        """
        """
        3. Assert
        Use unittest assertions to verify results.
        e.g.:
        self.assertEqual(title, "Test Automation for GUI Testing | Ranorex")
        """
