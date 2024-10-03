import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_005_mwh():

    def test_005_multiplewhandle(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get("https://demo.automationtesting.in/Windows.html") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//a[@class="analystic"])[3]').click() ;
        time.sleep(1) ;

        parenttitle=driver.title ;
        print("\n**********PARENT WINDOW TITLE**********") ;
        print(parenttitle) ;

        parentext=driver.find_element(By.XPATH, '//p[contains(text(),"Click the button to ope")]').text ;
        print("\n**********PARENT WINDOW TEXT*********")
        print(parentext) ;

        driver.find_element(By.XPATH, '(//button[@class="btn btn-info"])[2]').click() ;
        time.sleep(1) ;

        all_window=driver.window_handles ;

        print("\n*********PERFORMING ACTIONS ON ZEROTH WINDOW**********") ;
        driver.switch_to.window(all_window[0]) ;
        time.sleep(1) ;

        title0=driver.title ;
        print("\n*********TITLE OF ZEROTH WINDOW*********") ;
        print(title0) ;
        time.sleep(1) ;

        text0=driver.find_element(By.XPATH, '//h1[contains(text(), "Automation Demo")]').text ;
        print("\n**********TEXT OF ZEROTH WINDOW*********") ;
        print(text0) ;
        time.sleep(1) ;

        print("\n**********PERFORMING OPERATION ON FIRST WINDOW************") ;
        driver.switch_to.window(all_window[1]);
        time.sleep(1);

        title3=driver.title ;
        print("\n***********TITLE OF FIRST WINDOW***********") ;
        print(title3) ;
        time.sleep(1) ;

        text3=driver.find_element(By.XPATH, '//input[@ng-model="emailid"]').text ;
        print("\n**********TEXT OF FIRST WINDOW*********") ;
        print(text3) ;
        time.sleep(1) ;

        print("\nPERFORMINNG OPERATION ON SECOND WINDOW*********");
        driver.switch_to.window(all_window[2]);
        time.sleep(1);

        title2 = driver.title;
        print("\n**********TITLE OF SECOND WINDOW**********");
        print(title2);
        time.sleep(1);

        text2 = driver.find_element(By.XPATH, '//div[@class="mx-auto text-center p-4"]').text;
        print("\n**********TEXT OF SECOND WINDOW**********");
        print(text2);
        time.sleep(1);
        driver.close() ;

        driver.switch_to.window(all_window[1]) ;
        driver.close() ;

        driver.switch_to.window(all_window[0]) ;
        driver.close() ;

        #driver.quit();




