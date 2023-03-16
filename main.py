import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    url = "https://ec.europa.eu/eurostat/databrowser/view/PRC_HICP_MANR__custom_3761882/settings_1/table?lang=en&bookmarkId=4ad27e6f-358a-4a3d-82a0-587d69a833eb"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)
    number = driver.find_element(By.XPATH, '')
    print(number.text)

main()