def res(idade):
    if idade <=0:
        print("Erro!")
        print("Idade Invalida!")
    elif idade < 16 and idade>=1:
        print("Não tem direito a voto")
    elif (idade > 16 and idade < 18) or (idade > 70 ):
        print("Voto facultativo") 
    elif idade >=18 and idade <=70:
        print("Voto obrigatorio")
    else:
        print("Sinto muito mas você não é humano")

idade = int(input("Digite sua idade: "))
res(idade)
