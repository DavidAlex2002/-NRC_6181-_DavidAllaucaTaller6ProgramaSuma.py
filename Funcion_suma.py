#función suma 
def sumar (num1,num2,num3):
    #creación de la variable suma con operación para los tres números ingresados
    suma = num1 + num2 + num3
    #imprime el resultado de la operación de los tres números
    print ("La suma es: ", str(suma))
    return suma
#Ingresar el primer valor
num1 =int(input("Ingrese el primer número: "))
#Ingresar el segundo valor
num2 =int(input("Ingrese el segundo número: "))
#Ingresar el tercer valor
num3 =int(input("Ingrese el tercer número: "))
#Llamado a la función sumar
resultado = sumar(num1, num2, num3)

