from operator import itemgetter
def questions(cont):
    nome = input(f'Digite o nome do {cont}° candidato: ')
    nota = float(input(f'Digite a nota do {cont}° candidato: '))
    return nota,nome

def show(sorted_list):
    print(f'O ganhador foi {sorted_list[0][0]} com a nota {sorted_list[0][1]}')
   
cont = 1
while cont < 6:
    nota,nome = questions(cont)
    if nota > 0 and nota < 10:
        list_nn = []
        list_nn.append([nome,nota])
        cont+=1
        if cont == 6:
            sorted_list = sorted(list_nn, key=itemgetter(1), reverse=True)
            show(sorted_list)
    else:
        print("Nota não aceita")