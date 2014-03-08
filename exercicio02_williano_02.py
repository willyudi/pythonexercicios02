#!/usr/bin/env python
# encoding: utf-8
ano = int(input ('Informe o ano: '))
#Ano bissexto sua dezena é divisível por 4 e não termina em 00
#O ano terminado em 00 será bissexto se for divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print ('O ano ' + str(ano) + ' é bissexto.')
else:
    print ('O ano ' + str(ano) + ' não é bissexto.')