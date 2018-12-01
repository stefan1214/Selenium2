from configFilmweb import driver
from filmwebUserConfig import filmWebUserName as fwUserName
from filmwebUserConfig import botUserName as botLogin
from filmwebUserConfig import botPassword as botPass
import time

from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

def loggingBotAccount():
    driver.get("https://www.filmweb.pl/")
    try:
        driver.find_element_by_id("goToLink").click()
    except NoSuchElementException:
        print("Długa ta reklama")
    try:
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='REKLAMA:'])[1]/preceding::button[1]").click()
    except ArithmeticError:
        print("Długa ta reklama")
    except NoSuchElementException:
        print("Długa ta reklama")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Polityce prywatności'])[1]/following::button[1]").click()
    try:
        driver.find_element_by_id("menuOpenerLabel").click()
        driver.find_element_by_id("loginButton").click()
    except ElementNotVisibleException:
        driver.find_element_by_id("loginButton").click()

    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Google'])[1]/following::div[3]").click()
    driver.find_element_by_name("j_username").click()
    driver.find_element_by_name("j_username").clear()
    driver.find_element_by_name("j_username").send_keys(botLogin)
    driver.find_element_by_name("j_password").click()
    driver.find_element_by_name("j_password").clear()
    driver.find_element_by_name("j_password").send_keys(botPass)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Nie pamiętam hasła'])[1]/following::div[2]").click()
def openUserWantToSeePage():
    driver.get("https://www.filmweb.pl/user/"+fwUserName+"/wantToSee")
    i=1
    j=2
    while True:
        try:
            sleep(2000)
            print(driver.find_elements_by_class_name("filmPreview__title")[i].text+";")
            print(driver.find_elements_by_class_name("filmPreview__originalTitle")[i].text+";")
            print(driver.find_elements_by_class_name("filmPreview__year")[i].text+";")
            print(driver.find_elements_by_class_name("rateBox__rate")[i].text+"~")
        except IndexError:
            driver.get("https://www.filmweb.pl/user/"+fwUserName+"/wantToSee?page="+str(j))
            j+=1
            i=1

        i+=1


loggingBotAccount()
openUserWantToSeePage()


# driver.get("https://www.filmweb.pl/")
# driver.find_element_by_xpath(
#     "(.//*[normalize-space(text()) and normalize-space(.)='REKLAMA:'])[1]/preceding::button[1]").click()
# driver.find_element_by_xpath(
#     u"(.//*[normalize-space(text()) and normalize-space(.)='Polityce prywatności'])[1]/following::button[1]").click()
# driver.find_element_by_id("inputSearch").click()
# driver.find_element_by_id("inputSearch").clear()
# driver.find_element_by_id("inputSearch").send_keys(u"tytuł filmu")
# driver.find_element_by_id("searchForm").submit()