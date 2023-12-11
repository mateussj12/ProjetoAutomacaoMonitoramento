# Sistema de automação Zabbix e Google Maps
Esse projeto foi desenvolvido com o foco de automatizar o processo de execução e configuração do Zabbix para monitoramento de firewall Pfsense,
além de executar e configurar um mapa particular, desenvolvido através da API do Google Maps.

### Requisitos:
- Instalar o Python3
- Instalar as bibliotecas, selenium, pandas, time, datetime, pyautogui, dontenv 
- Driver do navegador Firefox
- Navegador Firefox atualizado

### Estrutura de pastas:
```
.
│   geckodriver.log
│   main.py
├───env
│       .env
├───geckodriver-v0.33.0-win64
│       geckodriver.exe
├───Mapa
│   │   mapa.py
│   └───__pycache__
│           mapa.cpython-311.pyc
└───Zabbix
    │   geckodriver.log
    │   zabbix.py
    └───__pycache__
            zabbix.cpython-311.pyc
```

### Considerações finais:
- **@Desenvolvedor:** Mateus Santos de Jesus
- **@Linkedin:** https://www.linkedin.com/in/mateus-santos-de-jesus-9819a8186