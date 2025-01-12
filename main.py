from elt import ler_csv ,filtrar_produtos_nao_entregues , somar_valores_dos_produtos

path_arquivo = "vendas.csv"
lista_de_produtos = ler_csv(path_arquivo)
produtos_entrgues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entrgues)

print(produtos_entrgues)
print(valor_dos_produtos_entregues)