import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_drp_down():

    def test_008_drop_down_handling(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1);

        driver.implicitly_wait(5) ;
        time.sleep(1);

        driver.get('https://www.careinsurance.com/rhicl/proposalcp/renew/index-care')  ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@placeholder="Policy Number"]').send_keys('123456987') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@placeholder="DOB"]').click() ;
        time.sleep(1);

        month=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-month"]') ) ;
        month.select_by_visible_text('Jun') ;
        time.sleep(1) ;

        year=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]'))
        year.select_by_value("2005") ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//a[@data-date="20"]').click() ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="alternative_number"]').send_keys('1234567890') ;
        time.sleep(1);
        
        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_008_drop_down_pass.png") ;

        driver.close() ;

