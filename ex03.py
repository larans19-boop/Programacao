lista_tarefas = []
#status , data , descricão
while (True):
    cod = input("\n-Adicionar tarefa(1)\n-Encerrar tarefa(2)\n-Visualizar lista(3)\n-Sair(4)\n" )
    if cod == "1":
         data =(input('\nData:'))
         desc = (input("Descrição: "))
         status = "Pendente"
         tarefa = {"data": data, "descricao": desc, "status": status }
         lista_tarefas.append(tarefa)
    elif cod == "2":    
        cod_tar = int(input("\nDigite o número da tarefa que deseja encerrar (a partir de tarefa 0): "))
        print(lista_tarefas[cod_tar])
        choice= input("Realmente deseja encerrar essa tarefa?(S/N)")
        if choice.upper == "S":
             lista_tarefas[cod_tar]['status'] = 'Encerrado'
             print(f'Tarefa número {cod_tar} encerrada')
        else:
             continue
    elif cod == "3":
         print("\n",(lista_tarefas) ,"\n")
    elif cod == "4":
         print('Saindo...')
         break
    else:
         print("Número inválido.")
         continue
    print(lista_tarefas) 