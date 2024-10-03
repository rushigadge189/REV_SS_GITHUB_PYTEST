import time

from selenium import webdriver


class Test_013_scroill_by_mouse():

    def test_013_mousescroll(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://www.bbc.com/") ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_013_beforescroll_pass.png") ;

        driver.execute_script("window.scrollBy(0,1000)") ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_013_afterscroll_pass.png");

        driver.close() ;
        assert True ;
