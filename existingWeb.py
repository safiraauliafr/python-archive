from selenium import webdriver
from selenium.webdriver.chrome.options import Options


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\\Users\\Safira\\Downloads\\chromedriver_win32\\chromedriver.exe",chrome_options=opt)
driver.get("https://facebook.com/")

# this is finally working yeay
