from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from dotenv import dotenv_values
import pyautogui
import time

def main():
    print(""" 
            
    ███████╗ █████╗ ██████╗ ██████╗ ██╗██╗  ██╗
    ╚══███╔╝██╔══██╗██╔══██╗██╔══██╗██║╚██╗██╔╝
      ███╔╝ ███████║██████╔╝██████╔╝██║ ╚███╔╝ 
     ███╔╝  ██╔══██║██╔══██╗██╔══██╗██║ ██╔██╗ 
    ███████╗██║  ██║██████╔╝██████╔╝██║██╔╝ ██╗
    ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝
        """)

    print("# Inicializando o Driver do Firefox e armazenando váriaveis")
    # Caminho para Execução do GeckoDriver (Firefox)
    gecko_driver_path = 'ProjetoAutomacaoMonitoramento\\Monitoramento\\geckodriver-v0.33.0-win64\\geckodriver.exe'  
    # Chama o arquivo de credênciais
    env_vars = dotenv_values(".env")
    # Configurações do Firefox
    firefox_options = Options()
    firefox_options.page_load_strategy = 'eager'
    # URL de acesso à API do Google Maps
    urlZabbix = env_vars.get("ZABBIX_URL")
    # Informações de login
    usuario = env_vars.get("ZABBIX_USER")
    senha = env_vars.get("ZABBIX_PASS")
 

    print("# Inicializando o Navegador")
    # Configuração do GeckoDriver (Firefox)
    firefox_service = FirefoxService(executable_path=gecko_driver_path)
    # Inicialização do WebDriver do Firefox
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    # Definir monitor
    driver.set_window_position(1920,0)
    # Maximizar a janela do navegador
    driver.maximize_window()
    pyautogui.press('f11')
    # Abrir URL
    driver.get(urlZabbix)
    time.sleep(5)

    print("# Preenchendo campos e clicando no botão")
    # Localizar o campo de e-mail e preencher
    campo_email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@name="user"]')))
    campo_email.send_keys(usuario)
    time.sleep(5)
    # Localizar o campo de senha e preencher
    campo_senha = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'current-password')))
    campo_senha.send_keys(senha)
    time.sleep(5)
    # Localizar o campo 'avançar' e clicar
    botao_next = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Login button"]')))
    botao_next.click()

    print("# Zabbix em execução...")

if __name__ == "__main__":
    main()