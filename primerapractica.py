#comentario se pone con gato y se ignora#
# Imprimir tu nombre de forma diferente#
#esta es una cadena de caracteres#
nombre= input("Introduce tu nombre: ")
print(f"Hola {nombre}")
print("hola, {}".format(nombre))
# variable de entero
edad= 25
# variable flotante y decimales
altura= 1.71
# convertir a tipo flotante 
edadstring= str(edad)
#string se juntan los valores como juntos
print(edad+edad)
print(edadstring+edadstring)
#type nos sirve para ver que tipo de datos es
print(type(edad))
bolleanos= False
#int ver si la edad es un numero entero
tuEdad=input("Introduce tu edad:")
tuEdad=int(tuEdad)
 # estructura de control es un codigo que permite saber un valor#

if tuEdad >= 18  and tuEdad <100:
    print("Eres mayor de edad")
elif tuEdad >=200:
   print("Eres inmortal")
elif tuEdad <=0:
    print("No existes")
else:
     print("Eres menor de edad")
#for es para ciclos y el rango nos da los numeros que dice el rango menos el ultimo valor dado
for i in range (0,10):
    print(i)
