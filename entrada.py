import re
usuario = input('Digite seu usuario\n')
print('Ola',usuario,',curte Black Metal?\n')

senha = input('Digite sua senha\n----------\n')
print('----------\n', '*' * len(senha))
dominio = input('Digite seu dominio, exemplo: @gmail\n')
print('seu dominio é',usuario + '@' + dominio + '.com')

mostrar_senha = input('Gostaria de rever sua senha? responda com sim ou não.\n')
if mostrar_senha == 'sim\n':
    print(senha)
else:
    print('ok\n')

palavra1 = 'banana'

print('colocando em maiuscula', palavra1.upper())

#colocar a string como toda maiuscula print(variavel.upper)
palavra = 'ABACATE'

print('colocando em minuscula: ', palavra.lower())


