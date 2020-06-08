from random import randint
computador = randint(0,2)

lista =['Pedra', 'Papel', 'Tesoura']
print('''
[0] = Pedra
[1] = Papel
[2] = Tesoura
''')
jogador = int(input('Faça a sua escolha:  '))
print('Voce escolheu {} '.format(lista[jogador]))
print('Seu inimigo escolheu {}'.format(lista[computador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Voce ganhou')
    elif jogador == 2:
        print('Voce perdeu')

elif computador == 1:
    if jogador == 0:
        print('Voce perdeu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Voce ganhou')

elif computador == 2:
    if jogador == 0:
        print('Voce ganhou')
    elif jogador == 1:
        print('Voce perdeu')
    elif jogador == 2:
        print('EMPATE')