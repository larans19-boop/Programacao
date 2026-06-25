despesas = []
while(True):
    cod = input("\nAdiciionar despesa(1) \nVer lista(2) \nEncerrar despesa(3) \nSair(4)")
    if cod == '1':
        data = input("\nData: ")
        valor = input("\nValor: ")  
        cat = input("\nCategoria: ")
        desc = input("\nDescrição: ")
        esp = {'data': data , 'valor':valor , 'categoria': cat , 'descricao': desc}
        despesas.append(esp) 
    elif cod == '2':
        cod_cat = input("Qual categoria: ")  
        print(f"listando categoria{cod_cat}")
        for i in despesas:
            if i['categoria'] == cod_cat:
                print(f"Data: {i['data']} valor: {i['valor']} categoria: {i['categoria']} descreção: {i['descricao']}")  
    elif cod == '3':
        cod_encerra = int(input("Qual tarefa, por ordem de incerção, deseja encerrar?(ordem á partir de 0): "))
        despesas.pop(cod_encerra)
    elif cod == "4":
        print("Saindo...")
        break
    else:
        print("Número inválido")
        continue 