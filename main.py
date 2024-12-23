import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Инициализация веб-драйвера для браузера Chrome
driver = webdriver.Chrome()

# URL сайта, с которого будет осуществляться скрейпинг
url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"

# Открытие указанного URL в браузере
driver.get(url)

# Ожидание 3 секунды для полной загрузки страницы
time.sleep(3)

# Поиск всех элементов на странице, которые соответствуют классу '_Ud0k'
divans = driver.find_elements(By.CLASS_NAME, '_Ud0k')

# Список для хранения названий и цен диванов
my_list = []

# Цикл по каждому найденному элементу (дивану)
for divan in divans:
    try:
        # Извлечение названия дивана
        name = divan.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        # Извлечение цены дивана
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        # Добавление названия и цены в список
        my_list.append([name, price])
    except NoSuchElementException:
        # Обработка случая, когда элемент не найден
        print("Произошла ошибка при парсинге")
        continue

# Закрытие браузера
driver.quit()

# Открытие (или создание) CSV-файла для записи данных
with open("homework.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Запись заголовков в CSV-файл
    writer.writerow(['Название', 'Цена'])
    # Запись всех извлеченных данных в CSV-файл
    writer.writerows(my_list)