# G_TK

Punto 1: 
En esta función, primero creamos una lista series con los números repetidos de X hasta el n-ésimo término.
Luego, calculamos la suma de estos números convertidos a enteros utilizando la función sum.
Después, generamos la expresión de la serie utilizando el método join para concatenar los números con el signo de suma " + ".
Finalmente, retornamos la cadena que contiene la expresión de la serie junto con el resultado de la suma.

Punto 2:
La función numeros_divisibles recorre la lista de entrada y agrega los números que satisfacen las condiciones a la lista de salida: El número debe ser divisible por 5,
si el número es mayor a 600 no se incluye en la salida, si un número es mayor que 1000, se detiene el procesamiento,  y se devuelve la lista resultante hasta ese punto.

Punto 3: 
La función grupo_similar utiliza un diccionario grouped_dict para agrupar los elementos similares de la lista "lista". 
Si un número ya existe en el diccionario, se agrega a la lista correspondiente, de lo contrario, se crea una nueva entrada en el diccionario.

Punto 4:

El programa de consola en Python cumple con los requerimientos para gestionar el inventario de un negocio.
Utiliza listas y diccionarios para organizar los productos en los grupos 'dairy', 'cleaning', y 'grain', y mantener sus respectivas existencias.
Permite registrar productos nuevos o actualizar existencias para productos existentes. 
