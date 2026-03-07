class GeradorSenha:

    contador_geral = 0
    contador_prioritario = 0

    def gerar(self, tipo):

        if tipo == "PRIORITARIO":
            GeradorSenha.contador_prioritario += 1
            return f"P-{GeradorSenha.contador_prioritario:03}"

        else:
            GeradorSenha.contador_geral += 1
            return f"G-{GeradorSenha.contador_geral:03}"