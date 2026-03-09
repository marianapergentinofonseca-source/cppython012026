import os
from funcoes import *


def exibir_nome_do_programa():
    nome =("Cadastro de produtos - MAJ comercio de sportswear")
    print(nome)

def exibir_opcoes():
    print("1.Gestão de estoque -  adicionar produto")
    print("2. Gestão de estoque -  excluir produto")
    print("3. Gestão de estoque -  atualizar estoque")
    print("4. Gestão de estoque -  alerta de estoque")
    print("5. Listar produtos")
    print("0.Sair\n")

def voltar_ao_menu_principal():
    input("digite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("opcao inválida\n")
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("escolha uma opcao: "))
        if opcao_escolhida == 1:
            estoque_adicionar_produto()
        elif opcao_escolhida == 2:
            estoque_excluir_produto()
        elif opcao_escolhida == 3:
            estoque_atualizar()
        elif opcao_escolhida == 4:
            estoque_alerta()
        elif opcao_escolhida == 5:
            listar_produtos()    
        elif opcao_escolhida ==0:
            finalizar_app()
            return False
        else:
            opcao_invalida()
            return False
    except ValueError:
        print("Por favor, digite um número válido.")
        voltar_ao_menu_principal()

def main():
    while True:
        os.system("clear")
        exibir_nome_do_programa()
        exibir_opcoes()
        if not escolher_opcoes():
            break    
if __name__ == '__main__':
    main()
