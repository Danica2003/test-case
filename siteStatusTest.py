import requests
import Constants

def isSiteOnLine(siteUrl):
    response= requests.get(siteUrl)
    if(response.status_code==200):
        return True
    else:
        return False

if(isSiteOnLine(Constants.BASE_URL)==True):
    print('Website je online')
else:
    print('Website nije online')

if(isSiteOnLine(f'{Constants.BASE_URL}{Constants.LOGIN_PAGE}')==True):
    print('Login stranica je online')
else:
    print('login stranica nije online')
