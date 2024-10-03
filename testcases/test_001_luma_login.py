import time


from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_001_luma_reg():

    def test_001_reg(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1);

        driver.implicitly_wait(5) ;

        driver.get("https://magento.softwaretestingboard.com/") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, "(//a[text()='Create an Account'])[1]" ).click();
        time.sleep(1) ;

        driver.find_element(By.CSS_SELECTOR, 'input[id="firstname"]').send_keys("Rushabh") ;
        time.sleep(1) ;

        driver.find_element(By.ID, "lastname").send_keys("Gadge") ;
        time.sleep(1) ;

        driver.find_element(By.NAME, "email").send_keys("rushabhgadge@gmail.com") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Rushabh@1995") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@type="password"])[2]').send_keys("Rushabh@1995") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//span[text()="Create an Account"]').click() ;
        time.sleep(1) ;

        if(driver.title=="My Account"):

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_001_luma_pass.png") ;
            print("\n**********REGISTRATION SUCCESSFUL**********") ;

            assert True;
            driver.close() ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_001_luma_fail.png");
            print("\n**********REGISTRATION UNSUCCESSFUL**********") ;

            assert False ;
            driver.close() ;