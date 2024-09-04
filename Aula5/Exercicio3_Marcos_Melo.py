'''
Aula 5 - 2024-07-25
@author: Marcos Melo
Exercícios 3 - Classes
'''

# Classe Pessoa


class Person:
    # Construtor
    # __init__ usar para iniciar e definir como construtor
    def __init__(self, name, age, nif) -> None:
        self.name = name  # instanciando os atributos as variáveis
        self.age = age
        self.nif = nif

    # Retorna o nome
    def getName(self):
        return self.name

    # Retorna a idade
    def getAge(self):
        return self.age

    # Retorna o NIF
    def getNIF(self):
        return self.nif
    
    # Atribui uma nova idade
    def setAge(self, age):
        self.age = age

    # Imprime todas as informações da Pessoa
    def printInfo(self):
        print("######### INFORMAÇÃO PESSOAL #########\n")
        print(f"Nome: {self.name}\nIdade: {self.age}\nNIF: {self.nif}")
        print("\n######### #################### #########\n")

# Escola 1 - Curso de Programador


class BestSchool (Person): # herda da classe Person
    # Definir o Construtor
    def __init__(self, name, age, nif, progLang, level) -> None:
        super().__init__(name, age, nif) # herda características da classe Person
        self.course = "Programador de Informática"  # tipo do curso
        self.progLang = progLang  # linguagem de programação
        # nível de conhecimento, classificado por 1, 2 e 3 (3 é o máximo)
        self.level = level

    # Obter informações individuais do aluno
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getNif(self):
        return self.nif

    def getProgLang(self):
        return self.progLang

    def getLevel(self):
        return self.level
    
     # Atribui um novo nível de conhecimento
    def setLevel(self, level):
        self.level = level
        return self.level

    # Imprime o Nome do aluno, nível e curso
    def myCourse(self):
        print(f"Eu sou {self.name} e estou a estudar a linguagem de programação {
              self.progLang} do curso de {self.course}\n")

    # Imprime Informação completa do Aluno (Sobreopões método main)
    def printInfo(self):
        print("######### INFORMAÇÃO DO ALUNO #########\n")
        print(f"Nome: {self.name}\nIdade: {self.age}\nNIF: {self.nif}\nCurso: {self.course}\nLinguagem de Programação: {self.progLang}\nNível: {self.level}\n")
        print("\n######### #################### #########\n")

    
person1 = Person("Marcos Melo", 49, 222333999)
person1.printInfo()
person1.setAge(38) # Corrigindo a idade da pessoa
print(f"Informação Extra\nNome: {person1.getName()}, Idade: {person1.getAge()}\n\n")

school1 = BestSchool("Alexandre Melo", 15, 244255266, "Python", 1)
school1.printInfo()
school1.setLevel(2) # alterado o nível de conhecimento do aluno para 2
print(f"Informação Extra\nNome: {school1.getName()}, Curso: {school1.getProgLang()} - Nível: {school1.getLevel()}\n\n")


