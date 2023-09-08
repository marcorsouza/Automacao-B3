from ativo_coletor_de_dados import AtivoColetorDeDados
from formato_saida import FormatoSaida
from helpers import salvar_dados_csv, salvar_dados_json, salvar_dados_xml
import logging

# Configurar o sistema de log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def salvar(ativos, formato_saida, nome_arquivo_saida=None, headless=True):
    try:
        # Cria um objeto ColetorDeDados
        coletor = AtivoColetorDeDados(ativos)
        # Coleta os dados de cada ativo
        coletor.coletar_dados()

        # Salva os dados no formato escolhido
        if formato_saida == FormatoSaida.JSON:
            salvar_dados_json(coletor.colecao_de_dados, nome_arquivo_saida)
        elif formato_saida == FormatoSaida.XML:
            salvar_dados_xml(coletor.colecao_de_dados, nome_arquivo_saida)
        elif formato_saida == FormatoSaida.CSV:
            salvar_dados_csv(coletor.colecao_de_dados, nome_arquivo_saida)

        # Exibe mensagem de conclusão
        mensagem = f'Dados de todos os ativos salvos em {nome_arquivo_saida}.{formato_saida}'
        logger.info(mensagem)

    except Exception as e:
        # Tratar exceções
        mensagem_erro = f"Ocorreu um erro: {str(e)}"
        logger.error(mensagem_erro)

if __name__ == "__main__":
    # Lista de ativos para coletar dados
    ativos = ['BBAS3', 'PETR4', 'VALE3']

    # Escolha o formato de saída desejado
    formato_saida = FormatoSaida.JSON

    # Nome de arquivo personalizado (ou deixe como None para usar o nome padrão "dados")
    nome_arquivo_saida = "meu_arquivo2"

    salvar(ativos, formato_saida, nome_arquivo_saida)
