'''
Aula 3 - 2024-07-19
@author: Marcos Melo
Exercício 2 - parte 1
'''

# Dicionário com os meses do ano
MESES = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# Solicitar ao utilizador o número do trimestre
trimestre = int(input("Digite o número do trimestre [1 a 4]: "))

# Verificar o trimestre e mostrar os meses correspondentes
if trimestre == 1:
    meses = [MESES.get(1), MESES.get(2), MESES.get(3)]
    mensagem = "Os meses do 1º trimestre são: %s, %s e %s." % (meses[0], meses[1], meses[2])
    print(f"{mensagem:^80}") # readapte o exemplo do slide Nº98 da aula Nº4

elif trimestre == 2:
    meses = [MESES.get(4), MESES.get(5), MESES.get(6)]
    mensagem = "Os meses do 2º trimestre são: %s, %s e %s." % (meses[0], meses[1], meses[2])
    print(f"{mensagem:^120}")
elif trimestre == 3:
    meses = [MESES.get(7), MESES.get(8), MESES.get(9)]
    mensagem = "Os meses do 3º trimestre são: %s, %s e %s." % (meses[0], meses[1], meses[2])
    print(f"{mensagem:^150}")
elif trimestre == 4:
    meses = [MESES.get(10), MESES.get(11), MESES.get(12)]
    mensagem = "Os meses do 4º trimestre são: %s, %s e %s." % (meses[0], meses[1], meses[2])
    print(f"{mensagem:^180}")
else:
    mensagem = "--> Valor errado! Por favor, digite o número do trimestre de 1 a 4. <--"
    print(f"{mensagem:>100}")

