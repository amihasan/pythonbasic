from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Fservice
from selenium.webdriver.chrome.service import Service as Chrmservice
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Firefox(service = Fservice(GeckoDriverManager().install()))
driver = webdriver.Chrome(service=Chrmservice(ChromeDriverManager().install()))




url = "https://www.gmail.com"

driver.maximize_window()
driver.implicitly_wait(20)

driver.get(url)

'''
learningaselenium@gmail.com
<input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username" spellcheck="false" tabindex="0" aria-label="Email or phone" name="identifier" 
value="" autocapitalize="none" 
id="identifierId" dir="ltr" data-initial-dir="ltr" data-initial-value="learningaselenium@gmail.com" badinput="false">

//*[@id="password"]/div[1]/div/div[1]/input
<span jsname="V67aGc" class="VfPpkd-vQzf8d">Next</span>

'''
driver.implicitly_wait(20)
username = driver.find_element("id", "identifierId")
username.send_keys("learningaselenium@gmail.com")

driver.find_element("xpath", "//*[@id=\"identifierNext\"]/div/button/span").click()



password = driver.find_element("xpath", "//*[@id=\"password\"]/div[1]/div/div[1]/input")
password.send_keys("Disney#2016")

driver.find_element("xpath", "//*[@id=\"passwordNext\"]/div/button/span").click()



# Need to check the error message issue
# error_message = driver.find_element("cssSelector", "#yDmH0d > c-wiz > div > div.eKnrVb > div > div.j663ec > div > form > span > section:nth-child(2) > div > div > div.SdBahf.Fjk18.Jj6Lae > div.OyEIQ.uSvLId > div:nth-child(2) > span").text()
# print(error_message)


time.sleep(10)

