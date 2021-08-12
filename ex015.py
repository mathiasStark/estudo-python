salario = float(input('Digite seu sálario:'))
prestacao = float(input('Digite o valor da prestação:'))

if prestacao > (salario*0.2):
    print('Empréstimo não pode ser concedido')
else:
    print('Empréstimo pode ser concedido')
