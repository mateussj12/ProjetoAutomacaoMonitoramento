from Monitoramento.Zabbix.zabbix import main as zabbix
from  Monitoramento.Mapa.mapa import main as mapa
import time


def main():

    print("""
        ██╗███████╗███████╗██╗   ██╗███████╗
        ██║██╔════╝██╔════╝██║   ██║██╔════╝
        ██║█████╗  ███████╗██║   ██║███████╗
   ██   ██║██╔══╝  ╚════██║██║   ██║╚════██║
   ╚█████╔╝███████╗███████║╚██████╔╝███████║
    ╚════╝ ╚══════╝╚══════╝ ╚═════╝ ╚══════╝
                                                 
    """)
    print("""
    **Estado**: Brasília - DF 
    **Desenvolvedor responsável**: Mateus Santos de Jesus
    **Objetivo**: Esse script chama duas funções, zabbix() e mapa(), e executa de forma respectiva. 
    A função Zabbix executa um script que iniciliaza o sistema de monitoramento zabbix para acompanhar a infraestrutura.
    A função Mapa executa um mapa desenvolvido com a API do Google Maps para monitoramento dos clientes da empresa com base região...
    """)

    # Chama a função principal do script Mapa
    zabbix()

    time.sleep(5)

    # Chama a função principal do script Zabbix
    mapa()

if __name__ == "__main__":
    main()