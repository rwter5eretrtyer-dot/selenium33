import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://ya.ru")

    print("Сайт успешно открыт")
    print("Заголовок страницы:", driver.title)
    print("Текущий адрес:", driver.current_url)

    # Браузер будет открыт 10 секунд
    time.sleep(10)

finally:
    # Затем программа сама корректно закроет Chrome
    driver.quit()