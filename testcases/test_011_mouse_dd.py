import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_011_darag_drop_mouse():

    def test_011_mouse_darag_drop(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get('https://vinothqaacademy.com/mouse-event/') ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_011_before_dd_pass.png") ;

        action=ActionChains(driver) ;

        src=driver.find_element(By.XPATH, '//div[@id="draggableElement"]') ;
        dest=driver.find_element(By.XPATH, '//div[@id="droppableElement"]');

        action.drag_and_drop(src,dest).perform() ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_011_after_dd_pass.png") ;

        driver.close() ;
        assert True ;