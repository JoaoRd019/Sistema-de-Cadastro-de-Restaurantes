import os

restaurantes = [{"nome": "MC Donalds", "categoria":"Lanche", "ativo": False},
                {"nome": "burger king", "categoria":"Lanche", "ativo": True}]

def exibir_nome_do_programa():
    print(""""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀\n""")
    
def exibir_opcoes():
    print("""1.Cadastrar Restaurante
2.Listar Restaurante
3.Ativar Restaurante
4.Sair\n""")

def finalizar_app():
    exibir_subtitulo("Finalizando App")

def opcao_invalida():
    print("Opção invalida\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurantes = {"nome":nome_do_restaurante, "categoria":categoria_restaurante, "ativo":False}
    restaurantes.append(dados_restaurantes)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    
    print(f"{"Nome restaurante".ljust(15)} | {"Categoria".ljust(15)} | {"Status".ljust(15)}")
    for i in restaurantes:
        nome_restaurante = i["nome"]
        categoria = i["categoria"]
        ativo = "Ativado"if i["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(15)}| {categoria.ljust(15)} | {ativo}")

    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()
     
def exibir_subtitulo(texto):
    os.system("cls")
    linha = "▫️" * len(texto)
    print(linha)
    print(texto,"")
    print(linha,"\n")


def status_restaurantes():
    exibir_subtitulo("Alterando status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar status: ATIVO/DESATIVADO: ")
    restaurante_encontrado = False
    for i in restaurantes:
        if nome_restaurante == i["nome"]:
            restaurante_encontrado = True
            i["ativo"] = not i["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com suscesso" if i["ativo"] else f"O restaurante {nome_restaurante} foi desativado com suscesso"
            print(mensagem)
        if not restaurante_encontrado:
             print("O restaurante nao foi encontrado")
    
    
    voltar_ao_menu_principal()

def escolher_opcao():
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
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
