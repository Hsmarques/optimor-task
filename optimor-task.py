from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk") # Load page
assert "O2" in browser.title
elem = browser.find_element_by_class_name("o2body") # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(1) # Let the page load, will be added to the API
try:
    browser.find_element_by_id("showAllCountries")
except NoSuchElementException:
    assert 0, "can't find the element you're looking for"
browser.close()