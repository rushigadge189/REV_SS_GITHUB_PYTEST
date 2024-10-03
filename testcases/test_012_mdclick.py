import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_012_mouse_double_click():

    def test_012_mouse_double_click(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://artoftesting.com/samplesiteforselenium") ;
        time.sleep(1) ;

        double_click=driver.find_element(By.XPATH, '//button[@id="dblClkBtn"]') ;
        time.sleep(1) ;

        action=ActionChains(driver) ;

        action.double_click(double_click).perform() ;
        time.sleep(1) ;

        text1=Alert(driver).text ;

        print("---------TEXT AFTER DOUBLE CLICK---------") ;
        print(text1) ;

        Alert(driver).accept() ;

        driver.close() ;
        assert True ;