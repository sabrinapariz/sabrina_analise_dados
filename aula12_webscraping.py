from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://dfimoveis.com.br/"
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
xpath = "/html/body/main/section[1]/div[1]/div[1]/form/div[1]/span[1]/span[1]/span"
botao_venda = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
botao_venda.click()

dropdown_xpath = "/html/body/main/section[1]/div[1]/div[1]/form/div[1]/span[1]/span[1]/span"
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()

opcao_venda = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@id,'select2-negocios-result') and text()='VENDA']")))
opcao_venda.click()

# === Seleciona o campo "TIPO (TODOS)" ===
xpath_tipo = "/html/body/main/section[1]/div[1]/div[1]/form/div[2]/span[1]/span[1]/span"
campo_tipo = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tipo)))
campo_tipo.click()

# === Seleciona a opção "Apartamento" ===
opcao_apartamento = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(@id, 'select2-tipos-result') and text()='Apartamento']"))
)
opcao_apartamento.click()