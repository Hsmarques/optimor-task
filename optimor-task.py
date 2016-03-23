from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

def get_prices(name):
	pass
	element = driver.find_element_by_id("countryName")
	element.send_keys(name, Keys.RETURN)

	paymonthly = driver.find_element_by_id("paymonthly")
	paymonthly.send_keys(Keys.RETURN)

	landline = driver.find_element_by_xpath("//table[@id='standardRatesTable']//tbody//td[contains(text(),'Landline')]/following::td")
	print("Landline: "+landline.text)

for country in countries:
	print("Prices for "+country)
	get_prices(country)

print("DONE")