from selenium import webdriver
import pytest

driver = webdriver.Chrome()
driver.maximize_window()

urlAddress = [
        ("https://www.google.com/","Google"),
        ("https://twitter.com/home","Twitter")
]

# urlAddress using tupple

@pytest.mark.parametrize('url, result',urlAddress)

def test_openWeb(url, result):
    driver.get(url)
    tittle = driver.title

    assert tittle == result 


# accounts = [
#         ("safiraa","123"),       # true uname and false password
#         ("safira","S123!")       # true password and false uname
# ]

# # accounts using tupple

# @pytest.mark.parametrize('username,password',accounts)

# def test_openAccounts(username,password):
#     urlAccounts = "https://twitter.com/i/flow/login"
#     driver.get(urlAccounts)
#     driver.find_element_by_id("username").send_keys(username)
#     driver.find_element_by_id("password").send_keys(password)

#     tittle = driver.find_element_by_id("example")

#     assert tittle == "Invalid username or password"