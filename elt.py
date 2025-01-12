import csv

## extração 
def ler_csv(arquivo_csv:str) -> list[dict]:

    lista =  []

    with open(arquivo_csv, mode = 'r' , encoding= 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in  leitor:
            lista.append(linha)

    return lista



## transformação 
def filtrar_produtos_nao_entregues(  lista: list[dict] )->  list[dict]:
    lista_com_produtos_filtrados  = []

    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)

    return lista_com_produtos_filtrados


def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
         valor_total  +=  int(produto.get("price"))
      
    return valor_total


