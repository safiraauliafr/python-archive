from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
import pytest

accounts = [
        ("idejongkok","123"),       # true uname and false password
        ("safira","asDF12#$"),      # true password and false uname
        ("safira","safira#$")       # false password and false uname
]

@pytest.fixture
def setup():
        driver = webdriver.Chrome()
        urlAccounts = "https://demoqa.com/login"
        driver.get(urlAccounts)
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit

# accounts using tupple

def test_openSuccess(setup):
       
        setup.find_element_by_id("userName").send_keys("safiratest")
        setup.implicitly_wait(5)
        setup.find_element_by_id("password").send_keys("Safira!23")
        setup.find_element_by_id("login").click()

        header = setup.find_element_by_class_name("main-header").text

        assert header == "Profile"

@pytest.mark.parametrize('username,password',accounts)

def test_openFail(setup, username,password):
        
        setup.find_element_by_id("userName").send_keys(username)
        setup.implicitly_wait(3)
        setup.find_element_by_id("password").send_keys(password)
        setup.find_element_by_id("login").click()

        tittle = setup.find_element_by_id("name").text

        assert tittle == "Invalid username or password!"