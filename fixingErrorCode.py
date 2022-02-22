from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service1 = Service("C:\\Users\\Safira\\Documents\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.maximize_window()
driver.get("https://google.com/")

webTitle = driver.title
print(webTitle)

assert "Google" in webTitle