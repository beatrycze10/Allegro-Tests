import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from argparse import Action
from common.driver_creation import Driver_Start

class Test(Driver_Start,unittest.TestCase):


    def category_verification(self):
        
        # finding elements by Xpath
        elem1 = self.driver.find_element_by_xpath("//a[@href='https://allegro.pl/dzial/elektronika']")
        hover1 = ActionChains(self.driver).move_to_element(elem1)
        hover1.perform()
        elem1.click()
        wait = WebDriverWait(self.driver,1)
        
        elem2 = self.driver.find_element_by_xpath("//a[@href='/kategoria/rtv-i-agd']")
        hover2 = ActionChains(self.driver).move_to_element(elem2)
        hover2.perform()
        elem2.click()
    
        elem3 = self.driver.find_element_by_xpath("//a[@href='https://allegro.pl/kategoria/agd-do-zabudowy-67524']")
        hover3 = ActionChains(self.driver).move_to_element(elem3)
        hover3.perform()
        elem3.click()
        wait = WebDriverWait(self.driver,1)
        
        #checking breadcrumbs
        elem1_check = self.driver.find_element_by_xpath("//a[@href='/dzial/elektronika']")
        elem2_check = self.driver.find_element_by_xpath("//a[@href='/kategoria/rtv-i-agd']")
        
        #checking the final element in breadcrumbs and printing it out
        elements = []
        for elem in self.driver.find_elements_by_xpath('.//span[@itemprop = "name"]'):
                a = elements.append(elem.text)
        print elements[3]
         
        # creating a condition, if true then print out the sentence in the console       
        if elements[3] == 'AGD do zabudowy':
            print "Product category and sub-categories are visible in breadcrumbs on the web page."
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()