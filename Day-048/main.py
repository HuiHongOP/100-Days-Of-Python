from selenium import webdriver
from selenium.webdriver.common.by import By

#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")

price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text


print(price_dollar, price_cents)

driver.quit()