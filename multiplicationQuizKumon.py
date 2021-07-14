#! python3
#-------------------------------------------------------------------------------------------------------------------
# Programa modelado a partir do exemplo mostrado no livro Automate Boring Stuff de Al Sweigart.
#-------------------------------------------------------------------------------------------------------------------
#   Exercício de Multiplicação
#       Este programa permite ao usuário selecionar o número de questões e quais valores máximos serão multiplicados.
#       O mecanismo de correção é inspirado no método Kumon de ensino, em que o usuário deve acertar o maior número
#           de questões, no menor tempo possível.
#       Por não haver um monitor humano os auxiliando e corrigindo essas questões, o programa não oferece a solução e
#           nem permite que o usuário proceda sem acertar.

#   REFERÊNCIA BIBLIOGRÁFICA:
#       ______. Automate the Boring Stuff, c2019. Chapter 8, INPUT VALIDATION.
#       Disponível em: https://automatetheboringstuff.com/2e/chapter8/. Acesso em: 12 de jul. de 2021.
#-------------------------------------------------------------------------------------------------------------------

import random, time, pyinputplus as pyip
from time import gmtime, strftime, localtime


questoesCorretas = 0

print('\n****  Teste de multiplicação  ***\n')
print(strftime('\nVocê está começando o exercício em %d/%m/%Y, à(s) %H:%M.\n', localtime()))

numeroDeQuestoes = pyip.inputInt('\nInforme quantas questões quer fazer: ')

limite1 = pyip.inputInt('\nInforme o maior número possível para o 1º NÚMERO da multiplicação "num1 x num2": ' )
limite2 = pyip.inputInt('\nInforme o maior número possível para o 2º NÚMERO da multiplicação "num1 x num2": ' )

for numQuestao in range(numeroDeQuestoes):
        # Pick two random numbers:
    num1 = random.randint(1, limite1)
    num2 = random.randint(1, limite2)

    prompt = '#%s: %s x %s = ' % (numQuestao + 1, num1, num2)

    while True:

        try:

            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], 
                              blockRegexes=[('.*', 'Incorreto!')],
                              limit=3)
        except pyip.RetryLimitException:
            sim = pyip.inputYesNo('Você errou muitas vezes. Gostaria de continuar tentando?')
            if sim =='yes':
                continue
            else:
                break

        else:
            print('Correto!')
            questoesCorretas += 1
            break
            time.sleep(1) # Brief pause to let user see the result.
    
print('\nScore: %s / %s' % (questoesCorretas, numeroDeQuestoes))

print('\nSeu tempo de resolução foi: '+str(int(time.perf_counter())) + ' segundos')

print(strftime('\nVocê finalizou o exercício em %d/%m/%Y, à(s) %H:%M.\n', localtime()))
