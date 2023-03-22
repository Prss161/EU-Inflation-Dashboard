import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    url = "https://tradingeconomics.com/country-list/inflation-rate?continent=europe"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    hinflatio_country_name = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody/tr[46]/td[1]')
    hinflatio_country_numb = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody/tr[46]/td[2]')
    linflation_country_name = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody/tr[1]/td[1]')
    linflation_country_numb = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody/tr[1]/td[2]')
    Poland = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]/div/div/table/tbody/tr[40]/td[2]')
    
    print(hinflatio_country_name.text ,hinflatio_country_numb.text, linflation_country_name.text, linflation_country_numb.text, 'Poland', Poland.text)

main()