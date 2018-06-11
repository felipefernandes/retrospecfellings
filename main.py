# -*- coding: utf-8 -*-

dic_palavra_polaridade = {}

# abre o lexico
sentilexpt = open("SentiLex-PT01/SentiLex-lem-PT01.txt",'r')

# processa e cria o dicionario de sentimentos
for i in sentilexpt.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra_polaridade[palavra] = polaridade

# print (dic_palavra_polaridade)

# print (dic_palavra_polaridade.get('abusivo'))

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
# - abrir o arquivo CSV
# - ler os dados corretos
# - aplicar o score de sentimento
# - armazenar o score de sentimento
# - montar uma visão gráfica do score de sentimento classificado

print Score_sentimento("Eu estou muito feliz hoje, porém, triste com a politica")
print Score_sentimento("Estou Muito Feliz hoje,super animado com o trabalho novo! :)")
print Score_sentimento("Estou muito triste, desanimado com algumas coisas…")