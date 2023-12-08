from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
import pyautogui
import time

def main():
    print("""
    ███╗   ███╗ █████╗ ██████╗  █████╗ 
    ████╗ ████║██╔══██╗██╔══██╗██╔══██╗
    ██╔████╔██║███████║██████╔╝███████║
    ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔══██║
    ██║ ╚═╝ ██║██║  ██║██║     ██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝                                          
    """)

    print("# Inicializando o Driver do Firefox e armazenando váriaveis")
    # Caminho para Execução do GeckoDriver (Firefox)
    gecko_driver_path = 'ProjetoAutomacaoMonitoramento\\Monitoramento\\geckodriver-v0.33.0-win64\\geckodriver.exe'
    # Configurações do Firefox
    firefox_options = Options()
    firefox_options.page_load_strategy = 'eager'
    # Chama o arquivo de credênciais
    env_vars = dotenv_values(".env")
    # URL de acesso à API do Google Maps
    urlApi = env_vars.get("API_MAPA_URL")
    # Informações de login
    email = env_vars.get("API_MAPA_USER")
    senha = env_vars.get("API_MAPA_PASS")

    print("# Inicializando o Navegador")
    # Configuração do GeckoDriver (Firefox)
    firefox_service = FirefoxService(executable_path=gecko_driver_path)
    # Inicialização do WebDriver do Firefox
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    # Definir monitor
    driver.set_window_position(0,0)
    # Maximizar a janela do navegador
    driver.maximize_window()
    pyautogui.press('f11')
    # Abrir URL
    driver.get(urlApi)
    time.sleep(5)

    print("# Preenchendo campos e clicando no botão")
    # Localizar o campo de e-mail e preencher
    campo_email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'identifierId')))
    campo_email.send_keys(email)
    # Localizar o campo 'avançar' e clicar
    botao_next = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
    botao_next.click()
    time.sleep(5)
    # Localizar o campo de senha e preencher
    campo_senha = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
    campo_senha.send_keys(senha)
    time.sleep(5)
    botao_next = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
    botao_next.click()
    time.sleep(10)

    print("# Executando PING nos clientes")
    # Esperar até que o login seja concluído e, em seguida, pressionar Enter
    espera = WebDriverWait(driver, 5) 
    espera.until(EC.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys(Keys.ENTER)

    time.sleep(5)

    print("# Mapa em execução...")
    while True:
        for n in range(140):
            driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[5]/div[1]/div/div[9]/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/div[3]/div[{n + 1}]').click()
            time.sleep(6)

if __name__ == "__main__":
    main()