

class Menu:
    def __init__(self):
        self.executando = True

    def mostrar_menu(self):
        print("\nMENU PRINCIPAL")
        print("Escolha uma opção")
        print("1 - Consulta")
        print("2 - Exame")
        print("3 - Emergência")
        print("0 - Sair")

    def executar(self):
        while self.executando:
            self.mostrar_menu()
            opcao = input("Escolha: ")

            if opcao == "1":
                self.consulta()
            elif opcao == "2":
                self.exame()
            elif opcao == "3":
                self.emergencia()
            elif opcao == "0":
                print("Saindo...")
                self.executando = False
            else:
                print("Opção inválida")


menu = Menu()
menu.executar()