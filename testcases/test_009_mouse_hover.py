import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_009_mouse_hover_demo():

    def test_mousehoverdemo(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://stqatools.com/demo/MouseHover.php") ;
        time.sleep(1) ;

        action = ActionChains(driver) ;

        hover_tab=driver.find_element(By.XPATH, '//button[@class="dropbtn"]') ;

        action.move_to_element(hover_tab).perform();
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_009_mousehover_pass.png") ;

        driver.find_element(By.XPATH, "//a[normalize-space()='Link 2']").click() ;
        time.sleep(1) ;

        text1=driver. find_element(By.XPATH, '//div[@class="modal-content"]').text ;
        print("-----------AFTER HOVER-----------\n") ;
        print(text1) ;

        driver.close() ;
        assert True ;