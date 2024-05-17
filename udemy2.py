# -*- coding: utf-8 -*-
"""udemy2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10YZUybspMmx6DAsdyJbpNBOpkt8eAXR-
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as srn
import statistics as sts
import seaborn as sns

#criar base de dados  - nome do documento, separação e utf
Data = pd.read_csv("TesteCD.csv",sep=";",encoding='latin-1')
#visualizar
Data.head()

#informações de tamanho do documento
Data.shape

#altera o nome de uma coluna
Data = Data.rename(columns={'Aposenta em': 'Aposentadoria'})
Data.head()

Data = Data.rename(columns={'2022': 'ano1'})
Data = Data.rename(columns={'2023': 'ano2'})
Data = Data.rename(columns={'2024': 'ano3'})

Data = Data.rename(columns={'Anos na empresa': 'TotalAnos'})

Cargos = Data.groupby(['Cargo']).size()
Cargos

Cargos.plot.bar(color='red')

Data['produtividade 2022'].describe()

Data['Salário'].fillna( 1500.00,inplace=True)
Data.head()

#altera o valor de uma célula
Data.iat[2,1]= "R$ 1.500,00";

Data['produtividade 2023'].describe()

media = sts.mean(Data['produtividade 2023'])
print(media)

Data['produtividade 2023'].fillna( 68,inplace=True)

Data.head()

Data.loc[Data['Cargo'] == 'repositor', 'Cargo'] = 'Repositor'
Data.head()

Data.plot.bar()

Data.head()

h = np.histogram(Data.iloc[:,2])
h
plt.hist(Data.iloc[:,2])
plt.Title = ('anos na empresa')
plt.ylabel('qnt de funcionarios')
plt.xlabel('anos')
plt.show()

sns.histplot(Data.iloc[:,2],kde=False, bins = 8, color='red').set(title='anos na empresa')

sns.kdeplot(Data.iloc[:,2], color='red').set(title='anos na empresa')

sns.boxplot(Data.iloc[:,2], color='red').set(title='anos na empresa')

sns.histplot(Data.iloc[:,2],kde=True, bins = 8, color='red').set(title='anos na empresa')

plt.scatter(Data.iloc[:,0],Data.iloc[:,6])
plt.title('produtividade x funcionario')
plt.xlabel('Funcionario')
plt.ylabel('produtividade')
plt.show()



plt.plot(Data.Funcionário, Data.Salário, marker="o")
plt.title('Salário x Funcionário')
plt.xlabel('Funcionário')
plt.ylabel('Salário')

plt.scatter(Data.Funcionário, Data.Salário, marker='o',facecolors='none',color='blue')

x = Data.Salário
y = Data.Funcionário

unicos =list(set(Data.Cargo))
unicos

for i in range(len(unicos)):
  indice = Data.Cargo == unicos[i]
  plt.scatter(x[indice], y[indice], label=unicos[i])
plt.legend(loc = 'upper left')

Data.head(

)

Data.loc[5] = ['Rodrigo','R$ 1.500,00',8,'13/05/2024','01/02/2025','Repositor',81,34,0]

Data.head()

Data.shape

Data

produtividade = [Data.ano1, Data.ano2, Data.ano3]

Data.ano1

produtividade

print(produtividade[0].mean())
print(produtividade[1].mean())
print(produtividade[2].mean())

medAno1= produtividade[0].mean()
medAno2= produtividade[1].mean()
medAno3= produtividade[2].mean()

print(medAno1)
print(medAno2)
print(medAno3)

medtotal = [medAno1,medAno2,medAno3]
print(medtotal)

Anos = ['2022','2023','2024']

plt.plot(Anos,medtotal)

medtotal.append(80)

Anos.append('2025')

print(medtotal)

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(Anos,medtotal)
plt.subplot(2,2,2)
plt.scatter(Data.Salário,Data.Funcionário)
plt.subplot(2,2,3)
plt.hist(Data.TotalAnos)
plt.title('Total de Anos')

agrupado = Data.groupby(['Cargo'])['TotalAnos'].sum()
agrupado

agrupado.plot.bar()

agrupado.plot.pie()

agrupado.plot.barh()

srn.boxplot(agrupado)

agrupado.plot.pie(legend = True, autopct='%1.1f%%', title='Total de anos distribuidos nos cargos')
plt.legend(loc = 'upper right')

