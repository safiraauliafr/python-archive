from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# def test_openWeb():
#     driver.get("https://www.google.com/")
#     tittle = driver.title

#     assert tittle == 'Google' 
#     print(tittle)

# test_openWeb()

# line 12 used for calling the function

class OpenTwitter:
    
    def openTwtClass(self):
        driver.get("https://twitter.com/home")
        title = driver.title

        assert title == 'Twitter'

open = OpenTwitter()
open.openTwtClass()