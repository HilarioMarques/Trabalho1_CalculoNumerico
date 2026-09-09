class NewtonRaphson:

    def __init__(self, funcao):
        self.funcao = funcao

    def resolver(self, x0, epsilon):

        historico = []

        erro_relativo = float("inf") #Começando com erro infinito para garantir que o while execute

        iteracao = 1

        while erro_relativo > epsilon:

            fx = self.funcao.f(x0) #Calcula f(Xn)

            dfx = self.funcao.df(x0) ##Calcula a derivada f(Xn)

            if dfx == 0:
                raise ValueError(
                    "Derivada igual a zero. Newton-Raphson não pode continuar."
                )

            x1 = x0 - fx / dfx #Formula de newton

            erro_relativo = abs((x1 - x0) / x1)

            historico.append({
                "iteracao": iteracao,
                "xn": x0,
                "f(xn)": fx,
                "f'(xn)": dfx,
                "xn+1": x1,
                "erro_relativo": erro_relativo
            })

            x0 = x1

            iteracao += 1

        return x0, historico