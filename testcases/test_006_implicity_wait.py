import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_006_impl_wait():

    def test_006_implicit_wait(self):

        driver=webdriver.Chrome()
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(30) ;

        driver.get("https://www.google.co.in/") ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//textarea[@aria-label="Search"]').send_keys("INTERNET SPEED TEST") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[1]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//div[@class="lv7K9c"])[1]').click() ;
        time.sleep(25) ;

        downloadspeed=driver.find_element(By.XPATH,'//div[@class="oyUhj"]').text ;
        print("\n**********INTERNET DOWNLOAD SPEED**********") ;
        print(downloadspeed) ;

        uplaodspeed=driver.find_element(By.XPATH, '//div[@class="iD3Ij"]').text
        print("\n*********INTERNET UPLOAD SPEED**********") ;
        print(uplaodspeed) ;

        driver.save_screenshot("D:\PYTHON CT15\REV20\screenshots\\test_006_implicit_wait_pass.png") ;
        driver.close() ;

