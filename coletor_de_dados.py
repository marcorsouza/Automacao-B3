from ativo import Ativo

class ColetorDeDados:
    def __init__(self, ativos):
        self.ativos = ativos
        self.colecao_de_dados = {}

    def coletar_dados(self):
        raise NotImplementedError("Método 'coletar_dados' deve ser implementado nas classes derivadas.")

