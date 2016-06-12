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
	if len(clusters) < 2:
		print "ERRO: Apenas um cluster identificado"
		sys.exit()
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

def getBetaCV( musicas ):
	clustersNomes = getClusters( musicas )
	clusters = separateClusters(clustersNomes, musicas)
	sumIntra = 0.0
	sumInter = 0.0
	for h in range(0, len(clusters)):#percorre todos os clusters
		for i in range(0, len(clusters[h])):#percorre cada musica do cluster
			#distancia intra-cluster
			for j in range(i+1, len(clusters[h])):#percorre cada musica intra-cluster sem repetir a combinacao
				sumIntra += getDistance(clusters[h][i], clusters[h][j])#calcula a distancia e guarda
			#distancia inter-cluster
			for k in range(h+1, len(clusters)): #percorre os outros clusters
				for l in range(0, len(clusters[k])): #percorre cada uma das musicas dos outros cluster
					sumInter += getDistance(clusters[h][i], clusters[k][l])#calcula a distancia e guarda
	return sumIntra/sumInter

def getDunn( musicas ):
	return 0

def main():
	if(len(sys.argv) != 2):
		print 'Informe o arquivo de leitura na chamada do script'
		print 'Ex: $ python main.py ./result.txt'
		sys.exit()
	musicas = readResults( str( sys.argv[1] ) )
	print 'SSE = ',getSSE( musicas )
	print 'BetaCV = ',getBetaCV( musicas )
main()