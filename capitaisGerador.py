#!  python 3
# Cria quizzes com perguntas e respostas a chave de resposta correta.

#-----------------------------------------------------------------------------------------------------------------------
# Programa adaptado para os estados brasileiros, a partir do capítulo 8, do livro Automate the Boring Stuff.

#   REFERÊNCIA BIBLIOGRÁFICA:
#       SWEIGART, Al. Automate the Boring Stuff, c2019. Chapter 8, Reading and Writing Files.
#       Disponível em: https://automatetheboringstuff.com/chapter8/. Acesso em: 12 de jul. de 2021.
#-----------------------------------------------------------------------------------------------------------------------

import random

#   Os dados do quiz. Chaves são estados e valores são capitais
capitais = {'Acre':                 'Rio Branco',
            'Alagoas':              'Maceió',
            'Amapá':                'Macapá',
            'Amazonas':             'Manaus',
            'Bahia':                'Salvador',
            'Ceará':                'Fortaleza',
            'Distrito Federal':     'Brasília',
            'Espírito Santo':       'Vitória',
            'Goiás':                'Goiânia',
            'Maranhão':             'São Luís',
            'Mato Grosso':          'Cuiabá',
            'Mato Grosso do Sul':   'Campo Grande',
            'Minas Gerais':         'Belo Horizonte',
            'Pará':                 'Belém',
            'Paraíba':              'João Pessoa',
            'Paraná':               'Curitiba',
            'Pernambuco':           'Recife',
            'Piauí':                'Teresina',
            'Rio de Janeiro':       'Rio de Janeiro',
            'Rio Grande do Norte':  'Natal',
            'Rio Grande do Sul':    'Porto Alegre',
            'Rondônia':             'Porto Velho',
            'Roraima':              'Boa Vista',
            'Santa Catarina':       'Florianópolis',
            'São Paulo':            'São Paulo',
            'Sergipe':              'Aracaju',
            'Tocantins':            'Palmas',}

#   Gerar 10 arquivos
for quizNum in range (10):
    #   Cria o quiz e o arquivo com o gabarito
    quizArquivo = open('''%squizcapitais.txt''' %(quizNum + 1), 'w')
    gabaritoChaveArquivo = open('''%squizcapitais_gabarito.txt''' %(quizNum + 1), 'w') 
  
    #   Escreve o cabeçalho no arquivos
    quizArquivo.write('Nome:\nData:\n\nSérie:\n\n')
    quizArquivo.write((' ' * 20) + 'Quiz das Capitais Estaduais Brasileira(Formulário%s)' % (quizNum + 1))
    quizArquivo.write('\n\n') 

    #   Embaralha as capitais
    estados = list(capitais.keys())    
    random.shuffle(estados)
 
    #   Passa pelos 27 estados formando uma pergunta para cada
    for questaoNum in range(27):

        #    Pega as respostas certas e erradas
        respostaCerta = capitais[estados[questaoNum]]
        respostaErrada = list (capitais.values())

        del respostaErrada[respostaErrada.index(respostaCerta)]
        respostaErrada = random.sample(respostaErrada, 3)
        respostaOpcoes = respostaErrada + [respostaCerta]
        random.shuffle(respostaOpcoes)


    #    Escreve a questão e as opçoes no arquivo de pergunta:
    quizArquivo.write('%s. Qual a capital de %s?\n' % (quizNum + 1, estados [questaoNum]))    
    print('%s. Qual a capital de %s?\n' % (quizNum + 1, estados [questaoNum]))        
    for i in range (4):
        quizArquivo.write (' %s. %s\n' % ('ABCD'[i], respostaOpcoes[i]))
        print(' %s. %s\n' % ('ABCD'[i], respostaOpcoes[i]))
        quizArquivo.write ('\n')
        
    #   Escreve a resposta certa no arquivo de gabarito
    gabaritoChaveArquivo.write('%s. %s\n' % (quizNum + 1, 'ABCD'[respostaOpcoes.index(respostaCerta)]))
    print('A resposta da questão nº %s é: %s\n' % (quizNum + 1, 'ABCD'[respostaOpcoes.index(respostaCerta)] + ' - ' + respostaCerta))
    print ('------------------------------------------------------------------------')
    quizArquivo.close()
    gabaritoChaveArquivo.close()
