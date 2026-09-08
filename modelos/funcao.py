import numpy as np

class FuncaoMovimento:

    """
    Classe responsável por representar a função matemática
    do problema e sua derivada.

    Separar a função dos métodos numéricos facilita a manutenção
    do código e permite trocar a equação sem alterar os algoritmos
    de Bisseção e Newton-Raphson.
    """

    def __init__(self, a):
        self.a = a

    def f(self, d):
        """
        Calcula o valor da função:

        f(d) = a*e^d - 4*d²

        Parâmetros:
            d -> deslocamento

        Retorno:
            valor da função em d
        """

        return self.a * np.exp(d) - 4 * d**2

    def df(self, d):
        """
        Calcula a derivada da função:

        f'(d) = a*e^d - 8*d

        Necessária para o método de Newton-Raphson.
        """

        return self.a * np.exp(d) - 8 * d

    