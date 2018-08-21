# -*- coding: utf-8 -*-

import csv

dic_palavra_polaridade = {}
dic_retro = ""

# abre o lexico
sentilexpt = open("SentiLex-PT01/SentiLex-lem-PT01.txt",'r')

# processa e cria o dicionario de sentimentos
for i in sentilexpt.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra_polaridade[palavra] = polaridade

def Score_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []
    for p in frase.split():
        l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))
    score = sum(l_sentimento)
    if score > 0:
        return 'Positivo, Score: {}'.format(score)
    elif score == 0:
        return 'Neutro, Score: {}'.format(score)
    else:
        return 'Negativo, Score: {}'.format(score)
        
# Todo:
# - armazenar o score de sentimento
# - montar uma visão gráfica do score de sentimento classificado

with open('retro-analise.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        dic_retro = ', '.join(row)
    
# print (dic_palavra_polaridade)

# print (dic_palavra_polaridade.get('abusivo'))

#print Score_sentimento("Eu estou muito feliz hoje, porém, triste com a politica")
#print Score_sentimento("Estou Muito Feliz hoje,super animado com o trabalho novo! :)")
#print Score_sentimento("Estou muito triste, desanimado com algumas coisas…")

print Score_sentimento(dic_retro)