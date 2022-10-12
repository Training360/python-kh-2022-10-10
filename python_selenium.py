from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Elindul a webdriver és utána a böngésző
driver = webdriver.Chrome(ChromeDriverManager().install())
# python.org
driver.get("https://python.org")

field = driver.find_element(By.ID, "id-search-field")
field.click()
field.send_keys("comprehension")

sleep(3)

button = driver.find_element(By.ID, "submit")
button.click()

sleep(3)

text = driver.find_element(By.CSS_SELECTOR, ".list-recent-events a").text
print(text)

