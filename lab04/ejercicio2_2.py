from operator import truediv


maximo = 0
minimo = 0
primer_numero = True
while True:
    try:
        input_str = input("Ingresar un numero: ")
        if(input_str = "done")
            break
        else:
            if(int(input_str) > maximo): maximo = int(input_str)
            if(input(input_str) < minimo): minimo = int(input_str)
    except:
        print("Valor no valido")
        continue
print("Maximo: ", maximo)
print("Minimo:", minimo)