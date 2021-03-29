import pandas as pd

pibs = pd.read_csv('/home/kiqec/Estudos/LCA/pib/pibs.csv')

pibs_list = pibs.values.tolist()
pibs_num = pibs.drop(columns = ['País'])
pibs_num_list = pibs_num.values.tolist()

nome_paises = []
for i in range(len(pibs_list)):
    nome_paises.append(pibs_list[i][0])

def expressao(p_n_l,num):
    vl = len(pibs_num_list[num]) - 1
    vi = pibs_num_list[num][0]
    vf = pibs_num_list[num][vl]
    valor_percentual = (vf/vi - 1) * 100
    return valor_percentual

for i in range(len(pibs_num_list)):
    v_p = expressao(pibs_num_list,i)
    print(f'{nome_paises[i]} \t\t\tVariação de {v_p:.2f}% entre 2013 e 2020.')