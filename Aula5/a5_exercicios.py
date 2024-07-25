'''
Aula 5 - 2024-07-25
@author: Marcos Melo
Exercícios e Testes durante a aula
'''

# Classes
class Cao:
    #Construtor
    def __init__(self, nome, idade, raca) -> None: # __init__ usar para iniciar e definir como construtor
        self.nome = nome # instanciando os atributos as variáveis
        self.idade = idade
        self.raca = raca

    # Definição de Métodos do Cão
    def ladrar(self):
        print(f"Au au, estou a ladrar e sou o {self.nome}") #self busca a variável interna

""" cao1 = Cao('Boby', 2, 'Pastor Alemão') # criando o objeto cao1 do Tipo Cao
cao2 = Cao('Faísca', 5, 'Buldog')
print(cao1.nome) # imprimir a variável nome do objeto
print(cao2.nome) 

cao1.ladrar()"""

class Cachorro (Cao):
    # Definir o Construtor
    def __init__(self, nome, idade, raca, leite, peso) -> None:
        super().__init__(nome, idade, raca)
        self.tipo_leite = leite
        self.peso = peso

    def mamar(self):
        print(f"Eu sou {self.nome} e estou a mamar {self.tipo_leite} porque sou um cachorro")

    def ladrar(self):
        print(f"Béu, Béu, este é o meu ladra. Sou o cachorro {self.nome} e só tenho {self.idade} anos.")
    
    def mostra_tipo_leite(self):
       return self.tipo_leite
    
    def mostra_peso(self):
       return self.peso
    
    def altera_tipo_leite(self, novo_leite):
       self.tipo_leite = novo_leite
       return self.tipo_leite
    
    def altera_peso(self, novo_peso):
       self.peso = novo_peso
       return self.peso
    
    

cao1 = Cao('Boby', 2, 'Pastor Alemão')
cachorro = Cachorro('Piloto', 1, 'Labrador', 'leite materno', 2)

cao1.ladrar()
cachorro.mamar()
cachorro.ladrar()
print("O meu peso é: ", cachorro.mostra_peso())
print("A minha alimentação é: ", cachorro.mostra_tipo_leite())
cachorro.altera_tipo_leite('Leite em pó')
print("A minha alimentação passou a ser: ", cachorro.mostra_tipo_leite)

cachorro.peso = 10
print("O meu peso agora é: ", cachorro.mostra_peso())
