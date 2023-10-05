"""
Escreva um programa que solicite do usuário dois valores positivos e
imprima todos os números inteiros dentro desse intervalo excluindo-se o
valor inicial do intervalo e o valor final.
"""

inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

while inicio < fim:
    print(inicio - 1)
    inicio += 1