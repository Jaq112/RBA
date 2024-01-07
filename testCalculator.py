
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select;
import time
driver = webdriver.Chrome()
driver.implicitly_wait(15)

#Navigate to RBA
driver.get("https://www.rba.hr/")



#Opening calculator
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
driver.find_element(By.XPATH, "//a[@href='https://www.rba.hr/alati']").click()
driver.find_element(By.XPATH, '//*[@id="mainNav"]/div/ul/li[4]/div/div/div[2]/div[4]/div/ul/li[1]/a').click() #title and href don't seem to work

#--- USD -> GPB
#Select GPB
select_element = driver.find_element(By.ID, 'val1')
select = Select(select_element)
select.select_by_value('826')

#Select USD
select_element = driver.find_element(By.ID, 'val2')
select = Select(select_element)
select.select_by_value('840')

#Write Amount
driver.find_element(By.ID,"suma1").clear()
driver.find_element(By.ID,"suma1").send_keys('20')
time.sleep(1)

#Read values
Value = driver.find_element(By.ID,"toHouseExch").text
Exch = driver.find_element(By.ID,"rateExch").text
GPB, USD = Value.split('=')
print("kupnja GBP: tečaj je "+ Exch +", za "+ USD +" dobijem " + GPB)



#--- EUR -> USD
#Select USD
select_element = driver.find_element(By.ID, 'val1')
select = Select(select_element)
select.select_by_value('840')

#Select EUR
select_element = driver.find_element(By.ID, 'val2')
select = Select(select_element)
select.select_by_value('978')

#Write Amount
driver.find_element(By.ID,"suma1").clear()
driver.find_element(By.ID,"suma1").send_keys('100')
time.sleep(1)

#Read values
Value = driver.find_element(By.ID,"toHouseExch").text
Exch = driver.find_element(By.ID,"rateExch").text
USD, EUR = Value.split('=')
print("kupnja USD: tečaj je "+ Exch +", za "+ EUR +" dobijem " + USD)