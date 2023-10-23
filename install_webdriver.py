from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))


url = "https://www.google.com"

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)

print(driver.current_url)
print(driver.title)

'''
xpath:
//*[@id="APjFqb"]
'''

text = driver.find_element("id", "APjFqb")
text.send_keys("Ahmed Hasan")

driver.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()

driver.close
driver.quit
