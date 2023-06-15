import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def selenium_driver():
   driver = selenium_webdriver.Chrome(r'C:\Users\71601088\PycharmProjects\pythonProject12\tests\chromedriver.exe')
   driver.get('http://petfriends.skillfactory.ru/login')

   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

   driver.find_element(By.ID, "email").send_keys("Ostaleksandra32@gmail.com")
   driver.find_element(By.ID, "pass").send_keys("12345")
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   yield driver

   driver.quit()
