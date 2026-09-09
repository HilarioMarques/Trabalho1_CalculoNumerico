class Bissecao:

    def __init__(self, funcao): #Recebe a função matemática que será usada
        self.funcao = funcao

    def resolver(self, a, b, epsilon):
        """
        Método da Bisseção.

        Parâmetros:
            a -> limite inferior
            b -> limite superior
            epsilon -> tolerância do erro

        Retorna:
            raiz aproximada
            histórico das iterações
        """

        historico = [] #Guardando cada passo

        xm_anterior = None

        while (b - a) / 2 > epsilon: #Quando o intervalo ficar muito pequeno, o while para

            meio = (a + b) / 2 #A Bisseção sempre divide o intervalo ao meio

            if xm_anterior is None:
                erro_relativo = None
            else:
                erro_relativo = abs((meio - xm_anterior) / meio)

            historico.append({
                "iteracao": len(historico) + 1,
                "a": a,
                "b": b,
                "xm": meio,
                "f(xm)": self.funcao.f(meio),
                "erro_relativo": erro_relativo
            })

            #Aqui tá sendo feito o teste do sinal se no primeiro if os sinais forem diferentes 
            #[a ----- meio] contém raiz, então descartamos a metade direita. Caso contrário
            #[meio ----- b] então descartamos a metade esquerda

            if self.funcao.f(a) * self.funcao.f(meio) < 0:
                b = meio
            else:
                a = meio

            xm_anterior = meio

        raiz = (a + b) / 2

        return raiz, historico