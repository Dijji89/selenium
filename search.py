from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Установка и запуск драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://handball.by")
    driver.maximize_window()

    # Тест 7: Проверка выполнения поиска по слову "Минск"
    def test_search_functionality():
        try:
            # Шаг 1: Нажать кнопку для активации поля поиска
            first_search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-submit"))
            )
            first_search_button.click()

            # Шаг 2: Ожидание, что поле ввода появится и будет доступно
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.search-input.active"))
            )

            # Шаг 3: Вводим текст в поле поиска
            search_input.clear()  # Очистить поле перед вводом
            search_input.send_keys("Минск")  # Вводим слово для поиска

            # Шаг 4: Нажать кнопку с классом .search-submit.activated для выполнения поиска
            second_search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-submit.activated"))
            )
            second_search_button.click()

            # Шаг 5: Проверяем, что результаты поиска загружены
            print("Ожидаем загрузки результатов поиска...")
            # Даем немного больше времени на загрузку, и проверяем наличие результата
            search_results = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'stm-single-post-loop')]"))
            )

            # Шаг 6: Проверяем количество страниц пагинации
            pagination_elements = driver.find_elements(By.CSS_SELECTOR, "ul.page-numbers a.page-numbers")
            
            # Если пагинация не пустая, то проверим количество страниц
            if pagination_elements:
                # Получаем номер последней страницы
                last_page_number = pagination_elements[-2].text  # Последний элемент перед "next"
                print(f"Найдено {last_page_number} страниц с результатами.")
                
                # Проверяем, что количество страниц больше 1
                if int(last_page_number) > 1:
                    print("Тест 7 пройден: Поиск по слову 'Минск' выполнен успешно.")
                else:
                    print("Тест 7 не пройден: Только одна страница с результатами.")
            else:
                print("Тест 7 не пройден: Не найдены элементы пагинации.")
                
        except Exception as e:
            print(f"Тест 7 не пройден: {e}")
            # Для диагностики выводим больше информации
            driver.save_screenshot("screenshot_failure.png")
            print("Скриншот сохранен как screenshot_failure.png для диагностики.")

    # Запуск теста
    test_search_functionality()

finally:
    driver.quit()