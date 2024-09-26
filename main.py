from cadastrarFuncionario import cadatrar_funcionario
from registroPonto import registrar_ponto
from conexao import conectar
import getpass

def login_admin():
    usuario = input("Usuario: ")
    senha = getpass.getpass("Senha: ")


    if usuario == "admin" and senha == "admin":
        print("login realizado com sucesso!")
        return True
    else:
        print("Usuario ou senha incorretos")
        return True


def verificar_ponto(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT entrada_manha, saida_manha, entrada_tarde, saida_tarde FROM registroPonto WHERE id_funcionario = (SELECT id FROM funcionarios WHERE cpf = %s)"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchone()

    if resultado:
        entrada_manha, saida_manha, entrada_tarde, saida_tarde = resultado
        pontos_restantes = []
        if entrada_manha is None:
            pontos_restantes.append("entrada_manha")
        if saida_manha is None:
            pontos_restantes.append("saida_manha")
        if entrada_tarde is None:
            pontos_restantes.append("entrada_tarde")
        if saida_tarde is None:
            pontos_restantes.append("saida_tarde")

        cursor.close()
        conexao.close()

        if pontos_restantes:
            print(f"Voce ainda não precisa registar os segiuntes pontos: {', '.join(pontos_restantes)}")
            return pontos_restantes
        else:
            print("Todos os pontos foram registrados para hoje")
            return []
    
    else:
        print("Nenhum ponto registrado ainda.")
        return ["entrada_manha", "saida_manha", "entrada_tarde", "saida_tarde"]


def voltarParaMenu():
    print("\nDigite 'voltar' para retornar ao menu principal a qualquer momento.")
    opcao = input("Pressione Enter para continuar ou digite 'voltar': ").lower()
    if opcao == 'voltar':
        return True  
    return False  

def menu():

    while True:
        print("\n1 - Cadastrar Funcionario (Somente Admin)")
        print("2 - Registrar Ponto (Funcionario)")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            if voltarParaMenu():
                continue
            if not cadastrarFuncionarioMenu():
                continue
        elif opcao == "2":
            if voltarParaMenu():
                continue
            if not registrarPontoMenu():
                continue
        elif opcao == "3":
            print("Encerrando o Sistema")
            break
        else:
            print("Codigo Invalido")


def cadastrarFuncionarioMenu():

    while True:
        print("\n1- Continuar com o cadastro do funcionario")
        print("2- voltar ao Menu Principal")
                 
        opcaoCad = input("\nEscolha uma Opção: ")

        if opcaoCad == "1":
            print("Se você deseja voltar ao menu principal digite 'voltar' a qualquer momento")

            if login_admin():
                nome = input("Nome: ")
                if nome.lower() == "voltar":
                    return False
                cargo = input("Cargo: ")
                if cargo.lower() == "voltar":
                    return False
                cpf = input("CPF: ")
                if cpf.lower() == "voltar":
                    return False
                
                cadatrar_funcionario(nome, cargo, cpf)
                print(f"Funcionario {nome} cadastrado com Sucesso!")
        elif opcaoCad == "2":
            return False
        else:
            print("Opção Invalida")

def registrarPontoMenu():

    while True:

        print("\n1 - Continuar com Registro de Ponto")
        print("2 - Voltar ao Menu Principal")
    
        opcaoReg = input("\nEscolha uma Opção: ")

        if opcaoReg == "1":
            cpf = input("Digite seu CPF (Matricula): ")
            pontos_restantes = verificar_ponto(cpf)

            if pontos_restantes:
                print("\nSeleciona o ponto que deseja registar: ")
                for idx, ponto in enumerate(pontos_restantes):
                    
                    print(f"{idx + 1} - Registrar {ponto.replace('_', ' ').title()}")
                
                opcaoPonto = int(input("\nEscolha uma Opção: ")) - 1

                if 0 <= opcaoPonto < len(pontos_restantes):
                    registrar_ponto(cpf, pontos_restantes[opcaoPonto])
                    print(f"Ponto {pontos_restantes[opcaoPonto].replace('_', ' ').title()} registrado com sucesso!")
                    pontos_restantes.pop(opcaoPonto)
                else:
                    print("Opção Inválida")
            return True
        elif opcaoReg == "2":
            return False
        else:
            print("Opção Inválida")


if __name__ == "__main__":
    menu()
            