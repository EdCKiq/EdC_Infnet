def renda(r_i,g_m,g_e,g_t):
    right_percent_m = r_i * 0.30
    right_percent_e = r_i * 0.15
    right_percent_t = r_i * 0.06
    percent_m = (g_m*100) / r_i
    percent_e = (g_e*100) / r_i
    percent_t = (g_t*100) / r_i
    return percent_m,percent_e,percent_t,right_percent_m,right_percent_e,right_percent_t

def show(p_m,p_e,p_t,r_p_m,r_p_e,r_p_t): # Abreviação das váriaveis retornadas da função 
    print('\nDiagnóstico:\n')
    if p_m > m:
        print(f'Seus gastos totais com moradia comprometem {p_m:.2f}% de sua renda total. O máximo recomendado é de {m}%.\nPortanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {r_p_m:.2f}\n')
    elif p_m < m :
        print(f'Seus gastos totais com moradia comprometem {p_m:.2f}% de sua renda total.\nSeus gastos estão dentro da margem recomendada.\n')
    if p_e > e:
        print(f'Seus gastos totais com educação comprometem {p_e:.2f}% de sua renda total.\nO máximo recomendado é de {e}%. \nPortanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {r_p_e:.2f}\n')
    elif p_e < e :
        print(f'Seus gastos totais com educação comprometem {p_e:.2f}% de sua renda total.\nSeus gastos estão dentro da margem recomendada.\n')
    if p_t > t:
        print(f'Seus gastos totais com transporte comprometem {p_t:.2f}% de sua renda total.\nO máximo recomendado é de {t}%. \nPortanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {r_p_t:.2f}\n')
    elif p_t < t:
        print(f'Seus gastos totais com transporte comprometem {p_t:.2f}% de sua renda total.\nSeus gastos estão dentro da margem recomendada.\n')


renda_inicial = float(input("Renda mensal: "))
g_moradia = float(input("Gastos com moradia: "))
g_educacao = float(input("Gastos com educação: "))
g_transporte = float(input("Gastos com transporte: "))

m=30 # Váriveis 
e=20 # de 
t=15 # Apoio

p_m,p_e,p_t,r_p_m,r_p_e,r_p_t = renda(renda_inicial,g_moradia,g_educacao,g_transporte)
show(p_m,p_e,p_t,r_p_m,r_p_e,r_p_t)