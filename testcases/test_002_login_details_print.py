import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_002_details_print():

    def test_002_luma_details(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1);

        driver.implicitly_wait(5) ;

        driver.get("https://magento.softwaretestingboard.com/");
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//a[contains(text(), "Sign In")])[1]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="login[username]"]').send_keys("rushabhgadge@gmail.com") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@type="password"])[1]').send_keys("Rushabh@1995") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//span[text()="Sign In"]').click();
        time.sleep(1) ;

        if(driver.title=="Home Page"):
            time.sleep(1) ;
            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_002_details_pass.png") ;
            print("\n**********LOGIN SUCCESSFUL*********") ;

            print("\n********WELCOME TEXT**********") ;
            text123=driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]').text ;
            print(text123) ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '(//a[contains(text(), "Sign Out")])[1]').click() ;
            time.sleep(1) ;

            assert True ;
            driver.close() ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_002_details_fail.png")
            print('\n*********SORRY, LOGIN UNSUCCESSFUL*********') ;

            assert False ;
            driver.close() ;
