import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_007_explicit_wait():

    def test_007_exp_wait(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1);

        driver.implicitly_wait(5) ;

        driver.get('https://www.google.co.in/') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//textarea[@aria-controls="Alh6id"]').send_keys('Internet Speed Test') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[1]').click() ;
        time.sleep(1);

        driver.find_element(By.XPATH, '(//div[@class="lv7K9c"])[1]').click() ;
        time.sleep(1);

        try:
            wait=WebDriverWait(driver, 30, poll_frequency=0.5) ;
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '(//div[@class="lv7K9c"])[3]'))) ;

            time.sleep(2) ;
            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_007_exp_wait_pass.png") ;

            print("\n***********INTERNET  DOWNLOAD SPEED***********") ;
            uplaodspeed=driver.find_element(By.XPATH, '//div[@class="oyUhj"]').text ;
            print(uplaodspeed) ;

            print("\n*********INTERNET UPLOAD SPEED**********") ;
            downloadspeed=driver.find_element(By.XPATH, '//div[@class="iD3Ij"]').text ;
            print(downloadspeed) ;

            driver.close() ;
            assert True ;

        except :

            print("\n**********SOORY, SOME ERROR OCCURED***********") ;

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_007_exp_wait_fail.png") ;

            driver.close() ;
            assert False ;