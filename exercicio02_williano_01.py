#!/usr/bin/env python
# encoding: utf-8
x = int(input ('Lado 1 do triângulo: '))
y = int(input ('Lado 2 do triângulo: '))
z = int(input ('Lado 3 do triângulo: '))
if x == y == z:
    #Equlátero (lados iguais)
    print ('Triângulo Equilátero.')
elif x != y and x != z and y != z:
    #Escaleno (lados diferentes)
    print ('Triângulo Escaleno.')
else:
    #Isóceles (pelo menos dois lados iguais)
    print ('Triângulo Isóceles.')


