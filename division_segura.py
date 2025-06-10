def dividir_seguro(num1,num2):
    try:
        resultado=num1/num2
        print(f"{num1} / {num2} = {resultado}")
    except ZeroDivisionError:
        print("La division por cero no es valida")

num1=int(input("Ingresa el primer numero  "))
num2=int(input("Ingresa el segundo numero  "))
dividir_seguro(num1,num2)