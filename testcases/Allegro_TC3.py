import unittest
from argparse import Action
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from common.driver_creation import Driver_Start

search_text = "converse"


class Test(Driver_Start,unittest.TestCase):


    def add_to_cart(self):
        main_searchbox = self.driver.find_element_by_id("main-search-text")
        hover = ActionChains(self.driver).move_to_element(main_searchbox)
        main_searchbox.click()
        main_searchbox.send_keys(search_text)
        submitt_button = self.driver.find_element_by_class_name("sprite.search-btn")
        submitt_button.click()
        wait = WebDriverWait(self.driver,1)
        item = self.driver.find_element_by_class_name("ecdefa6")
        item.click()
        wait = WebDriverWait(self.driver,1)
        cart = self.driver.find_element_by_id("add-to-cart").click()
        wait = WebDriverWait(self.driver,2)
        close = self.driver.find_element_by_xpath("//button[@type='button']")
        wait = WebDriverWait(self.driver,5)
        hover = ActionChains(self.driver).move_to_element(close)
        wait = WebDriverWait(self.driver,2)
        refresh = self.driver.get("https://allegro.pl/")
        wait = WebDriverWait(self.driver,1)
        screenshot = self.driver.save_screenshot('cart.png')
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    

    unittest.main()
    
