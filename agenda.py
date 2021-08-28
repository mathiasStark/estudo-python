print('*-----------------------*')
print('* - Agenda Telefônica - *')
print('*-----------------------*')

# Menu da agenda
escolha = None
# Função que define as opções do menu.
def menu():
    global escolha
    escolha = int(input('1 - Inserir novo contato\n2 - Consultar contato\n3 - Editar contato\n4 - Remover contato\n0 - Sair\nEscolha uma opção:'))

# Chamada da função menu
menu()

# Criando  o dicionário
contato = {}

# Criando variável de loop do dicionário
inicio = None
while inicio != 0:

    if escolha == 1:

        # inserir novo contato
        nome = input('Digite o nome:\t')
        numero = input('Digite o número do contato:\t')
        email = input('Digite o email:\t')
        twitter = input('Digite a conta do Twitter:\t')
        insta = input('Digite a conta do Instagram:\t')
        contato[nome] = numero, email, twitter, insta

        # chamada do menu inicial
        menu()


    elif escolha == 2:

        # buscar contato na agenda
        buscar = input('Digite o nome do contato que deseja buscar:')
        print(contato.get(buscar, 'Contato não localizado'))

        # chamada do menu inicial
        menu()

    elif escolha == 3:
        # Editar contato
        novosValores = input('Nome do contato a ser editado:\n')
        if novosValores in contato:
            novoNome = input('Digite o novo nome:\n')
            novoNumero = input('Digite o novo número:\n')
            novoEmail = input('Digite o novo email:\n')
            novoTwitter = input('Digite o novo Twitter:\n')
            novoInsta = input('Digite o novo Insta:\n')

            contato[nome] = novoNome, novoNumero, novoEmail, novoTwitter, novoInsta
            #contato[email] = novoEmail
            #contato[numero] = novoNumero
            #contato[twitter] = novoTwitter
            #contato[insta] = novoInsta
        else:
            print('Contato inexistente')

        # chamada do menu inicial
        menu()

    elif escolha == 4:

        # excluir contato
        apagar = input('Digite o nome do contato a ser excluído:')
        print(contato.pop(apagar, 'Contato não localizado'))

        # chamada do menu inicial
        menu()

    elif escolha == 0:
        print('Agenda Fechada.')
        break
    else:
        print('Comando inválido\n')

        # chamada do menu inicial
        menu()
else:
    ('Agenda Fechada.')