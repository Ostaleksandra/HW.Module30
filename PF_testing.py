from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# python -m pytest -v --driver Chrome --driver-path pythonProject12/tests/chromedriver.exe PF_testing.py

def test_show_my_pets(selenium_driver):
   driver = selenium_driver

   # Нажимаем на кнопку входа в пункт меню Мои питомцы
   driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
   time.sleep(3)

   # Проверяем, что оказались на странице питомцев пользователя
   assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

   # Проверяем, что присутствуют все питомцы
   pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
   pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
   assert int(pets_number) == len(pets_count)


def test_checking_cards_of_pets(selenium_driver):
   driver = selenium_driver
   driver.implicitly_wait(3)
   images = driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/th/img")
   driver.implicitly_wait(3)
   names = driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[1]")
   driver.implicitly_wait(3)
   breeds = driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[2]")
   driver.implicitly_wait(3)
   ages = driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[3]")

   images_count = 0
   names_list = []
   pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
   driver.implicitly_wait(3)

   # Проверяем, что хотя бы у половины питомцев есть фото
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         images_count += 1
      else:
         images_count += 0
      assert images_count / len(pets_count) >= 0.5

   # Проверяем, что у всех питомцев есть имя, возраст и порода
      assert names[i].text != ''
      assert breeds[i].text != ''
      assert ages[i].text != ''

   # Проверяем, что у всех питомцев разные имена
      names_list.append(names[i].text)
      names_set = set(names_list)
      assert len(names_set) == len(names_list)







