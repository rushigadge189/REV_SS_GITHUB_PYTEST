import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_facebook_drp_calneder():

    def test_008_fb_drp_handle(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get('https://www.facebook.com/') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//a[@role="button"])[2]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@placeholder="First name"]').send_keys('Rushabh') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Gadge') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="reg_email__"]').send_keys('rushabhgadge@gmail.com') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@data-type="password"]').send_keys("Rushabh@1995") ;
        time.sleep(1) ;

        dd_day=Select(driver.find_element(By.XPATH, '//select[@name="birthday_day"]')) ;
        dd_day.select_by_value('24') ;
        time.sleep(1) ;

        dd_month=Select(driver.find_element(By.XPATH, '//select[@aria-label="Month"]')) ;
        dd_month.select_by_index(0) ;
        time.sleep(1) ;

        dd_year=Select(driver.find_element(By.XPATH, '//select[@name="birthday_year"]')) ;
        dd_year.select_by_visible_text("1995") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@value="2"]').click() ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_008_fb_calende_pass.png") ;

        driver.close() ;


