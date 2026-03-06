from paciente import Pacientes
class triagem:
     def emergencia(self):
         print(f"Paciente: {Pacientes.nome},\n"
              "STATUS: RISCO GRAVE DE VIDA. \n" 
              ">>> ATENÇÃO: Encaminhe-se IMEDIATAMENTE\n"
               "ao balcão de triagem médica.\n"
               "Não é necessário aguardar senha.\n")
