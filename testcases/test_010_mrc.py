import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_010_mouserightclcik():

    def test_010_mouse_click_right(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;
        time.sleep(1) ;

        driver.get("https://demo.guru99.com/test/simple_context_menu.html") ;
        time.sleep(1) ;

        right_clcik=driver.find_element(By.XPATH, '//span[text()="right click me"]') ;

        action=ActionChains(driver) ;

        action.context_click(right_clcik).perform() ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_010_rightclick_pass2.png") ;

        driver.find_element(By.XPATH, '//span[contains(text(), "Quit")]').click() ;
        time.sleep(1) ;

        print("----------AFTER RIGHT CLICK TEXT----------") ;

        tetx1=Alert(driver).text ;
        print(tetx1) ;

        Alert(driver).accept() ;
        time.sleep(1) ;

        driver.close() ;
        assert True ;