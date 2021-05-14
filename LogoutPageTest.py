from selenium import webdriver
import time
import Constants
import Locators

def LogoutPageTest(username, password):
    driver=webdriver.Chrome()
    driver.get(f'{Constants.BASE_URL}{Constants.LOGIN_PAGE}')
    driver.maximize_window()

    usernameField= driver.find_element_by_css_selector(Locators.login_page_username_css_selector)
    passwordField= driver.find_element_by_css_selector(Locators.login_page_password_css_selector)
    logInButton= driver.find_element_by_css_selector(Locators.Login_page_login_button_css_selector)

    usernameField.send_keys(username)
    passwordField.send_keys(password)

    logInButton.click()

    # Ukoliko se ne ulogijemo ne mozemo da se izlogujemo
    # zato ukoliko je neuspesan login imamo RANIJI izlazak iz programa

    if(driver.current_url!=f'{Constants.BASE_URL}{Constants.SECURE_PAGE}'):
       print('Neuspesan login')
       return

    # ako smo se ulogovali zelimo da nastavimo sa izvrsavanje testa
    # Odnosno, pritiskamo logout dugme

    logoutButton= driver.find_element_by_css_selector(Locators.Logout_page_Logout_button_css_selector)
    logoutButton.click()
    time.sleep(1)

    if(driver.current_url==f'{Constants.BASE_URL}{Constants.LOGIN_PAGE}'):
        print('Uspesno izlogovan')
    else:
        print('Neuspesno izlogovan')
    time.sleep(3)

LogoutPageTest('tomsmith','SuperSecretPassword!')