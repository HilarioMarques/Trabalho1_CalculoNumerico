# Trabalho1_CalculoNumerico

## Integrantes

- Hilário
- Luca
- Ryan

## Objetivo

Desenvolver um sistema para encontrar raízes da função:

f(d) = a·e^d - 4d²

utilizando os métodos numéricos:

- Bisseção
- Newton-Raphson

---

## Função Utilizada

A função estudada foi:

f(d) = a·e^d - 4d²

e sua derivada:

f'(d) = a·e^d - 8d

---

## Métodos Implementados

### Método da Bisseção

Método baseado na divisão sucessiva de um intervalo que contém uma raiz.

Condição de aplicação:

f(a) · f(b) < 0

---

### Método de Newton-Raphson

Método iterativo baseado na fórmula:

x(n+1) = x(n) - f(x(n))/f'(x(n))

Utiliza a derivada da função para acelerar a convergência.

---

## Resultados Obtidos

### Teste padrão

Parâmetros:

- a = 1
- intervalo = (0,1)
- ε = 10^-4

### Bisseção

- Raiz encontrada: 0.714783
- Iterações: 13

### Newton-Raphson

- Raiz encontrada: 0.714806
- Iterações: 4

---

## Comparação dos Métodos

| Método | Raiz | Iterações |
|----------|----------|----------|
| Bisseção | 0.714783 | 13 |
| Newton-Raphson | 0.714806 | 4 |

Observa-se que ambos encontraram praticamente a mesma raiz.

O método de Newton-Raphson apresentou convergência significativamente mais rápida.

---

## Análise do Parâmetro a

Foi realizada uma análise para diferentes valores de a.

Observou-se que:

- existem raízes para valores de a menores que aproximadamente 2.165;
- para a ≈ 2.165 ocorre o caso limite;
- para valores maiores que 2.165 não existem raízes reais.

O valor crítico foi obtido a partir da análise da função:

a = 4d²e^(-d)

resultando em:

a_critico = 16/e² ≈ 2.165

---

## Diagrama de Classes

(colocar aqui a imagem do diagrama)

+--------------------------------------------------+
|                 FuncaoMovimento                  |
+--------------------------------------------------+
| - a : float                                      |
+--------------------------------------------------+
| + f(d : float) : float                           |
| + df(d : float) : float                          |
+--------------------------------------------------+

                ▲                    ▲
                |                    |
                | utiliza            | utiliza
                |                    |

+----------------------------+   +----------------------------+
|          Bissecao          |   |      NewtonRaphson        |
+----------------------------+   +----------------------------+
| - funcao : FuncaoMovimento |   | - funcao : FuncaoMovimento |
+----------------------------+   +----------------------------+
| + resolver()               |   | + resolver()               |
+----------------------------+   +----------------------------+

---

## Tecnologias Utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook
