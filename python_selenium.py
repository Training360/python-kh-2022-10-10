from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Elindul a webdriver és utána a böngésző
driver = webdriver.Chrome(ChromeDriverManager().install())
# python.org
driver.get("https://python.org")

