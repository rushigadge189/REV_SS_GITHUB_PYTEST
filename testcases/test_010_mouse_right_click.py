import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_010_right_click_mouse():

    def test_010_right_clcik(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://vinothqaacademy.com/mouse-event/") ;
        time.sleep(1) ;

        right_clcik=driver. find_element(By.XPATH, '//button[@id="rightclick"]') ;

        action=ActionChains(driver) ;

        action.context_click(right_clcik).perform() ;
        time.sleep(1) ;

        driver.execute_script("window.scrollBy(0,1000)");
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_010_rightclick_pass.png") ;

        text1=driver.find_element(By.XPATH, '//div[@id="myDiv"]').text ;
        print("------------TEXT AFTER RIGHT CLICK-----------1") ;
        print(text1) ;

        driver.close();
        assert True ;
