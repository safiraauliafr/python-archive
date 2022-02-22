import imp
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://facebook.com/")
driver.implicitly_wait(10)

driver.find_element_by_id("email").send_keys("fadhillahaulia1@gmail.com")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.ENTER).perform()

# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)\
#     .key_down()
