import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_017_screenshots():

    def test_017_01_ss(self):

        driver=webdriver.Chrome() ;

        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get("https://opensource-demo.orangehrmlive.com/auth/login") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('Admin') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('admin123') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;
        time.sleep(1) ;

        if(driver.title=="OrangeHRM"):

            print("\n-----------WELCOME TO ORANGE HRM HOME PAGE---------\n") ;
            time.sleep(1) ;

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_017_ss_pass.png") ;

            driver.find_element(By.XPATH, '//span[@class="oxd-userdropdown-tab"]').click() ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//a[text()="Logout"]').click() ;
            time.sleep(1) ;

            driver.close();
            assert True ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_017_ss_fail.png") ;

            print("\n----------SORRY LOGIN IS NOT POSSIBLE DUE TO SOME ERROR\n")

            driver.close() ;
            assert False ;

    def test_017_addition(self):

        a=10 ;
        b=5 ;
        add=a+b ;
        if(add==15) :
            print("\n---------ADDITION IS SUCCESSFUL----------\n") ;
            print("\nADDITION = ",add) ;

            assert True;

        else:
            print("\nSORRY. ADDITION IS NOT POSSIBLE\n") ;
            assert False ;