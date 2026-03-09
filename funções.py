import os

lista_dicionarios = [
{
"nome_produto": "roupa de borracha feminino",
"cod_produto": "001",
"tipo": "vestuario",
"quantidade_estoque": "10",
"preco": "1299",
"detalhes": "roupa de borracha da marca ripcurl tamanho M",
"fornecedor": "RipCurl"
},
{
"nome_produto": "prancha de surf 6.0",
"cod_produto": "002",
"tipo": "equipamento",
"quantidade_estoque": "5",
"preco": "2500",
"detalhes": "prancha de surf epoxy tamanho 6.0",
"fornecedor": "SurfTech"
},
{
"nome_produto": "leash surf 6 pés",
"cod_produto": "003",
"tipo": "acessorio",
"quantidade_estoque": "45",
"preco": "120",
"detalhes": "leash resistente para pranchas até 6 pés",
"fornecedor": "FCS"
},
{
"nome_produto": "parafina para prancha",
"cod_produto": "004",
"tipo": "acessorio",
"quantidade_estoque": "80",
"preco": "25",
"detalhes": "parafina para agua tropical",
"fornecedor": "Sticky Bumps"
},
{
"nome_produto": "bermuda surf masculina",
"cod_produto": "005",
"tipo": "vestuario",
"quantidade_estoque": "30",
"preco": "220",
"detalhes": "bermuda elastano para surf",
"fornecedor": "Quiksilver"
},
{
"nome_produto": "camiseta uv surf",
"cod_produto": "006",
"tipo": "vestuario",
"quantidade_estoque": "60",
"preco": "180",
"detalhes": "camiseta proteção UV fator 50",
"fornecedor": "RipCurl"
}
]
def voltar_ao_menu_principal():
    from main import voltar_ao_menu_principal as _voltar
    _voltar()

def finalizar_app():
    exibir_subtitulo("finalizando o app")

def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def estoque_adicionar_produto():
    exibir_subtitulo("cadastro de produtos")
    nome_produto = input("digite o nome do produto que deseja cadastrar: ")
    if not nome_produto.strip():
        print("erro: o nome do produto não pode estar vazio")
        voltar_ao_menu_principal()
        return True
    elif nome_produto:
        print(f"o produto {nome_produto} foi cadastrado com sucesso")
    
    while True:
        categoria = input(f"digite o nome da categoria do produto {nome_produto} - escolha entre as opcoes vestuario, calcado ou acessorio:")
        if categoria == "vestuario":
                print (f"o produto {nome_produto} foi cadastrado com sucesso na categoria vestuario")
                break
        if categoria == "calcado":
                print (f"o produto {nome_produto} foi cadastrado com sucesso na categoria calcado")
                break
        if categoria == "acessorio":
                print (f" o produto {nome_produto} foi cadastrado com sucesso na categoria acessorio")
                break
        elif categoria:
            print("digite uma categoria válida")

    dados_do_produto= {"titulo": nome_produto, "tipo": categoria, "ativo": True}
    lista_dicionarios.append(dados_do_produto)
    voltar_ao_menu_principal()

def estoque_excluir_produto():
    exibir_subtitulo("exclusao de produtos")
    nome_produto = input("digite o nome do produto que deseja excluir:  ")

    for produto in lista_dicionarios:
        if produto["nome_produto"] == nome_produto:
            lista_dicionarios.remove(produto)
            print(f"o produto {nome_produto} foi removido com sucesso")
    voltar_ao_menu_principal()

    print("produto nao encontrado")
    voltar_ao_menu_principal()

def listar_produtos():
    exibir_subtitulo("produtos em estoque")

    if not lista_dicionarios:
        print("nenhum produto cadastrado")
        voltar_ao_menu_principal()
        return

    for produto in lista_dicionarios:
        print(f"produto: {produto['nome_produto']}")
        print(f"codigo: {produto['cod_produto']}")
        print(f"tipo: {produto['tipo']}")
        print(f"quantidade em estoque: {produto['quantidade_estoque']}")
        print(f"preco: {produto['preco']}")
        print("-" * 30)

    voltar_ao_menu_principal()

def estoque_atualizar():

    exibir_subtitulo("atualizacao do numero de produtos em estoque")
    nome_produto = input ("digite o nome do produto que voce quer atualizar o estoque: ")

    for produto in lista_dicionarios:
         if produto["nome_produto"].lower() == nome_produto.lower():
              nova_quantidade = input("digite a nova quantidade em estoque: ")
              produto["quantidade_estoque"] = nova_quantidade
              print(f"o estoque do produto{nome_produto} foi atualizado para {nova_quantidade}")
    voltar_ao_menu_principal()

def estoque_alerta():
    exibir_subtitulo("produtos com estoque abaixo de 50 unidades")

    encontrou_produto = False

    for produto in lista_dicionarios:
        if int(produto["quantidade_estoque"]) < 50:
            print(f"{produto['nome_produto']} - estoque: {produto['quantidade_estoque']}")
            encontrou_produto = True

    if not encontrou_produto:
        print("nenhum produto com estoque baixo")

    voltar_ao_menu_principal()

def listar_produtos():
    exibir_subtitulo("produtos em estoque")

    if not lista_dicionarios:
        print("nenhum produto cadastrado")
        voltar_ao_menu_principal()
        return

    for produto in lista_dicionarios:
        print(f"produto: {produto['nome_produto']}")
        print(f"codigo: {produto['cod_produto']}")
        print(f"tipo: {produto['tipo']}")
        print(f"quantidade em estoque: {produto['quantidade_estoque']}")
        print(f"preco: {produto['preco']}")
        print("-" * 30)

    voltar_ao_menu_principal()
