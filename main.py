from models.paciente import Pacientes
from models.menu import Menu
from models.classificador import Classificador
from models.gerador_senha import GeradorSenha
from models.triagem import triagem
from models.impressora import Impressora

def main():


    print("==========================================")
    print("HOSPITAL VIVER BEM - AUTOATENDIMENTO")
    print("==========================================")

    while True:

        # Cadastro do paciente
        print("\n[CADASTRO DE PACIENTE]")
        paciente = Pacientes("", 0, "")
        paciente.cadastro()

        ficha = paciente.ficha()

        # Classificar paciente
        classificador = Classificador(ficha)
        prioridade = classificador.classificar()

        if prioridade == "Prioridade Alta":
            tipo = "PRIORITARIO"
        else:
            tipo = "GERAL"

        # Menu
        print("\n[MENU DE SERVIÇOS]")
        menu = Menu()
        menu.mostrar_menu()
        opcao = input("Escolha a opção: ")

        if opcao == "0":
            print("Sistema encerrado.")
            break

        # Emergência
        if opcao == "3":
            print("\n------------------------------------------")
            print("ALERTA DE EMERGÊNCIA")
            print("------------------------------------------")

            t = triagem()
            t.emergencia()

        else:

            if opcao == "1":
                servico = "Consulta"
            elif opcao == "2":
                servico = "Exame"
            else:
                print("Opção inválida.")
                continue

            # Gerar senha
            gerador = GeradorSenha()
            senha = gerador.gerar(tipo)

            # Imprimir ticket
            impressora = Impressora()
            impressora.imprimir_ticket(paciente, tipo, servico, senha)


if __name__ == "__main__":
    main()
