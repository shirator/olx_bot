from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get("https://am.olx.com.br")

time.sleep(2)
user_name = "your_email"
password = "your_password"
element = driver.find_element_by_xpath(f"//span[@class='e58tx4-4 cGiAhA']")
element.click()
element = driver.find_element_by_xpath(f"//input[@type='email']")
element.send_keys(user_name)
element = driver.find_element_by_xpath(f"//input[@type='text']")
element.send_keys(password)
element.send_keys(Keys.RETURN)

time.sleep(4)
publish = driver.find_element_by_link_text('Anunciar')
publish.click()


titulo_input = "title here"
descricao_input = "description here"

titulo = driver.find_element_by_xpath(f"//input[@type='text']")
titulo.send_keys(titulo_input)

descricao = driver.find_element_by_xpath("//textarea[@id='input_body']")
descricao.send_keys(descricao_input)

time.sleep(2)
categoria = driver.find_element_by_xpath("//a[@id='category_item-2000']")
categoria.click()
time.sleep(2)
sub_categoria = driver.find_element_by_xpath("//a[@id='category_item-2060']")
sub_categoria.click()

time.sleep(2)
selecionar_marca = driver.find_element_by_xpath("//select[@id='vehicle_brand']")
selecionar_marca.click()
time.sleep(2)
marca = driver.find_element_by_xpath("//option[@value='7']")
marca.click()
