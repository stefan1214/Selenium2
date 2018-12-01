from configFilmweb import driver

driver.get("https://www.filmweb.pl/")
driver.find_element_by_xpath(
    "(.//*[normalize-space(text()) and normalize-space(.)='REKLAMA:'])[1]/preceding::button[1]").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='Polityce prywatności'])[1]/following::button[1]").click()
driver.find_element_by_id("inputSearch").click()
driver.find_element_by_id("inputSearch").clear()
driver.find_element_by_id("inputSearch").send_keys(u"tytuł filmu")
driver.find_element_by_id("searchForm").submit()