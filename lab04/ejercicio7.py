def calificaciones(grade):
    if (grade >= 0.9 and grade <=1.0):
        score = "sobresaliente"
    elif (grade >= 0.8 and grade < 0.9):
        score = "notable"
    elif (grade > 0.7 and grade < 0.8):
        score = "buena"
    elif (grade >= 0.7 and grade < 0.6):
        score = "suficiente"
    elif (grade <= 0.6):
        score = "Insuficiente"
    else:
        score = "Grade no valida"
    return score

try:
    grade = float(input("ingrese la calificacion entre 0.1 y 1.0: "))
    score = calificaciones
    print("Su score es: ", score)
except:
    print("Error, se debe ingresar un valor numerico")