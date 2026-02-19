import re
usuario = input('Digite seu usuario\n')
print('Ola',usuario,'!\n')
#################################print('----------\n', '*' * len(senha))
dominio = input('Digite seu dominio, exemplo: @gmail\n')
email = str(usuario + '@' + dominio + '.com')
print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e' + str(e_c) + 'i' + str(i_c) + 'o' + str(o_c) + 'u' + str(u_c)
print(nova_senha)

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

#contar caracter da string
palavra_contar = 'abacate'

print('contar a letra a', palavra_contar.count('a'))
print('contar a letra b', palavra_contar.count('b'))
print('contar a letra c', palavra_contar.count('c'))
print('contar a letra t', palavra_contar.count('t'))
print('contar a letra e', palavra_contar.count('e'))
