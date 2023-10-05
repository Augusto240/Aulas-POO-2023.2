"""
Escreva um programa que solicite do usuário dois valores positivos e
imprima todos os números inteiros dentro desse intervalo. O algoritmo
deve armazenar cada valor em duas variáveis diferentes (v_ini e v_fim).
"""
v_ini = int(input("Digite o início: "))
v_fim = int(input("Digite o fim: "))

while v_ini < v_fim:
    print(v_ini)
    v_ini += 1