#Interface de usuário
print('Conversão de Criptomoedas\n')
print('*-----------------------------*\n')
print('1 - Converter Bitcoins em Reais:\n2 - Converter Reais para Bitcoins:\n3 - Sair.\n\n' )

#entrada com opção do usuário
entrada = int(input('Escolha uma opção:\n'))
real = 1

#condição sair
if entrada == 0:
    print('Fim do programa')

#Opcao 1
if entrada == 1:
    
    print('*-----------------------------*\n')
    print('Convertendo Bitcoin para Real:\n')
    print('*-----------------------------*\n')
    
    valorBit = float(input('Quanto vale 1 real em Bitcoin?'))
    bitcoin = float(input('Quanto em Bitcoin quer converter?'))
    
    #conversao bit para real
    if valorBit >= 0.0000000000001:
        real = bitcoin/valorBit
        print('{} Bitcoins vale R$ {}' .format(bitcoin, real))
        
#opcao 2        
if entrada == 2:
    
    print('*-----------------------------*\n')
    print('Convertendo Real para Bitcoin:\n')
    print('*-----------------------------*\n')
 
    reais = float(input('Quantos Reais quer converter?'))
    valorBit = float(input('Quanto vale 1 real em Bitcoin?'))
    
    #conversao real para Bitcoin
    if reais > 0.0000000001:
        
        real = reais*valorBit
        print('R$ {}, vale {} Bitcoins.' .format(reais, real))
        
print('Fim da Conversão')
        