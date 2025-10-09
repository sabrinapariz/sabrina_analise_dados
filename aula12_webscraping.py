from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
# --- Configurações ---
url = "https://www.dfimoveis.com.br/"
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 15) # espera até 15 segundos
# Abre o combobox de Venda/Aluguel
time.sleep(10)
# --- Abre o dropdown de Tipo de Negócio ---
botao_negocio = wait.until(EC.element_to_be_clickable((By.ID, "select2-negocios-container")))
botao_negocio.click()
print("Dropdown de tipo de negócio aberto.")
# --- Seleciona a opção 'VENDA' ---
nome_opcao = "VENDA"
xpath_opcao = (
f"//li[contains(@class,'select2-results__option') "
f"and normalize-space(text())='{nome_opcao}']"
)
elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
elemento_opcao.click()
print(f"Opção '{nome_opcao}' selecionada com sucesso!")
time.sleep(5)

# --- Abre o dropdown de Tipo de Imóvel ---
botao_tipo = wait.until(EC.element_to_be_clickable((By.ID, "select2-tipos-container")))
botao_tipo.click()
print("Dropdown de tipo de imóvel aberto.")

# --- Seleciona a opção 'APARTAMENTO' ---
nome_opcao = "APARTAMENTO"
xpath_opcao = (
    f"//li[contains(@class,'select2-results__option') "
    f"and normalize-space(text())='{nome_opcao}']"
)
elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
elemento_opcao.click()
print(f"Opção '{nome_opcao}' selecionada com sucesso!")

time.sleep(5)

# --- Abre o dropdown de Estado ---
botao_estado = wait.until(EC.element_to_be_clickable((By.ID, "select2-estados-container")))
botao_estado.click()
print("Dropdown de estado aberto.")

# --- Seleciona a opção 'DF' ---
nome_opcao = "DF"
xpath_opcao = (
    f"//li[contains(@class,'select2-results__option') "
    f"and normalize-space(text())='{nome_opcao}']"
)
elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
elemento_opcao.click()
print(f"Opção '{nome_opcao}' selecionada com sucesso!")
time.sleep(5)

# --- Abre o dropdown de Cidade ---
botao_cidade = wait.until(EC.element_to_be_clickable((By.ID, "select2-cidades-container")))
botao_cidade.click()
print("Dropdown de cidade aberto.")

# --- Seleciona a opção 'BRASÍLIA' ---
nome_opcao = "BRASILIA / PLANO PILOTO"
xpath_opcao = (
    f"//li[contains(@class,'select2-results__option') "
    f"and normalize-space(text())='{nome_opcao}']"
)
elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
elemento_opcao.click()
print(f"Opção '{nome_opcao}' selecionada com sucesso!")

time.sleep(5)


# --- Abre o dropdown de Bairro ---
botao_bairro = wait.until(EC.element_to_be_clickable((By.ID, "select2-bairros-container")))
botao_bairro.click()
print("Dropdown de bairro aberto.")

# --- Seleciona a opção 'ASA SUL' ---
nome_opcao = "ASA SUL"
xpath_opcao = (
    f"//li[contains(@class,'select2-results__option') "
    f"and normalize-space(text())='{nome_opcao}']"
)
elemento_opcao = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_opcao)))
elemento_opcao.click()
print(f"Opção '{nome_opcao}' selecionada com sucesso!")

time.sleep(5)

# --- Clica no botão PESQUISAR ---
botao_pesquisar = wait.until(EC.element_to_be_clickable((By.ID, "botaoDeBusca")))
botao_pesquisar.click()
print("Botão 'PESQUISAR' clicado com sucesso!")

time.sleep(5)




