import os

restaurantes = [{"nome": "MC Donalds", "categoria":"Lanche", "ativo": False},
                {"nome": "burger king", "categoria":"Lanche", "ativo": True}]

def exibir_nome_do_programa():
    """Essa função é para exibir o nome do programa"""
    print(""""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀\n""")
    
def exibir_opcoes():
    """Essa função ée responsavel para exibir as opçoes para o usuario escolher"""
    print("""1.Cadastrar Restaurante
2.Listar Restaurante
3.Ativar Restaurante
4.Sair\n""")

def finalizar_app():
    """Essa função serve para finalizar o programa"""
    exibir_subtitulo("Finalizando App")

def opcao_invalida():
    """Exibe mensagem de opção inválida e retorna ao menu principal """
    print("Opção invalida\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    """Essa funçao é responsavel por cadstrar um novo restaurante"""
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurantes = {"nome":nome_do_restaurante, "categoria":categoria_restaurante, "ativo":False}
    restaurantes.append(dados_restaurantes)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Lista os restaurantes presentes na lista """
    exibir_subtitulo("Listando restaurantes")
    
    print(f"{"Nome restaurante".ljust(15)} | {"Categoria".ljust(15)} | {"Status"}")
    for i in restaurantes:
        nome_restaurante = i["nome"]
        categoria = i["categoria"]
        ativo = "Ativado"if i["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(15)}| {categoria.ljust(15)} | {ativo}")

    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    """Essa função seve para voltar ao menu principal"""
    input("\nDigite uma tecla para voltar ao menu ")
    main()
     
def exibir_subtitulo(texto):
    """Exibe um subtítulo estilizado na tela"""
    os.system("cls")
    linha = "▫️" * len(texto)
    print(linha)
    print(texto,"")
    print(linha,"\n")


def status_restaurantes():
    """Alterar os status do restaurante para ativado ou desativado """
    exibir_subtitulo("Alterando status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar status: ATIVO/DESATIVADO: ")
    restaurante_encontrado = False
    for i in restaurantes:
        if nome_restaurante == i["nome"]:
            restaurante_encontrado = True
            i["ativo"] = not i["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if i["ativo"] else f"O restaurante {nome_restaurante} foi desativado com suscesso"
            print(mensagem)
    if not restaurante_encontrado:
             print("O restaurante nao foi encontrado")
    
    
    voltar_ao_menu_principal()

def escolher_opcao():
    """Solicita e executa a opção escolhida pelo usuário"""
    try:  
        opcao_escolhida = int(input("Escolha uma opçao: "))

        if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
                status_restaurantes()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
         opcao_invalida()
           
def main():
    """Função principal que inicia o programa"""
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()