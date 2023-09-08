import json
import csv
import xml.etree.ElementTree as ET

def salvar_dados_json(colecao_de_dados, nome_arquivo):
    lista_de_dados = list(colecao_de_dados.values())
    with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as json_file:
        json.dump(lista_de_dados, json_file, ensure_ascii=False, indent=4)

def salvar_dados_xml(colecao_de_dados, nome_arquivo):
    lista_de_dados = list(colecao_de_dados.values())
    root = ET.Element("dados")
    for dados in lista_de_dados:
        asset_element = ET.SubElement(root, "asset")
        for chave, valor in dados.items():
            elemento = ET.SubElement(asset_element, chave)
            elemento.text = valor
    tree = ET.ElementTree(root)
    tree.write(f'{nome_arquivo}.xml', encoding='utf-8', xml_declaration=True)

def salvar_dados_csv(colecao_de_dados, nome_arquivo):
    lista_de_dados = list(colecao_de_dados.values())
    with open(f'{nome_arquivo}.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        escritor_csv = csv.DictWriter(csv_file, fieldnames=lista_de_dados[0].keys())
        escritor_csv.writeheader()
        escritor_csv.writerows(lista_de_dados)