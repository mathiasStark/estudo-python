salarioMinimo = float(input('Digite o valor do salario mínimo:'))
kw = float(input('Digite quantos kw foram gastos na residência:'))

#100 kilowatts custa 1/7 do salário mínimo
valorKw = (kw*(salarioMinimo/7))/100

#valor cada kw gasto
custoCadaKw = valorKw/kw

#valor com desconto de 10%
desconto = valorKw*0.9

print('O valor de cada kw gasto custa R$ {}.' .format(custoCadaKw))
print('O valor total da conta de energia é R$ {}.' .format(valorKw))
print('Se optar com pontualidade teré 10% de desconto, resultando em R$ {}.' .format(desconto))
           
