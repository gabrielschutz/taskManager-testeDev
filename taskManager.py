import json
from datetime import date
from faker import Faker

fake = Faker()


# Arquivo
# --------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    with open("tarefas.json", "r") as f:
        data = json.load(f)
        if "tarefas" not in data or not isinstance(data["tarefas"], list):
            raise ValueError()
except FileNotFoundError:
    with open("tarefas.json", "w") as f:
        json.dump({"tarefas": []}, f)
except (json.JSONDecodeError, ValueError):
    with open("tarefas.json", "w") as f:
        json.dump({"tarefas": []}, f)




# --------------------------------------------------------------------------------------------------------------------------------------------------------

search_options = {
    "1": "id",
    "2": "titulo",
    "3": "descricao",
    "4": "status",
    "5": "data_criacao"
}

# --------------------------------------------------------------------------------------------------------------------------------------------------------

def printTarefas(list_tasks, indent=False):
    
    if(indent == False):
        print("-"*126)
        print("| {:<10} | {:<20} | {:<60} | {:<10} | {:<10} |".format("ID","Título", "Descrição", "Status", "Data"))
        print("-"*126)
        
        for task in list_tasks:
            print("| {:<10} | {:<20} | {:<60} | {:<10} | {:<10} |".format(task["id"],task["titulo"], task["descricao"], task["status"], task["data_criacao"]))
            
        print("-"*126)
    
    if(indent == True):
        print("-"*126)
        print("| {:<10}| {:<10} | {:<20} | {:<60} | {:<10} | {:<10} |".format("Indice","ID","Título", "Descrição", "Status", "Data"))
        print("-"*126)
        
        for i, task in enumerate(list_tasks):
            print("| {:<10}| {:<10} | {:<20} | {:<60} | {:<10} | {:<10} |".format(i,task["id"],task["titulo"], task["descricao"], task["status"], task["data_criacao"]))
            
        print("-"*126)


def ListarTarefas():
    with open("tarefas.json", "r") as f:
        
        list_tasks = json.load(f)["tarefas"]
        
        printTarefas(list_tasks)
         
        f.close()

def ListarTarefasFiltro():
    
    with open("tarefas.json", "r") as f:
        
        list_tasks = json.load(f)
        
        while (value := input("Por qual índice deseja filtrar? (1 - Id, 2 - Título, 3 - Descrição, 4 - Status ou 5 - Data de criação): ")) not in search_options:
            print("Opção inválida.")

        filter = search_options.get(value)
        
        if filter in ['id']:
            filtred_tasks = sorted(list_tasks['tarefas'], key=lambda k: int(k[filter]))
        else:
            filtred_tasks = sorted(list_tasks['tarefas'], key=lambda k: k[filter].casefold())
        
           
        printTarefas(filtred_tasks)
        
        f.close()

def BuscarPorTarefas():
    
    while (value := input("Por qual índice deseja buscar? (1 - Id, 2 - Título, 3 - Descrição, 4 - Status ou 5 - Data de criação): ")) not in search_options:
        print("Opção inválida.")
    search_index = search_options.get(value)
    search_value = input(f"Qual o valor do campo {search_index}: ")
    
    with open("tarefas.json", "r") as f:
        
        list_tasks = json.load(f)
  
        tasks_found = [task for task in list_tasks["tarefas"] if search_value.lower() in task[search_index].lower()]
    
        printTarefas(tasks_found)
                
        f.close()


def CriarTarefas():
    

    
    titulo = input("Qual o título da tarefa: ")
    descricao = input("Qual a descrição da tarefa: ")
    status = input("Qual o status da tarefa: ")
    
    with open("tarefas.json", "r") as f:
        createdata = json.load(f)
    with open("tarefas.json", "w") as f:
        createdata["tarefas"].append(
            {
            "id": str(fake.random_number(digits=5)),
            "titulo": titulo,
            "descricao": descricao,
            "status": status,
            "data_criacao": str(date.today())
            }
        )
        json.dump(createdata, f, indent=4)
        print("Tarefa adicionada com sucesso: ")
        f.close()
        
def AtualizarTarefas():
    
    while (value := input("Por qual índice deseja buscar? (1 - Id, 2 - Título, 3 - Descrição, 4 - Status ou 5 - Data de criação): ")) not in search_options:
        print("Opção inválida.")
    search_index = search_options.get(value)
    search_value = input(f"Qual o valor do campo {search_index}: ")
    
    with open("tarefas.json", "r") as f:
        att_data = json.load(f)
        tasks_found = [task for task in att_data["tarefas"] if search_value.lower() in task[search_index].lower()]
        if tasks_found:
            print("Foi encontrada a(s) seguinte(s) tarefa(s): ")
            printTarefas(tasks_found,indent=True)
            while (value := int(input("Qual tarefa deseja atualizar, digite o valor do índice dentre as tarefas listadas!: "))) not in range(0,len(tasks_found)):
                print("Opção inválida.")   
            search_value = value
            for i, task in enumerate(tasks_found):
                if i == search_value:
                    attribute_mapping = {"1": "titulo", "2": "descricao", "3": "status"}
                    while (value := input("Qual índice deseja atualizar? (1 - Título, 2 - Descrição, 3 - Status): ")) not in attribute_mapping:
                        print("Opção inválida.")
                    attribute = attribute_mapping.get(value)
                    new_value = input(f"Novo valor para '{attribute}': ")
                    task[attribute] = new_value    
                    print("Tarefa atualizada com sucesso!")     
            with open("tarefas.json", "w") as f:
                json.dump(att_data, f, indent=4)          
        else:   
            print("Não foi encontrada nenhuma tarefa!")
        f.close()
        
def DeletarTarefas():
    
    while (value := input("Por qual índice deseja buscar? (1 - Id, 2 - Título, 3 - Descrição, 4 - Status ou 5 - Data de criação): ")) not in search_options:
        print("Opção inválida.")
    search_index = search_options.get(value)
    search_value = input(f"Qual o valor do campo {search_index}: ")
    
    with open("tarefas.json", "r") as f:
        dell_data = json.load(f)
        tasks_found = [task for task in dell_data["tarefas"] if search_value.lower() in task[search_index].lower()]
        if tasks_found:
            print("Foi encontrada a(s) seguinte(s) tarefa(s): ")
            printTarefas(tasks_found,indent=True)
            while (value := int(input("Qual tarefa deseja deletar, digite o valor do índice dentre as tarefas listadas!: "))) not in range(0,len(tasks_found)):
                print("Opção inválida.")   
            search_value = value
            for i, task in enumerate(tasks_found):
                if i == search_value:
                    dell_data["tarefas"].remove(task)
                    print("Tarefa deletada com sucesso!")     
            with open("tarefas.json", "w") as f:
                json.dump(dell_data, f, indent=4)          
        else:   
            print("Não foi encontrada nenhuma tarefa!")
        f.close()
        
def PopData():
    
    with open("tarefas.json", "r") as f:
        createdata = json.load(f)
    with open("tarefas.json", "w") as f:
        qtd = int(input("Quantas tarefas deseja gerar: "))
        for _ in range(qtd):
            createdata["tarefas"].append(
                {
                    "id": str(fake.random_number(digits=5)),  
                    "titulo": fake.text(max_nb_chars=10), 
                    "descricao": fake.text(max_nb_chars=20),
                    "status": fake.random_element(elements=("Em andamento", "Finalizada","Urgencia")),
                    "data_criacao": fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d')
                }
            )
        json.dump(createdata, f, indent=4)
        print("Dados populados com sucesso!")
        f.close() 

def LimparArquivo():
    
    while (value := int(input("Deseja realmente deletar todas tarefas? (1 - Sim, 2 - Nao): "))) not in range(1,3):
        print("Opção inválida.")
    confirmation = value
    
    if (confirmation == 1):
        with open("tarefas.json", "w") as f:
            json.dump({"tarefas": []}, f)
    
def main():
    
    while True:
        print("1 - Listar Tarefas!")
        print("2 - Listar Tarefas ordenadas!")
        print("3 - Buscar por Tarefa!")
        print("4 - Criar Tarefa!")
        print("5 - Atualizar Tarefa!")
        print("6 - Deletar Tarefa!")
        print("7 - Popular Arquivo!")
        print("8 - Limpar todas Tarefas!")
        print("9 - Sair!")
        
        option = input("Qual opção deseja: ")
        
        match option:
            
            case "1":
                print("----------- Listar Tarefas -----------")
                ListarTarefas()
            
            case "2":
                print("----------- Listar Tarefas por Índice -----------")
                ListarTarefasFiltro()

            case "3":
                print("----------- Buscar por Tarefas -----------")
                BuscarPorTarefas()
                
            case "4":
                print("----------- Criar Tarefa -----------")
                CriarTarefas()
                
            case "5":
                print("----------- Atualizar Tarefa -----------")
                AtualizarTarefas()
                    
            case "6":
                print("----------- Deletar Tarefa -----------")
                DeletarTarefas()
            
            case "7":
                print("----------- Popular Tarefas -----------")
                PopData()
            
            case "8":
                print("----------- Limpar Tarefas -----------")
                LimparArquivo()
    
            case "9":
                print("----------- Sair -----------")
                break

if __name__ == "__main__":
    main()