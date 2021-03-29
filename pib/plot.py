import pandas as pd
import matplotlib.pyplot as plt

pibs = pd.read_csv('/home/kiqec/Estudos/LCA/pib/pibs.csv')
pibs_list = pibs.values.tolist()
pibs_num = pibs.drop(columns = ['País'])
pibs_num_list = pibs_num.values.tolist()

pais = input('Digite o nome do país desejado: ')

def search(p_l,pais):
    for i in range(len(p_l)):
        if pais == p_l[i][0]:
            p = True
            break;
        else:
            p = False
          
    return i,p

p_d,p = search(pibs_list,pais)
if p == True:

  plt.plot(pibs.columns[1:9],pibs_num_list[p_d])
  plt.title(pibs_list[p_d][0])
  
  plt.show()
else:
  print("Pais não disponivel")