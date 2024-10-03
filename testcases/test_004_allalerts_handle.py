import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_alerthandling_all():

    def test_004_sinmple_alert(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1);

        driver.implicitly_wait(5) ;

        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="alertexamples"]').click() ;
        time.sleep(1) ;

        simplealerttext=Alert(driver).text ;
        print("\n**********SIMPLE ALERT TEXT********") ;
        print(simplealerttext) ;

        Alert(driver).accept() ;
        time.sleep(1) ;

        saftertext=driver.find_element(By.XPATH, '//p[@id="alertexplanation"]').text ;
        print("\n*********TEXT AFTER ACCEPTING SIMPLE ALERT**********") ;
        print(saftertext) ;

        driver.close() ;
        assert True ;

    def test_004_confirmation_alert(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="confirmexample"]').click() ;
        time.sleep(1) ;

        catext=Alert(driver).text ;
        print("\n**********CONFIRMATION ALERT TEXT********") ;
        print(catext) ;

        Alert(driver).dismiss();

        cadismisstext=driver.find_element(By.XPATH, '//p[@id="confirmexplanation"]').text ;
        print("\n*********TEXT AFTER DISMIISSING CONFIRMATION ALERT**********") ;
        print(cadismisstext) ;

        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="confirmexample"]').click() ;
        time.sleep(1) ;

        Alert(driver).accept();
        time.sleep(1) ;

        caaccept=driver.find_element(By.XPATH, '//p[@id="confirmexplanation"]').text ;
        print("\n*********TEXT AFTER ACCEPTING CONFIRMATION ALERT*********") ;
        print(caaccept) ;


        driver.close() ;
        assert True ;

    def test_004_prompt_alert(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;
        time.sleep(1) ;

        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="promptexample"]').click() ;
        time.sleep(1) ;

        patext=Alert(driver).text ;
        print("\n**********PROMPT ALERT TEXT**********") ;
        print(patext) ;

        Alert(driver).send_keys("WELCOME TO JUNGLE") ;
        time.sleep(2) ;

        Alert(driver).accept() ;

        paatext=driver.find_element(By.XPATH, '//p[@id="promptexplanation"]').text ;
        print("\n**********TEXT AFTER ACCEPTING PROMT ALERT**********") ;
        print(paatext) ;

        driver.close() ;
        assert True ;