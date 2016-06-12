from scipy.spatial import distance #sudo apt-get install python-scipy
from musica import Musica
import sys, numpy, math

def readResults( nome_arquivo ):
    musicas = []
    arquivo = open( nome_arquivo, 'r' )
    for linha in arquivo:
        musica = linha.replace('\n','').split(',')
        musicas.append( Musica(musica[len(musica)-1], musica[:len(musica)-1]) )
    arquivo.close()
    return musicas

def getIndex(list_item, search):
	index = 0
	for item in list_item:
		if item == search:
			return index
		index += 1

def getDistance( v1, v2 ):
	return distance.euclidean( v1, v2 )

def getClusters( musicas ):
	clusters = []
	for musica in musicas:
		if musica.cluster not in clusters:
			clusters.append( musica.cluster )
	return clusters

def separateClusters( clusters, musicas ):
	clusters_output = []
	for i in range(0, len(clusters)):
		clusters_output.append([])
	for musica in musicas:
		index = getIndex( clusters, musica.cluster )
		clusters_output[index].append( musica.getTagsBin() )
	return clusters_output

def getSSE( musicas ):
	clusters = getClusters( musicas )
	clustersSeparados = separateClusters(clusters, musicas)
	sse = 0.0
	for cluster in clustersSeparados:
		media = numpy.average(cluster, axis=0) #calcula vetor medio para calculo de variancia
		for musica in cluster:
			dist = math.pow( getDistance(musica, media), 2) #distancia da media ao quadrado
			sse += dist
	return sse

def main():
	if(len(sys.argv) != 2):
		print 'Informe o arquivo de leitura na chamada do script'
		print 'Ex: $ python main.py ./result.txt'
		sys.exit()
	musicas = readResults( str( sys.argv[1] ) )
	print 'SSE = ',getSSE(musicas)
main()