from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pintek.id/")

driver.implicitly_wait(40)

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="qontak-webchat-widget"]'))
driver.find_element_by_class_name("qchat-button").click()
driver.find_element_by_name("Name").send_keys("Safira")