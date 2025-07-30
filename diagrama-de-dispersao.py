## Você está prestando serviços a uma empresa química, eles estão analisando dois métodos para realizar a verificação de concentração de hidrogênio no intuito de conhecer se os resultados fornecem valores adequados.

# Observe as informações que eles forneceram e responda aos questionamentos iniciais que ajudaram a dar inicio à tomada de decisão. Os dados fornecidos são: x = concentração de hidrogênio (ppm) usando um método de cromatografia gasosa, e y = concentração usando um novo método

# Fonte: “A new method to measure the diffusible hydrogen content in steel weldments using a polymer electrolyte-based hydrogen sensor” (Welding Res., jul. 1997: 251s-256s).

# E forneceram os seguintes resultados: dados-diagrama-dispersao.png



## Analisando as características do meus dados

    #I. Observe os dados sobre concentração de hidrogênio, e responda: x e y são dados:

        #Categóricos.
        #Univariados.
        #Bivariados.

        # R.: São dados bivariados porque representam duas observações feitas e ambas variávies devem ser analisadas


    #II. Observe a característica da informação dos dados x e y, considernado as características da informação que eles apresentam podem ser caracterizados como dados:

        #Numéricos.
        #Categóricos.
        #Binários.

        # R.: Numéricos


## Analisando os dados propriamente

    # Bem, após saber o tipo de dados com que você está tratando, realize um diagrama de dispersão.

    # Para realizar o diagrama de dispersão incialmente deve definir os dados a serem analisados, isto é: x e y

x = [47, 62, 65, 70, 70, 78, 95, 100, 114, 118, 124, 127, 140, 140, 140, 150, 152, 164, 198, 221]
y = [38, 62, 53, 67, 84, 79, 93, 106, 117, 116, 127, 114, 134, 139, 142, 170, 149, 154, 200, 215]

#Uma vez tendo os dados prontos declarados é só realizar o gráfico, existem diversas possibilidades, deixo a seguir uma delas:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(x, y)
#plt.xlim(0,2)   #axis x métod de cromatografia gasosa
#plt.ylim(0,5)   #axis y métod novo
plt.xlabel('método de cromatografia gasosa')
plt.ylabel('método novo')
plt.title('Gráfico de dispersão')
plt.show()

## Observando a caraterística do gráfico indique qué tipo de correlação tem os dados x e y.

    #Zero.
    #Positiva.
    #Negativa.

    # R.: Positiva





