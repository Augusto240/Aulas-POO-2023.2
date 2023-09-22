quantos = int(input("Quantos usuários irão responder a pergunta? "))
contador = 0
insatisfeito = 0
satisfeito = 0
nao_responder = 0
while contador < quantos:
    pesquisa = int(input("Qual sua opinião sobre o atendimento na farmácia? \n 1 - INSATISFEITO / 2 - SATISFEITO / OUTRO - NÃO QUERO RESPONDER "))
    if pesquisa == 1:
        insatisfeito += 1
    elif pesquisa == 2:
        satisfeito +=1
    else:
        nao_responder += 1
    contador += 1
print(insatisfeito)   
print(satisfeito)
print(nao_responder)
# Porcentagem = (parte/total) * 100

total = quantos
porcentagem_insatisfeito = (insatisfeito / total) * 100
porcentagem_satisfeito = (satisfeito / total ) * 100
porcentagem_nao_respondeu = (nao_responder / total) * 100

print("A porcentagem é: ")
print()
print(f'{porcentagem_insatisfeito}% estão insatisfeitos')
print(f'{porcentagem_satisfeito}% estão satisfeitos')
print(f'{porcentagem_nao_respondeu}% não responderam')




