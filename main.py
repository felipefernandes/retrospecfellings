# -*- coding: utf-8 -*-
# encoding=utf8  
import sys 
import csv
from textblob import TextBlob
from datetime import datetime

reload(sys)  
sys.setdefaultencoding('utf8')
now = datetime.now()

# Todo:
# - montar uma visão gráfica do score de sentimento classificado
# - Fazer separação por projeto (um por coluna) da análise

dic_retro = ""

# openCSV
# abre o arquivo CSV e retorna uma variável com o arquivo
# 
def openCSV(csv_file):
    dic_retrospectiva = ' '
    with open(csv_file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            dic_retrospectiva += ' ' + ' '.join(row) 

    return dic_retrospectiva

# translateTerms
# traduz termos de uma string para inglês
# 
def translateTerms(dic):
    dictonary = TextBlob(dic)
    if dictonary.detect_language() != 'en':
        traducao = dictonary.translate(to='en')
    else:
        traducao = dictonary
    return traducao        

# sentimentAnalysis
# usa o arquivo CSV como base e o converte em uma variavel
# depois usa um analisador de sentimento
# 
def sentimentAnalysis(csv_file_retro):   
    terms = translateTerms(openCSV(csv_file_retro))
    theSentiment = terms.sentiment    
    Polarity = int(round(terms.sentiment.polarity*100))

    if Polarity < 0:
        polarityResult = 'Negativo'
    elif Polarity == 0:
        polarityResult = 'Neutro'
    else:
        polarityResult = 'Positivo'

    print '-----------------------'
    print '{0}/{1}/{2}'.format(now.day, now.month, now.year)
    print 'Arquivo analisado: {0}'.format(csv_file_retro)
    print 'Subjetividade: {0}%'.format(int(round(terms.sentiment.subjectivity*100)))
    print 'Polaridade: {0}% {1}'.format(int(round(terms.sentiment.polarity*100)), polarityResult)
    print '-----------------------'

# executa a analise
sentimentAnalysis('retro-analise.csv')