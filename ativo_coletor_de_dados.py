from ativo import Ativo
from coletor_de_dados import ColetorDeDados


class AtivoColetorDeDados(ColetorDeDados):
    def coletar_dados(self, headless=True):
        for ativo in self.ativos:
            ativo_obj = Ativo(ativo, headless)
            ativo_obj.buscar_dados_economicos()
            self.colecao_de_dados[ativo] = ativo_obj.dados