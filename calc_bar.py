def calc_total(valor_total,num_pessoas,servico):
    valor_total = valor_total + (valor_total * (servico / 100))
    valor_dividido = valor_total / num_pessoas
    return valor_total, valor_dividido

def show(v_t,v_d, num_pessoas):
    v_d = str(v_d).replace(".",",")
    v_t = str(v_t).replace(".",",")
    print(f'O valor total é de R${v_t}')
    print(f'O valor da conta divida por {num_pessoas} é de R${v_d}')

try:
    valor_total = float(input("Qual o valor conta? R$:"))
    num_pessoas = int(input("N° de  pessoas: "))
    servico = float(input("Percentual do serviço entre 0 e 100: "))
    erro = False
except ValueError:
    erro = True
    print("Valor não permitido")

if erro == False and (servico >= 0 and servico <=100) and num_pessoas > 0 and  valor_total >= 1:
    v_t,v_d = calc_total(valor_total,num_pessoas,servico)
    show(v_t,v_d,num_pessoas)
else:
    print("Valores não aceitos foram digitados, por favor concerte")