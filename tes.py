from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/login")

driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("safiratest")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="password"]').send_keys("Safira!23")
driver.find_element_by_id("password").submit()