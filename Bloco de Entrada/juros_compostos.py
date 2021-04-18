import matplotlib.pyplot as plt
def composto(aporte_inicial,aporte_mes,taxa_juros,meses):
    list_rendimentos = []
    juros = aporte_inicial + aporte_inicial * (taxa_juros/100)
    for i in range(meses):
        juros += aporte_mes
        aporte_att = juros
        juros = aporte_att + aporte_att * (taxa_juros/100)
        print(f'Valor no mês {i+1} após o aporte inicial: R${aporte_att:.2f}')
        list_rendimentos.append(aporte_att)
    return list_rendimentos

def grafico(list_rendimentos):
    plt.plot(list_rendimentos)
    plt.ylabel('Valor')
    plt.xlabel('Meses')
    plt.show()

aporte_inicial = float(input('Digite o valor do aporte inicial: '))
aporte_mes = float(input('Digite o valor do aporte mensal: '))
taxa_juros = float(input('Digite a taxa de juros: '))
meses = int(input('Meses que será guardado: '))

grafico(composto(aporte_inicial,aporte_mes,taxa_juros,meses))

