# Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
# Si trabaja 40 horas o menos se le paga $2600 por hora
# Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40 horas y $5000 por cada hora extra
horas = int(input('\nIngrese su horas laborales: '))
if horas <= 40:
    salario = horas * 2600
    print('\nSu salario es de: ', salario)
elif horas > 40:
    horasextra = horas - 40
    salario = (horasextra * 5000) + 104000
    print('\nSu salario es de: ', salario)
