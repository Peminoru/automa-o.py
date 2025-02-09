from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os

# Configurar o proxy
PROXY =   #inserir proxy

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')
chrome_options.add_argument('--headless')  # Modo sem interface gráfica (opcional)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessar a página de login 
driver.get("link")   # inserir link 

# Clique no botão "Entrar com Google"
try:
    google_button_selector = "button[data-test='googleBtn']"
    google_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, google_button_selector))
    )
    google_button.click()
except TimeoutException:
    print("Erro ao encontrar o botão 'Entrar com Google'")

# Aguarde e mude para a nova janela (Login do Google)
try:
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])  # Muda para a nova janela
except TimeoutException:
    print("Erro ao alternar para a janela do Google Login")

# Encontrar o campo de e-mail e preenchê-lo
try:
    email_input_selector = "input#identifierId"
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector))
    )
    email_input.send_keys("email")   #inserir email
except TimeoutException:
    print("Erro ao encontrar o campo de e-mail")

# Clique no botão "Próxima" após preencher o e-mail
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'Próxima')]"))
    )
    next_button.click()
except TimeoutException:
    print("Erro ao encontrar ou clicar no botão 'Próxima'")

# Preencher o campo de senha
try:
    password_input_selector = "input[name='Passwd']"
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, password_input_selector))
    )
    # Utilize uma variável de ambiente para segurança
    password_input.send_keys(os.getenv("senha")   #inserir senha
except TimeoutException:
    print("Erro ao encontrar o campo de senha")

# Clique no botão "Próximo" para finalizar o login
try:
    next_button_selector = "button#passwordNext"
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, next_button_selector))
    )
    next_button.click()
except TimeoutException:
    print("Erro ao encontrar o botão 'Próximo'")

# Fechar o navegador após o teste (opcional)
driver.quit()
