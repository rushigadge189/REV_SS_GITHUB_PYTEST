
import time
import pyscreenshot
import pyautogui
from selenium import webdriver


class Test_02_live_screenshot():

    def test_02_ls(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get("https://www.instagram.com/") ;
        time.sleep(1) ;

        driver.save_screenshot("D:\PYTHON CT15\REV20\screenshots\\livess1.png") ;
        image=pyscreenshot.grab() ;
        image.show() ;
        image.save("livess1.png") ;


        driver.get("https://www.facebook.com/") ;
        time.sleep(5) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\livess2.png") ;
        image2 = pyautogui.screenshot() ;
        image2.show() ;
        image2.save("livess2.png") ;


        driver.close();
        assert True ;