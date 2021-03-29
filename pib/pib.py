import pandas as pd
pibs = pd.read_csv('/home/kiqec/Estudos/LCA/pib/pibs.csv')
    
pibs_list = pibs.values.tolist()

def search(pibs_list,nome_solicitado,ano_solicitado):

    for i in range(len(pibs_list)):
        if nome_solicitado == pibs_list[i][0]:
            num_p = i
            p = True
            break;
        else:
            num_p = 404
            p = False
    for i in range(len(pibs.columns)):
        if pibs.columns[i] == ano_solicitado:
            num_a = i
            a = True
            break;
        else:
            num_a = 404
            a = False
        
    if p == False:
        print("\nPaís não disponível.")
    elif a == False:
        print("\nAno não disponível.")
    elif p == False and a == False:
        print("\nPaís nem ano disponiveis.")
    
    return a,p,num_p,num_a

nome_solicitado = input("Digite o país que deseja procurar: ")
ano_solicitado = input("Digite o ano que deseja procurar: ")

a,p,num_p,num_a = search(pibs_list, nome_solicitado, ano_solicitado)

def show(a,p,num_p,num_a):
    if a == True and p == True:
        pib = pibs_list[num_p][num_a]
        print(f'\nPIB {nome_solicitado} em {ano_solicitado} era de {pib}' )

show(a,p,num_p,num_a)