"""
Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo.
"""

inicio_intervalo = int(input("Digite o início do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))

valor = int(input("Digite um valor: "))

if (valor >= inicio_intervalo and valor <= fim_intervalo):
    print("Dentro do Intervalo")
elif (valor < inicio_intervalo):
    print("Fora do Intervalo: Na parte inferior")
elif (valor > fim_intervalo):
    print("Fora do Intervalo: Na parte superior")