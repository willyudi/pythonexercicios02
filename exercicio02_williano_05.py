#!/usr/bin/env python
# encoding: utf-8
primeiro = int(input ('Informe o primeiro número: '))
segundo = int(input ('Informe o segundo número: '))
terceiro = int(input ('Informe o terceiro número: '))
if primeiro < segundo < terceiro:
    #terceiro e primeiro
    print ('O maior é o terceiro = ' + str(terceiro))
    print ('O menor é o primeiro = ' + str(primeiro))
elif primeiro > segundo > terceiro:
    #primeiro e terceiro
    print ('O maior é o primeiro = ' + str(primeiro))
    print ('O menor é o terceiro = ' + str(terceiro))
elif primeiro == segundo == terceiro:
    #iguais
    print ('Todos são iguais a ' + str(primeiro))    
else:
    #segundo e (primeiro ou terceiro)
    print ('O maior é o segundo = ' + str(segundo))
    if primeiro < terceiro:
        print ('O menor é o primeiro = ' + str(primeiro))
    else:
        print ('O menor é o terceiro = ' + str(terceiro))
        