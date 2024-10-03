import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_003_Login_Lp():

    def test_003_print_ll(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get('https://magento.softwaretestingboard.com/') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//a[contains(text(), "Sign In")]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="login[username]"]').send_keys("rushabhgadge@gmail.com") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="login[password]"]').send_keys('Rushabh@1995') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click() ;
        time.sleep(1) ;

        if(driver.title=="Home Page"):

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_003_dp_pass.png") ;
            print("\n*********LOGIN SUCCESSFUL**********") ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '(//a[text()="My Account"])[1]').click();
            time.sleep(1) ;

            print("\n*********LOGIN NAME**********") ;
            text1=driver.find_element(By.XPATH, '//p[contains(text(), "Rushabh Gadge")]').text ;
            print(text1) ;

            print("\n*********LOGIN ADDRESS********")
            text2=driver.find_element(By.XPATH, '(//address[contains(text(), "Rushabh Gadge")])[1]').text ;
            print(text2) ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click();
            time.sleep(1) ;

            driver.find_element(By.XPATH, '(//a[contains(text(), "Sign Out")])[1]').click();
            time.sleep(1) ;

            driver.close();
            assert True ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_003_dp_fail.png") ;

            print("\n*********SORRY, LOGIN UNSUCCESSFUL*********") ;

            driver.close();
            assert False ;


