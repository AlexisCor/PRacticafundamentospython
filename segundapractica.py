#imprimir un valor aleatorio de los valores dados#
import random
#Libreria para obtener graficas
#debemos instalar los siguientes comandos 
#python -m pip install -U pip
#python -m pip install -U matplotlib
#despues ponemos pip install y podemos ejecutar nuestro proyecto con la grafica
import matplotlib.pyplot as plt 
# nos genera una tablar#
print(random.randrange(10, 100, 2))

print(random.randint(0,10))
#Pone la lista normal
lista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("lista original",lista)
#Imprime una lista mezclada
random.shuffle(lista)
print("Lista mixeada", lista)
#Genera una grafica de campana de gauus
#GEnera los datos de la grafica
campana =[random.gauss(1,0.5) for i in range (1000)]
#Arma la grafica
plt.hist(campana, bins=15)
#Muestra la graifca 
plt.show()