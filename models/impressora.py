from datetime import datetime

class Impressora:

    def imprimir_ticket(self, paciente, tipo, servico, senha):

        print("\n------------------------------------------")
        print("TICKET DE ATENDIMENTO")
        print("------------------------------------------")

        print(f"PACIENTE: {paciente.nome}")

        if tipo == "PRIORITARIO":
            print("TIPO: PRIORITÁRIO (Lei 10.048)")
        else:
            print("TIPO: Geral")

        print(f"SERVIÇO: {servico}")
        print(f"SENHA: {senha}")

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"DATA: {data}")

        print("------------------------------------------")
        print("Aguarde ser chamado no painel central.")