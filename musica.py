class Musica:
	def __init__(self, cluster, tags):
		self.cluster = cluster
		self.tags = tags
	def __str__( self ):
		return self.cluster+' => '+' '.join(self.tags)

	def getTagsBin( self ):
		outputBin = []
		for item in self.tags:
			outputBin.append( float(item) )
		return outputBin