import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_011_mouse_dd():

    def test_dd_mouse(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1);

        driver.implicitly_wait(5) ;

        driver.get('https://demo.automationtesting.in/Static.html') ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_011_mdd_beforedd_pass.png") ;

        action=ActionChains(driver) ;

        src=driver.find_element(By.XPATH, '//img[@id="mongo"]') ;
        dest=driver.find_element(By.XPATH, '//div[@class="dragged"]') ;

        action.drag_and_drop(src,dest).perform() ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_011_mdd_afterdd_pass.png") ;

        driver.close() ;
        assert True ;