from scipy.spatial import distance #sudo apt-get install python-scipy
from musica import Musica
import sys

def readComments( nome_arquivo ):
    musicas = []
    arquivo = open( nome_arquivo, 'r' )
    for linha in arquivo:
        musica = linha.replace('\n','').split(',')
        musicas.append( Musica(musica[len(musica)-1], musica[:len(musica)-1]) )
    arquivo.close()
    return musicas

def toIntVector( stringList ):
	output = []
	for item in stringList:
		output.append( int(item) )
	return output

def getDistance( v1, v2 ):
	print 'teste'

musicas = readComments( 'teste' )
for musica in musicas:
	print musica
print distance.euclidean(musicas[0].getTagsBin(),musicas[2].getTagsBin())