#!/usr/bin/env python
# encoding: utf-8
regulamento = 50
excedente = 4.00
excesso = 0
multa = 0
peso = int(input ('Informe o peso dos peixes em kilos: '))
if peso > regulamento:
    excesso = peso - regulamento
    multa = excesso * excedente
    print ('O peso de excesso foi ' + str(excesso) + ' kilos.')
    print ('O valor da multa é R$ %.2f' % multa)
else:
    print ('Não houve excesso.')
    print ('excesso = ' + str(excesso))
    print ('multa = ' + str(multa))