#Exercício 01
"""
Escreva uma função que receba uma tupla de números inteiros e retorne uma nova tupla com os elementos pares da tupla original.
Por exemplo, se a tupla for (1, 2, 3, 4, 5), a função deve retornar (2, 4)
"""

def eh_par(tupla):   
    pares = tuple(i for i in tupla if i % 2 == 0)
    return pares

numeros_inteiros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nova_tupla = eh_par(numeros_inteiros)
print(nova_tupla) 