import os
from datetime import datetime


lista_dicionarios = [
    {
        "nome_produto": "roupa de borracha feminino",
        "cod_produto": "001",
        "tipo": "vestuario",
        "quantidade_estoque": 10,
        "preco": 1299.00,
        "detalhes": "roupa de borracha da marca ripcurl tamanho M",
        "fornecedor": "RipCurl",
        "desconto": 0
    },
    {
        "nome_produto": "prancha de surf 6.0",
        "cod_produto": "002",
        "tipo": "equipamento",
        "quantidade_estoque": 5,
        "preco": 2500.00,
        "detalhes": "prancha de surf epoxy tamanho 6.0",
        "fornecedor": "SurfTech",
        "desconto": 0
    },
    {
        "nome_produto": "leash surf 6 pés",
        "cod_produto": "003",
        "tipo": "acessorio",
        "quantidade_estoque": 45,
        "preco": 120.00,
        "detalhes": "leash resistente para pranchas até 6 pés",
        "fornecedor": "FCS",
        "desconto": 0
    },
    {
        "nome_produto": "parafina para prancha",
        "cod_produto": "004",
        "tipo": "acessorio",
        "quantidade_estoque": 80,
        "preco": 25.00,
        "detalhes": "parafina para agua tropical",
        "fornecedor": "Sticky Bumps",
        "desconto": 0
    },
    {
        "nome_produto": "bermuda surf masculina",
        "cod_produto": "005",
        "tipo": "vestuario",
        "quantidade_estoque": 30,
        "preco": 220.00,
        "detalhes": "bermuda elastano para surf",
        "fornecedor": "Quiksilver",
        "desconto": 0
    },
    {
        "nome_produto": "camiseta uv surf",
        "cod_produto": "006",
        "tipo": "vestuario",
        "quantidade_estoque": 60,
        "preco": 180.00,
        "detalhes": "camiseta proteção UV fator 50",
        "fornecedor": "RipCurl",
        "desconto": 0
    }
]


lista_vendas = []
lista_movimentacoes = []


def voltar_ao_menu_principal():
    from main import voltar_ao_menu_principal as _voltar
    _voltar()


def finalizar_app():
    exibir_subtitulo("Finalizando o app")


def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print("-" * 40)


def buscar_produto_por_codigo(codigo):
    for produto in lista_dicionarios:
        if produto["cod_produto"] == codigo:
            return produto
    return None


def registrar_movimentacao(tipo_movimentacao, produto, quantidade, observacao):
    movimentacao = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "tipo_movimentacao": tipo_movimentacao,
        "produto": produto,
        "quantidade": quantidade,
        "observacao": observacao
    }

    lista_movimentacoes.append(movimentacao)


def estoque_adicionar_produto():
    exibir_subtitulo("Cadastro de produtos")

    nome_produto = input("Digite o nome do produto que deseja cadastrar: ")

    if not nome_produto.strip():
        print("Erro: o nome do produto não pode estar vazio.")
        voltar_ao_menu_principal()
        return

    cod_produto = input("Digite o código do produto: ")
    categoria = input("Digite a categoria do produto: ")

    try:
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Erro: quantidade e preço devem ser valores numéricos.")
        voltar_ao_menu_principal()
        return

    detalhes = input("Digite os detalhes do produto: ")
    fornecedor = input("Digite o fornecedor do produto: ")

    dados_do_produto = {
        "nome_produto": nome_produto,
        "cod_produto": cod_produto,
        "tipo": categoria,
        "quantidade_estoque": quantidade,
        "preco": preco,
        "detalhes": detalhes,
        "fornecedor": fornecedor,
        "desconto": 0
    }

    lista_dicionarios.append(dados_do_produto)

    registrar_movimentacao(
        "Entrada de estoque",
        nome_produto,
        quantidade,
        "Produto cadastrado no sistema"
    )

    print(f"\nO produto {nome_produto} foi cadastrado com sucesso.")
    voltar_ao_menu_principal()


def estoque_excluir_produto():
    exibir_subtitulo("Exclusão de produtos")

    codigo = input("Digite o código do produto que deseja excluir: ")
    produto = buscar_produto_por_codigo(codigo)

    if produto:
        quantidade_removida = produto["quantidade_estoque"]
        nome_produto = produto["nome_produto"]

        lista_dicionarios.remove(produto)

        registrar_movimentacao(
            "Remoção de estoque",
            nome_produto,
            quantidade_removida,
            "Produto excluído do sistema"
        )

        print(f"O produto {nome_produto} foi removido com sucesso.")
    else:
        print("Produto não encontrado.")

    voltar_ao_menu_principal()


def listar_produtos():
    exibir_subtitulo("Produtos em estoque")

    if not lista_dicionarios:
        print("Nenhum produto cadastrado.")
        voltar_ao_menu_principal()
        return

    for produto in lista_dicionarios:
        preco = produto["preco"]
        desconto = produto["desconto"]
        preco_com_desconto = preco - (preco * desconto / 100)

        print(f"Produto: {produto['nome_produto']}")
        print(f"Código: {produto['cod_produto']}")
        print(f"Tipo: {produto['tipo']}")
        print(f"Quantidade em estoque: {produto['quantidade_estoque']}")
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Desconto: {desconto}%")
        print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
        print("-" * 40)

    voltar_ao_menu_principal()


def estoque_atualizar():
    exibir_subtitulo("Atualização do estoque")

    codigo = input("Digite o código do produto que você quer atualizar: ")
    produto = buscar_produto_por_codigo(codigo)

    if produto:
        quantidade_anterior = produto["quantidade_estoque"]

        try:
            nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        except ValueError:
            print("Erro: a quantidade deve ser um número inteiro.")
            voltar_ao_menu_principal()
            return

        produto["quantidade_estoque"] = nova_quantidade

        diferenca = nova_quantidade - quantidade_anterior

        if diferenca > 0:
            tipo_movimentacao = "Entrada de estoque"
            observacao = "Aumento manual da quantidade em estoque"
        elif diferenca < 0:
            tipo_movimentacao = "Remoção de estoque"
            observacao = "Redução manual da quantidade em estoque"
        else:
            tipo_movimentacao = "Atualização sem alteração"
            observacao = "A quantidade permaneceu igual"

        registrar_movimentacao(
            tipo_movimentacao,
            produto["nome_produto"],
            abs(diferenca),
            observacao
        )

        print(f"O estoque do produto {produto['nome_produto']} foi atualizado para {nova_quantidade}.")
    else:
        print("Produto não encontrado.")

    voltar_ao_menu_principal()


def estoque_alerta():
    exibir_subtitulo("Produtos com estoque abaixo de 50 unidades")

    encontrou_produto = False

    for produto in lista_dicionarios:
        if produto["quantidade_estoque"] < 50:
            print(f"{produto['nome_produto']} - estoque: {produto['quantidade_estoque']}")
            encontrou_produto = True

    if not encontrou_produto:
        print("Nenhum produto com estoque baixo.")

    voltar_ao_menu_principal()


def aplicar_desconto_promocao():
    exibir_subtitulo("Aplicar desconto ou promoção")

    codigo = input("Digite o código do produto: ")
    produto = buscar_produto_por_codigo(codigo)

    if produto:
        try:
            desconto = float(input("Digite o percentual de desconto: "))
        except ValueError:
            print("Erro: o desconto deve ser um número.")
            voltar_ao_menu_principal()
            return

        if desconto < 0 or desconto > 100:
            print("Desconto inválido. Digite um valor entre 0 e 100.")
        else:
            produto["desconto"] = desconto
            print(f"Desconto de {desconto}% aplicado ao produto {produto['nome_produto']}.")
    else:
        print("Produto não encontrado.")

    voltar_ao_menu_principal()


def registrar_venda():
    exibir_subtitulo("Registro de venda")

    codigo = input("Digite o código do produto vendido: ")
    produto = buscar_produto_por_codigo(codigo)

    if not produto:
        print("Produto não encontrado.")
        voltar_ao_menu_principal()
        return

    try:
        quantidade_vendida = int(input("Digite a quantidade vendida: "))
    except ValueError:
        print("Erro: a quantidade vendida deve ser um número inteiro.")
        voltar_ao_menu_principal()
        return

    if quantidade_vendida <= 0:
        print("A quantidade vendida deve ser maior que zero.")
        voltar_ao_menu_principal()
        return

    if quantidade_vendida > produto["quantidade_estoque"]:
        print("Estoque insuficiente para realizar a venda.")
        print(f"Quantidade disponível: {produto['quantidade_estoque']}")
        voltar_ao_menu_principal()
        return

    preco_original = produto["preco"]
    desconto = produto["desconto"]
    preco_final_unitario = preco_original - (preco_original * desconto / 100)
    valor_total = preco_final_unitario * quantidade_vendida

    produto["quantidade_estoque"] -= quantidade_vendida

    registrar_movimentacao(
        "Saída por venda",
        produto["nome_produto"],
        quantidade_vendida,
        "Venda registrada e estoque atualizado automaticamente"
    )

    venda = {
        "produto": produto["nome_produto"],
        "codigo": produto["cod_produto"],
        "quantidade": quantidade_vendida,
        "preco_unitario": preco_original,
        "desconto": desconto,
        "preco_final_unitario": preco_final_unitario,
        "valor_total": valor_total,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    lista_vendas.append(venda)

    emitir_recibo(venda)

    voltar_ao_menu_principal()


def emitir_recibo(venda):
    print("\n" + "=" * 40)
    print("RECIBO DE VENDA - MAJ SPORTSWEAR")
    print("=" * 40)
    print(f"Data: {venda['data']}")
    print(f"Produto: {venda['produto']}")
    print(f"Código: {venda['codigo']}")
    print(f"Quantidade vendida: {venda['quantidade']}")
    print(f"Preço unitário original: R$ {venda['preco_unitario']:.2f}")
    print(f"Desconto aplicado: {venda['desconto']}%")
    print(f"Preço unitário final: R$ {venda['preco_final_unitario']:.2f}")
    print(f"Valor total da venda: R$ {venda['valor_total']:.2f}")
    print("=" * 40)
    print("Venda registrada com sucesso.")
    print("Estoque atualizado automaticamente.")


def listar_vendas():
    exibir_subtitulo("Vendas realizadas")

    if not lista_vendas:
        print("Nenhuma venda registrada.")
        voltar_ao_menu_principal()
        return

    for venda in lista_vendas:
        print(f"Data: {venda['data']}")
        print(f"Produto: {venda['produto']}")
        print(f"Código: {venda['codigo']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Valor total: R$ {venda['valor_total']:.2f}")
        print("-" * 40)

    voltar_ao_menu_principal()


def relatorio_vendas():
    exibir_subtitulo("Relatório detalhado de vendas")

    if not lista_vendas:
        print("Nenhuma venda registrada.")
        voltar_ao_menu_principal()
        return

    valor_total_geral = 0
    quantidade_total_vendida = 0

    for venda in lista_vendas:
        print(f"Data da venda: {venda['data']}")
        print(f"Produto vendido: {venda['produto']}")
        print(f"Código do produto: {venda['codigo']}")
        print(f"Quantidade vendida: {venda['quantidade']}")
        print(f"Preço unitário final: R$ {venda['preco_final_unitario']:.2f}")
        print(f"Valor total da venda: R$ {venda['valor_total']:.2f}")
        print("-" * 40)

        valor_total_geral += venda["valor_total"]
        quantidade_total_vendida += venda["quantidade"]

    print("Resumo geral")
    print("-" * 40)
    print(f"Quantidade total de itens vendidos: {quantidade_total_vendida}")
    print(f"Valor total vendido: R$ {valor_total_geral:.2f}")

    voltar_ao_menu_principal()


def relatorio_estoque():
    exibir_subtitulo("Relatório de estoque atual")

    if not lista_dicionarios:
        print("Nenhum produto cadastrado.")
        voltar_ao_menu_principal()
        return

    valor_total_estoque = 0
    quantidade_total_produtos = 0

    for produto in lista_dicionarios:
        quantidade = produto["quantidade_estoque"]
        preco = produto["preco"]
        valor_em_estoque = quantidade * preco

        print(f"Produto: {produto['nome_produto']}")
        print(f"Código: {produto['cod_produto']}")
        print(f"Tipo: {produto['tipo']}")
        print(f"Quantidade atual em estoque: {quantidade}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Valor total em estoque: R$ {valor_em_estoque:.2f}")
        print("-" * 40)

        quantidade_total_produtos += quantidade
        valor_total_estoque += valor_em_estoque

    print("Resumo geral do estoque")
    print("-" * 40)
    print(f"Quantidade total de itens em estoque: {quantidade_total_produtos}")
    print(f"Valor total estimado do estoque: R$ {valor_total_estoque:.2f}")

    voltar_ao_menu_principal()


def historico_movimentacoes():
    exibir_subtitulo("Histórico de movimentações de estoque")

    if not lista_movimentacoes:
        print("Nenhuma movimentação registrada.")
        voltar_ao_menu_principal()
        return

    for movimentacao in lista_movimentacoes:
        print(f"Data: {movimentacao['data']}")
        print(f"Tipo de movimentação: {movimentacao['tipo_movimentacao']}")
        print(f"Produto: {movimentacao['produto']}")
        print(f"Quantidade movimentada: {movimentacao['quantidade']}")
        print(f"Observação: {movimentacao['observacao']}")
        print("-" * 40)

    voltar_ao_menu_principal()