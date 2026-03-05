class Paciente:
    def __init__(self, nome, idade, pcd):
        self.nome = nome
        self.idade = idade
        self.pcd = pcd

    def ficha(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "pcd": self.pcd
        }
    
    def cadastro(self):
        print("Insira seu nome: ")
        self.nome = input()
        print("Insira sua idade: ")
        self.idade = int(input())
        print("possui deficiência? (s/n): ")
        pcd_input = input().lower()
        self.pcd = True if pcd_input == "s" else False
