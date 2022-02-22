from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://facebook.com/")

driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
driver.implicitly_wait(5)

driver.find_element_by_name("firstname").send_keys("Alvin")
driver.find_element_by_name("lastname").send_keys("X")
driver.find_element_by_name("reg_email__").send_keys("alvinx@yopmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("alvinx@yopmail.com")
driver.find_element_by_id("password_step_input").send_keys("alvinxfactor!23")

day = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text("24")

month = Select(driver.find_element_by_name("birthday_month"))
month.select_by_visible_text("Aug") 

year = Select(driver.find_element_by_name("birthday_year"))
year.select_by_visible_text("1997")

driver.find_element_by_xpath("//label[text()='Male']").click()

driver.find_element_by_xpath("//button[text()='Sign Up']").click()