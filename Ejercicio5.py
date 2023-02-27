'''

Ejercicio 5:

Crea un código que tome como parámetro una frase y sea capaz de contar el número de palabras que contiene.
 Haga un test con la frase: "Me gusta estudiar python en la UNSAM".

Y si queremos contar los caracteres incluyendo los espacios. ¿Cómo seria?

Prueba con otras frases, para eso podes usar la funcion de ingreso de valores por teclado.

'''

parametro = "Me gusta estudiar python en la UNSAM"
parametro2 = str(input("Ingresa una frase : "))

print("Cantidad de letras en parametro: ", len(parametro))
print("Cantidad de palabras de la frase: ", len(parametro2))
