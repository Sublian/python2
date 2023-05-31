import random
import matplotlib.pyplot as plt
import seaborn as sns

campana=[random.gauss(1,0.5) for __ in range(1000)]

#utilizando la libreria matplotlib
plt.hist(campana, bins=30)
plt.title('1era Campana de Gauss')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.ylim(0, 100)
plt.show() 
