# -*- coding: utf-8 -*-

import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):\n")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):\n")

    return textos

def separa_palavras(frase):
    #A funcao recebe um texto e devolve uma lista das palavras dentro dele
    return frase.split()

def separa_sentencas(texto):
    #A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
    
def separa_frases(sentenca):
    #A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def n_palavras_diferentes(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_palavras_unicas(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras(texto):
    return len(lista_palavras(texto))

def caractere_palavras(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = list()
    for i in frs:
        x = separa_palavras(i)
        plvr += x
        
    s = 0
    for i in plvr:
        s += len(i)
    return s

def caractere_sentencas(texto):
    stnc = separa_sentencas(texto)
    frs = 0
    for i in stnc:
        x = len(i)
        frs += x
    return frs

def caractere_frases(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = 0
    for i in frs:
        x = len(i)
        plvr += x
    return plvr

def conta_frases(texto):
    c = separa_sentencas(texto)
    frases = []
    for w in c:
        f = separa_frases(w)
        frases += f
    return len(frases)

def conta_sentencas(texto):
    return len(separa_sentencas(texto))

def lista_palavras(texto):
    stnc = separa_sentencas(texto)
    frs = list()
    for i in stnc:
        x = separa_frases(i)
        frs += x
    plvr = list()
    for i in frs:
        x = separa_palavras(i)
        plvr += x
    return plvr

def wal(texto):
    return caractere_palavras(texto) / n_palavras(texto)

def ttr(texto):
    return n_palavras_diferentes(lista_palavras(texto)) / n_palavras(texto)

def hlr(texto):
    return n_palavras_unicas(lista_palavras(texto)) / n_palavras(texto)

def sal(texto):
    return caractere_sentencas(texto) / conta_sentencas(texto)

def sac(texto):
    return conta_frases(texto) / conta_sentencas(texto)

def pal(texto):
    return caractere_frases(texto) / conta_frases(texto)
    
def calcula_assinatura(texto):
    
    vwal = wal(texto)
    #print("Tamanho medio de palavra: ", vwal)
    vttr = ttr(texto)
    #print("Relação Type-Token: ", vttr)
    vhlr = hlr(texto)
    #print("Razão Hapax Legomana: ", vhlr)
    vsal = sal(texto)
    #print("Tamanho médio de sentença: ", vsal)
    vsac = sac(texto)
    #print("Complexidade média da sentença: ", vsac)
    vpal = pal(texto)
    #print("Tamanho medio de frase: ", vpal)
    return [vwal, vttr, vhlr, vsal, vsac, vpal]
    

def compara_assinatura(ass_cp,as_b):
    i = 0
    x = 0
    s = 0
    ca = list()
    while i<=5:
        x = ass_cp[i]-as_b[i]
        if x<0:
            ca.append(x*-1)
        else:
            ca.append(x)
        i += 1
    
    for i in ca:
        x = i
        s += x
    
    return s/6
    
    
    
    

def avalia_textos(lista_textos, ass_cp):
    ca = []
    for i in lista_textos:
        as_b = calcula_assinatura(i)
        ca.append(as_b)
    cpa = []
    for i in ca:
        x = compara_assinatura(ass_cp,i)
        cpa.append(x)
    return cpa.index(min(cpa))+1
        
        
    
        
        
    
    
ass_cp = le_assinatura()

lista_textos = le_textos()

print ('O autor do texto', avalia_textos(lista_textos, ass_cp), 'está infectado com COH-PIAH')
    