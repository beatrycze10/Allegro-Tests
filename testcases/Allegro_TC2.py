import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from common.driver_creation import Driver_Start

class Test(Driver_Start,unittest.TestCase):


    def css_elements(self):
    # finding elements by css 
        elem1 = self.driver.find_element_by_css_selector("a[data-analytics-click-value='Moda i uroda']")
        hover1 = ActionChains(self.driver).move_to_element(elem1)
        hover1.perform()
        elem1.click()
        wait = WebDriverWait(self.driver,1)
        
        elem2 = self.driver.find_element_by_css_selector("a.m-link[data-analytics-click-custom-index-0='0']")
        hover2 = ActionChains(self.driver).move_to_element(elem2)
        hover2.perform()
        elem2.click()
        
        elem3 = self.driver.find_element_by_css_selector("span[data-reactid='28']")
        hover3 = ActionChains(self.driver).move_to_element(elem3)
        hover3.perform()
        elem3.click()
        wait = WebDriverWait(self.driver,1)
        
        #checking breadcrumbs
        #checking the final element in breadcrumbs by means of inner text and printing it out
        elem3_check = self.driver.find_element_by_css_selector("h1[class='listing-title ']")
        
        
      
         
        
        



#if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
   # unittest.main()
    