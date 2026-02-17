import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from .models import Products

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
time.sleep(2)  # pause to see typing
# Fill form
driver.find_element(By.NAME, "name").send_keys("Laptop")
time.sleep(2)  # pause to see typing
driver.find_element(By.NAME, "price").send_keys("1000")
time.sleep(2)  # pause to see typing

# Submit
driver.find_element(By.TAG_NAME, "button").click()
# time.sleep(2)  # pause to see typing

# # Assert something after submit
# assert "success" in driver.page_source.lower()
# assert Products.objects.filter(name="Laptop", price=1000).exists()
#Products.objects.filter(name="Laptop", price=1000).delete()
driver.quit()