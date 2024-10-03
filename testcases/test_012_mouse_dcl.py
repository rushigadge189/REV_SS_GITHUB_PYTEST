import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_012_mouse_double_clcik():

    def test_012_mousedoubleclcik(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://demo.guru99.com/test/simple_context_menu.html") ;
        time.sleep(1) ;

        double_clcik=driver.find_element(By.XPATH, '//button[@ondblclick="myFunction()"]') ;
        time.sleep(1) ;

        action=ActionChains(driver) ;

        action.double_click(double_clcik).perform() ;
        time.sleep(1) ;

        print("\n----------TEXT AFTER DOUBLE CLICK----------\n") ;
        text1=Alert(driver).text ;
        print(text1) ;

        Alert(driver).accept() ;
        time.sleep(1) ;

        driver.close();
        assert True ;




