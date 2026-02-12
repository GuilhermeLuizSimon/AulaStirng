import re
usuario = input('Digite seu usuario\n')
print('Ola',usuario,',curte Black Metal?\n')

senha = input('Digite sua senha\n----------\n')
print('----------\n', '*' * len(senha))
dominio = input('Digite seu dominio, exemplo: @gmail\n')
print('seu dominio é',usuario + dominio + '.com')

mostrar_senha = input('Gostaria de rever sua senha? responda com sim ou não.\n')
if mostrar_senha == 'sim':
    print(senha)
else:
    print('ok')



