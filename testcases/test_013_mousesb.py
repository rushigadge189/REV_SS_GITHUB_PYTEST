import time

from selenium import webdriver


class Test_013_scroll_by_mouse() :

    def test_013_sbm(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://ed.ted.com/?utm_term=ted%20ed&utm_campaign=TED-Ed+site&utm_source=adwords&utm_medium=ppc&hsa_acc=7777130675&hsa_cam=18739292599&hsa_grp=151439764548&hsa_ad=631444589734&hsa_src=g&hsa_tgt=kwd-296155107571&hsa_kw=ted%20ed&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwxsm3BhDrARIsAMtVz6O8hI-lJIwThcqbdly9xoiHpTVh8uSHhjZ8lcKcijGFYvD6JCIEplMaAk-pEALw_wcB") ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_013_beforesc_pass.png") ;

        driver.execute_script("window.scrollBy(0,1000)") ;
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REV20\\screenshots\\test_013_aftersc_pass.png");

        driver.close();
        assert True ;