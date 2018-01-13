
def sortIt():
	file = open('Vocs.txt','r')
	words = []
	for i in file.readlines():
		word, something, somethingElse = i.split(':')
		words.append(word)
	file.close()
	file = open('ZuLernen.txt','w')
	for i in words:
		file.write(i+":0/1:100%\n")
	file.close()

sortIt()