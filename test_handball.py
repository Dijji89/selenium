from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://handball.by")
    driver.maximize_window()

    # Тест 1: Проверка наличия логотипа
    def test_logo_presence():
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'logo-handball.png')]"))
            )
            print("Тест 1 пройден: Логотип найден.")
        except Exception as e:
            print(f"Тест 1 не пройден: {e}")

    test_logo_presence()

    # Тест 2: Проверка доступности кнопки поиска
    def test_search_button_accessibility():
        try:
            search_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'search-submit')]"))
            )
            assert search_button.is_displayed(), "Кнопка поиска недоступна"
            print("Тест 2 пройден: Кнопка поиска доступна.")
        except Exception as e:
            print(f"Тест 2 не пройден: {e}")

    test_search_button_accessibility()

    # Тест 3: Проверка отображения кнопки "Поиск"
    def test_search_button_displayed():
        try:
            search_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'search-submit')]"))
            )
            assert search_button.is_displayed(), "Кнопка поиска не отображается"
            print("Тест 3 пройден: Кнопка поиска отображается.")
        except Exception as e:
            print(f"Тест 3 не пройден: {e}")

    test_search_button_displayed()

    # Новый Тест 4: Проверка наличия значка поиска внутри кнопки
    def test_search_icon_inside_button():
        try:
            search_icon = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'search-submit')]/i[contains(@class, 'fa-search')]"))
            )
            assert search_icon.is_displayed(), "Значок поиска внутри кнопки отсутствует"
            print("Тест 4 пройден: Значок поиска внутри кнопки найден.")
        except Exception as e:
            print(f"Тест 4 не пройден: {e}")

    test_search_icon_inside_button()

    # Тест 5: Проверка текста "Новости"
    def test_news_section_text():
        try:
            news_section = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Новости"))
            )
            assert news_section.text.strip() == "Новости", "Текст раздела Новости некорректен"
            print("Тест 5 пройден: Текст раздела Новости корректен.")
        except Exception as e:
            print(f"Тест 5 не пройден: {e}")

    test_news_section_text()

    # Тест 6: Проверка наличия футера
    def test_footer():
        try:
            footer = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//footer | //div[contains(@class, 'footer') or contains(@class, 'site-footer')]")
                )
            )
            assert footer.is_displayed(), "Футер отсутствует"
            print("Тест 6 пройден: Футер найден.")
        except Exception as e:
            print(f"Тест 6 не пройден: {e}")

    test_footer()

finally:
    driver.quit()