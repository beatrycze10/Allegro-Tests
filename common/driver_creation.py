
import unittest
from selenium import webdriver


class Driver_Start(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://allegro.pl/")
        self.driver.maximize_window()
        assert "Allegro" in self.driver.title


    def tearDown(self):
        self.driver.quit()


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()