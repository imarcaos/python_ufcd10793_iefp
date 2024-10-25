'''
Projeto Final - 2024-09-11
@author: Marcos Melo
'''
import pandas as pd

# Indicar caminho e nome do ficheiro CSV
PATH = 'Projeto_Final/'
FILENAME = 'todo_list.csv'


# Classe Todo List - Lista de Tarefas
class Todolist:
    # Construtor
    # __init__ usar para iniciar e definir como construtor
    def __init__(self, id, description, date) -> None:
        self.id = id  # instanciando os atributos as variáveis
        self.description = description
        self.date = date

    # Retorna o id
    def getId(self):
        return self.id

    # Retorna a descrição
    def getDescription(self):
        return self.description

    # Retorna a Data
    def getDate(self):
        return self.date

    # Retorna a Tarefa
    def getTodolist(self):
        return self.id, self.description, self.date

    # Atribui uma nova descrição
    def setDescription(self, description):
        self.description = description

    # Atribui uma nova data
    def setDate(self, date):
        self.date = date

    # Imprime todas as informações da Tarefa
    def printTarefas(self):
        print("********* TAREFAS *********\n")
        print(f"Id: {self.id}\nDescrição: {
              self.description}\nData: {self.date}")
        print("\n********* XXXXXXX *********\n")


class DataFrame:
    # construtor recebe o nome do arquivo
    def __init__(self, name_file=None, df=None):
        if name_file is not None:
            self.df = pd.read_csv(name_file)
        elif df is not None:  # verifica se foi realmente criado o DataFrame
            self.df = df

    # Veirficar se o ID existe
    def checkID(self, id):
        return id in self.df['ID'].values

    # Faz a verificação e retorna o próximo ID disponível
    def checkNextID(self):        
        x = 1
        for x in range(self.df.size+1):
            x += 1
            if (not (x in self.df['ID'].values)):
                return x
                break

    # Apresenta todas as Tarefas
    def printAllTodolist(self):
        print(self.df.set_index('ID'))

    # Adiciona uma nova Tarefa
    def add(self, id):
        # Linhas de Adição da Tarefa com índice automático
        description = input("Digite a Descrição da Tarefa: ")
        date = input("Digita a data Limite (dd/mm/aaaa): ")

        # adiciono a tarefa ao final do DataFrame 
        self.df.loc[len(self.df.index)] = [id, description, date]

        # Gravo as alterações feitas ao ficheiro CSV
        self.df.to_csv(PATH + 'todo_list.csv', index=False)

        # Adiciono a Tarefa a Classe TodoList para uso temporário 
        tdl = Todolist(id, description, date)
        tdl.printTarefas() # Imprime a última tarefa adicionada

    # Remove uma nova Tarefa
    def removeId(self, id):
        # Pergunta se tem certeza da remoção
        checkRemove = input("Tem certeza que deseja remover esta tarera (yes/no): ")
        if(checkRemove == 'yes'):
            self.df.drop(self.df[self.df["ID"] == id].index, inplace=True)
            print("Tarefa removida com sucesso!\n")
            self.printAllTodolist()

            # Gravo as alterações feitas ao ficheiro CSV
            self.df.to_csv(PATH + 'todo_list.csv', index=False)
        else:
            print("Ok, certifique-se de concluir a tarefa!!!")

def main():
    df = DataFrame(name_file=PATH+FILENAME)
    while True:
        print(""" MENU
            1- Adicionar Tarefas
            2- Listar Tarefas
            3- Apagar Tarefa
            9- Sair
            """)
        resposta = int(input("Escolha uma das Opções: "))  # Casting string to int
        if resposta == 1:
            print('\nAdicionar tarefa e a data para execução!!!')

            # Chama o método Adicionar tarefa e pesquisa um índice válido
            df.add(df.checkNextID())

        if resposta == 2:
            print("\n**** Lista de Tarefas ****")
            df.printAllTodolist()
            print("\n**************************\n")

        if resposta == 3:
            print('\nRemover Tarefa Concluída!!!')

            # Listar as Tarefas, pedir o Id da tarefa e chamar o método Remover
            df.printAllTodolist() # lista tarefas
            id = int(input("\nDigite o número do ID a remover: "))
            df.removeId(id) # chama o método remover

        if resposta == 9:
            print("Obrigado, Não te esqueças das Tarefas!")
            break


# Executa a função Main para iniciar o programa
# menu com opções
main()


### ÁREA DE TESTES ###
### Deixo a área de testes, para finalidades de estudos
### em uma situação de cliente, removeria toda esta parte e comentários sem importância

# ## df (data frame)
# df = pd.read_csv(PATH+FILENAME)
# #print(df.head()) # testar se carregou o ficheiro

# # print(df.to_string()) # escreve o conteúdo
# print(df.index) # escreve informações sobre o index
# print(df.set_index('ID')) # escreve informações sobre o index que específicamos 'ID'
# sorted = df.sort_values('ID')
# # sorted.to_csv(PATH+'new_todo_list.csv', index=False) # escrevemos um ficheiro CSV sem o index criado por ele

# # Verifica se o ID = 2 está contido no campo 'ID' do DataFrame
# print(2 in df['ID'].values)

# # tarefa1 = Tarefa(1, "Iniciar Projeto Final de Python", "11/09/2024")
# # tarefa1.printTarefas()

### FIM ÁREA DE TESTES ###
