#!/usr/bin/env python

import sys
import os
from pygraphviz import *



def quantos_pais( G, n ):
	qtd = 0

	hue = G.edges()
	for i in range( len(hue) ):
		if (n == hue[i][1]):
			qtd = qtd + 1


	return qtd


def quantos_filhos( G, n ):
	qtd = 0

	hue = G.edges()
	for i in range( len(hue) ):
		if (n == hue[i][0]):
			qtd = qtd + 1

	return qtd


def checar_atributos( n ):

        if (not n.attr['qtd_pais']):
	    n.attr['qtd_pais'] = quantos_pais(G, n)
        if (not n.attr['qtd_filhos']):
	    n.attr['qtd_filhos'] = quantos_filhos(G, n)

	return n
    

def calcula_char(v):
    a = list(v)
    
    #print len(a)
    #print v
    
    l = len(a)-1 
    new = ord(a[l]) + 1
    if ( new > 57 ):
        print "MAIS QUE PODE >>", new
        if ( l == 1 ):
            a[0] = 48
            a[1] = 47
        else:
            a[0] = ord(a[0]) + 1
            a[1] = 47

    return str(a)


def atualiza_atributos( n, f ):
    if ( int(n.attr['qtd_filhos']) != 0 ):
    
        for hue in f.attr:
            if ( hue != 'qtd_pais' and hue != 'qtd_filhos' ):
                
                if (n.attr[hue]):
                    #n.attr[hue] = str(ord(n.attr[hue]) + 1)
                    #n.attr[hue] = calcula_char(n.attr[hue])
                    #print (ord(n.attr[hue]))
                    n.attr[hue] = int(n.attr[hue]) + 1
                    #print n, " = ",  hue, "-->" , n.attr[hue]
                else:
                    n.attr[hue] = 1
        
    return n


def calcula_zuera( G, n, f ):
        
        n = checar_atributos( n )
        qtd_pais = int(n.attr['qtd_pais'])
        ini = len(G[n]) - 1
        fim = (ini - qtd_pais)
        if ( fim < (-1) ):
            fim = -1

        for i in range( ini, fim, -1 ):
            edges = G[n]
            
            # Para cada atributo de f (folha), se diferente de 'qtd_pais' e 'qtd_filhos', adicionar +1 ou criar atributo em n 
            n = atualiza_atributos(n, f)
            calcula_zuera( G, G[n][i], f )
        
        if ( fim == ini ):
            n = atualiza_atributos(n, f)
        
        return




# **************************** Main ***************************** #

f_out = "tmp.dot"
out = open(f_out, "w")
for line in sys.stdin:
    print >> out, line,
out.close()

G=AGraph(f_out)

for hue in G:
	n = G.get_node(hue)
        n = checar_atributos( n )

	if ( int(n.attr['qtd_filhos']) == 0):
		#fazer uma para o filho e o caminho ateh chegar na raiz
                calcula_zuera( G, n, n )


#print G.string()
for hue in G:
	n = G.get_node(hue)
	del n.attr['qtd_pais']
        if ( n.attr['qtd_filhos'] ):
	    del n.attr['qtd_filhos']
	#print hue, '-->' ,
	#for j in range( len(G[hue]) ):
	#	print G[hue][j], 
	#print n.attr


print ''
s = G.string().expandtabs(2)
print s

#G.layout(prog='dot')
#G.draw('file.png')

os.remove(f_out)

