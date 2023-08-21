from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
import time
import threading
 
class CPUPainter:
 
    def paintwall(self) :
 
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome("C:/Users/Juwon/Downloads/chromedriver.exe")
 
        url = "https://docs.google.com/forms/d/e/1FAIpQLSf0Qt1L6XInU7K-LmJAVbzVZwn4YihQicdHdZ1eRztGlAyVWg/viewform"
 
        driver.get(url)
        # voteCount = 0
 
 
        def fill_form(maleCandidate, femaleCandidate):
            print("Fill Form")
            # WebDriverWait(driver, 30).until(
            #     EC.visibility_of_element_located((By.CLASS_NAME, "exportButtonContent")))
 
            time.sleep(2)
            maleRadioButton = driver.find_elements(By.ID, "i20")
            femaleRadioButton = driver.find_elements(By.ID, "i35")
            print("Time Sleep")
            print(maleRadioButton)
            print("Time Sleep")
 
            for maleRadio in maleRadioButton:            
                print("Radio Loop")
                print("data-value => " + maleRadio.get_attribute("data-value"))
                if maleRadio.get_attribute("data-value") == maleCandidate:
                    maleRadio.click()
                else:
                    print("Error Validating MaleRadio")
 
            for femaleRadio in femaleRadioButton:            
                print("Radio Loop")
                print("data-value => " + femaleRadio.get_attribute("data-value"))
                if femaleRadio.get_attribute("data-value") == femaleCandidate:
                    femaleRadio.click()
                else:
                    print("Error Validating FemaleRadio")
 
            submit = driver.find_element(By.CLASS_NAME, "lRwqcd")
            print("Submit")
            print(submit)
            submit.click()
 
            time.sleep(1)
            # WebDriverWait(driver, 10).until(
            #     EC.visibility_of_element_located((By.ID, "freebirdFormviewerViewResponseLinksContainer")))
 
            another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
            another_response.click()
            # voteCount += 1
            # print("Completed Votes => " + str(voteCount))
            fill_form("Ayodele Ayotola (Nursing 100Level)", "Adisa Adeola Victoria (Nursing 100Level")
 
        fill_form("Ayodele Ayotola (Nursing 100Level)", "Adisa Adeola Victoria (Nursing 100Level")
 
    def __init__(self):
        t = threading.Thread(target=self.paintwall)
        t.start()
 
# 15 instances of this program are executed simultaneously (Multi-Thread)
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()