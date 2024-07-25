'''
Aula 4 - 2024-07-23
@author: Marcos Melo
Exercício 2 - parte 2
'''

def main() :
    # Solicitar ao utilizador o número do trimestre
    trimestre = int(input("Digite o número do trimestre [1 a 4]: "))
    trim_meses(trimestre)

def trim_meses(trimestre) :
    # Dicionário com os meses do ano
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
             7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    
    mesTrimestre = []
    inicio = 0 # mês ínicio trimestre
    fim = 0 # mês fim trimestre
    validate = False # variável para validar se existe mensagem
    
    # Verificar o trimestre e atribuir valores as variáveis correspondentes
    if trimestre == 1:
        inicio = 1
        fim = 3
        validate = True         
    elif trimestre == 2:
        inicio = 4
        fim = 6   
        validate = True 
    elif trimestre == 3:
        inicio = 7
        fim = 9 
        validate = True   
    elif trimestre == 4:
        inicio = 10
        fim = 12 
        validate = True   
    else:
        validate = False
    
    # Fazer o teste para ver se as variáveis estão atribuidas antes de retornar a mensagem
    # Impressão das mensagens
    if validate:
        for mes in range(inicio, fim+1): # Loop para obter os meses do trimestre
            mesTrimestre.append(meses[mes])        
        mensagem = f"Os meses do {trimestre}º trimestre são: {mesTrimestre[0]}, {mesTrimestre[1]} e {mesTrimestre[2]}."
        print(f"{mensagem:^80}")
    else:        
        mensagem = "--> Valor errado! Por favor, digite o número do trimestre de 1 a 4. <--"
        print(f"{mensagem:>100}")

main()