# -*- coding: utf-8 -*-
"""Estrutura Condicional
"""

# if
if 5 < 10:        # se 5 é menor que 10, mostre que é verdade
  print('verdade')

# if/else

x = 10
y = 5

if x > y:
    print(' O valor x é maior que y')

else:
    print('O valor y é maior que x')

# if / Elif / Else

x = 10
y = 10

if x > y:
  print('O valor de x é maior que y')

elif x < y:
  print('O valor de y é maior que x')

else:
  print('Os dois valores são iguais')

"""# Condicional com operadores lógicos"""

# Testar vários valores

x = 10
y = 5
z = 2

if (x > y) and (x > z):      #Se x é maior que y, e maior que z, logo o maior número é X
  print(' O x é o maior número')

else:
  print('O x não é o maior número')
