entrada = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(entrada))
print('Só tem espaços?', entrada.isspace())
print('É um número?', entrada.isnumeric())
print('É tdo maisculo?', entrada.isupper())
print('è minusculo?', entrada.islower())
print('É alfanumerico?', entrada.isalnum())
print('É alfabético', entrada.isalpha())
print('Está capitalizado', entrada.istitle())
