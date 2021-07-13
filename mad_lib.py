#! python3

#   Mad Libs
#       Este programa preenche um texto pré-existente com dados definidos pelo usuário. São eles:
#       ADJETIVO, SUBSTANTIVO, ADVÉRBIO E VERBO.
#       Tentei utilizar aqui o conhecimento adquirido através dos capítulos 7, 8 (1ªversão) e 8 (2ª versão) do livro.
#-----------------------------------------------------------------------------------------------------------------------
#   REFERÊNCIA BIBLIOGRÁFICA:
#       SWEIGART, Al. Automate the Boring Stuff, c2019. Chapter 8, Reading and Writing Files.
#       Disponível em: https://automatetheboringstuff.com/chapter8/. Acesso em: 12 de jul. de 2021.

#       ______. Automate the Boring Stuff, c2019. Chapter 8, INPUT VALIDATION.
#       Disponível em: https://automatetheboringstuff.com/2e/chapter8/. Acesso em: 12 de jul. de 2021.

#       ______. Automate the Boring Stuff, c2019. Chapter 7, PATTERN MATCHING WITH REGULAR EXPRESSIONS.
#       Disponível em: https://automatetheboringstuff.com/2e/chapter7/. Acesso em: 12 de jul. de 2021.

#-----------------------------------------------------------------------------------------------------------------------

import os, re, pyinputplus as pyip

#   Localiza o arquivo de texto, abre-o e mostra o conteúdo, antes do preenchimento.
texto = open('texto.txt')
textoLer = texto.read()
print(textoLer)

#   Cria variáveis para: ADJETIVO, SUBSTANTIVO, ADVÉRBIO E VERBO.
#   Solicita ao usuário que preencha os dados e reatribui às variáveis.
adjetivo = pyip.inputStr('Informe o adjetivo: ')
substantivo = pyip.inputStr('Informe o substantivo: ')
verbo = pyip.inputStr('Informe o verbo: ')

###   3: Usa REGEX para encontrar os dados e atribuir a eles as variáveis.
subsTextoLer = re.compile(r'\*(ADJETIVO|VERBO|SUBSTANTIVO)\*')

textoLer = re.sub(subsTextoLer,adjetivo, textoLer,1)
textoLer = re.sub(subsTextoLer,substantivo, textoLer,1)
textoLer = re.sub(subsTextoLer,verbo, textoLer,1)

#   5: Apresentar o texto preenchido com informações do usuário e criar novo arquivo de texto.
print(textoLer)
textoNovo = open('texto_novo.txt', 'w')
textoNovo.write(textoLer)
textoNovo.close()
texto.close()
