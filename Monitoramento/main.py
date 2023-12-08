from Monitoramento.Zabbix.zabbix import main as zabbix
from  Monitoramento.Mapa.mapa import main as mapa
import time


def main():

    print("""
    ███████╗███╗   ██╗███████╗██╗    ██╗███████╗
    ██╔════╝████╗  ██║██╔════╝██║    ██║██╔════╝
    ███████╗██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗
    ╚════██║██║╚██╗██║██╔══╝  ██║███╗██║╚════██║
    ███████║██║ ╚████║███████╗╚███╔███╔╝███████║
    ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝                                              
    """)
    print("""
    Estado: Brasilia - DF 
    Author: Snews
    Desenvolvedor responsável: Mateus Santos de Jesus
    Objetivo: Esse script tem por objetivo automatizar o fluxo de abertura e de acessos dos 
    sistemas de monitoramento que possuímos atualamente. 
    """)

    # Chama a função principal do script Mapa
    zabbix()

    time.sleep(5)

    # Chama a função principal do script Zabbix
    mapa()

if __name__ == "__main__":
    main()