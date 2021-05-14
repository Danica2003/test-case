from selenium import webdriver
import Constants
import Locators
import MockedData
import time

def TestLogin(username, password):
    driver=webdriver.Chrome()
    driver.get(f'{Constants.BASE_URL}{Constants.LOGIN_PAGE}')
    driver.maximize_window()

    usernameField= driver.find_element_by_css_selector(Locators.login_page_username_css_selector)
    passwordField= driver.find_element_by_css_selector(Locators.login_page_password_css_selector)
    logInBotton= driver.find_element_by_css_selector(Locators.Login_page_login_button_css_selector)

    usernameField.send_keys(username)
    passwordField.send_keys(password)

    logInBotton.click()
    if(driver.current_url==f'{Constants.BASE_URL}{Constants.SECURE_PAGE}'):
        print(f'Sucessfull login with {username} and {password}')
    else:
        print(f'Bad login for {username} and {password}')
    
    time.sleep(3)

for podatak in MockedData.TEST_DATA: # Mockedata je lista recnika koju smo importovali
    TestLogin(podatak['username'], podatak['password'])

