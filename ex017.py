horasTrabalhadas = int(input('Digite a quantidade de horas trabalhadas:'))
print('Salário total = R$ {}.' .format(horasTrabalhadas*10))

if horasTrabalhadas > 50:
    bonus = (horasTrabalhadas-50)*20
    print('Salário com bônus = R$ {}.' .format(bonus+(50*10)))
else:
    bonus = 0

