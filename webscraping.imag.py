from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crie um novo navegador
driver = webdriver.Chrome()

# Acesse o site
driver.get("")

# Espere até que a página carregue
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product")))

# Encontre todos os produtos na página
produtos = driver.find_elements(By.CSS_SELECTOR, ".product")

# Itere sobre os produtos e extraia as informações
for produto in produtos:
    nome = produto.find_element(By.CSS_SELECTOR, ".product-name").text
    preco = produto.find_element(By.CSS_SELECTOR, ".price").text
    descricao = produto.find_element(By.CSS_SELECTOR, ".description").text

    print("Nome:", nome)
    print("Preço:", preco)
    print("Descrição:", descricao)
    print("------------------------")

# Feche o navegador
driver.quit()
