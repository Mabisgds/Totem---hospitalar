
from paciente import Pacientes

class Classificador:
    def __init__(self, ficha):
        self.ficha = ficha

    def classificar(self):
        if self.ficha["pcd"] == "s" or self.ficha["idade"] >= 60:
            return "Prioridade Alta"

        elif 45 <= self.ficha["idade"] < 60:
            return "Prioridade Média"

        else:
            return "Prioridade Baixa"