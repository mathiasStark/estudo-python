horasTrabalhadas = int(input('Quantas horas trabalhadas:'))
salarioBruto = horasTrabalhadas*10
impostoRenda = salarioBruto*0.1
inss = salarioBruto*0.08
salarioLiquido = salarioBruto-impostoRenda-inss
print('O salario bruto é R$ {0}, com os devidos descontos o trabalhador receberá R$ {1}.' .format(salarioBruto, salarioLiquido))
