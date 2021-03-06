#Maxim Strzebkowski
#07.01.2018
#Vocabel Trainer

import random
import os

def createVariableList(filename):
	variableList = {}
	try:
		file = open(filename,'r')
	except:
		print("No such file: "+filename)
		return False
	for i in file.readlines():
		infinitive, simplePast, pastParticiple = i.split(':')
		pastParticiple = pastParticiple[:-1]
		variableList[infinitive] = [infinitive,simplePast,pastParticiple]
	file.close()
	return variableList

def createStatisticList(filename):
	statisticList = {}
	try:
		file = open(filename, 'r')
	except:
		print("No such file: "+filename)
		return False
	for i in file.readlines():
		word, stats, percent = i.split(':')
		percent = percent[:-2]
		rights, askedAmount = stats.split('/')
		
		statisticList[word] = [int(rights), int(askedAmount),int(percent)]
	file.close()
	return statisticList

def getKey(item):
	return item[1]

def sortStats(stats):
	sortedStats = []
	for word in stats:
		sortedStats.append([word,stats[word][2]])
	sortedStats.sort(key=getKey)
	return sortedStats

def writeStats(statFile,stats):
	file = open(statFile, 'w')
	sStats = sortStats(stats)
	for i in sStats:
		stats[i[0]][2] = int((float(stats[i[0]][0]) / float(stats[i[0]][1]))*100)
		file.write(i[0]+":"+str(stats[i[0]][0])+"/"+str(stats[i[0]][1])+":"+str(stats[i[0]][2])+"%\n")
	file.close()

def allKeys(vocFile):
	variables = createVariableList(vocFile)
	vocs = []
	for i in variables:
		vocs.append(i)
	return vocs

def createMini(length, vocFile):
	vocs = allKeys(vocFile)
	miniVocs = []
	for i in range(length):
		randomWord = random.choice(vocs)
		while randomWord in miniVocs:
			randomWord = random.choice(vocs)
		miniVocs.append(randomWord)
	return miniVocs

def printWrong(variables, key):
	print("Wrong!")
	print("Correct answers would be: ")
	print("Verb: "+variables[key][0])
	print("simple past: "+variables[key][1])
	print("Past participle: "+variables[key][2])
	raw_input("press ENTER to continue...")

def printResult(vocs, correct, testTimes, incorrect):
	os.system('clear')
	print("your score is "+str(correct)+"/"+str(testTimes))
	if int(correct) != int(testTimes):
		print("Words you didn't know: ")
	for i in incorrect:
		print(i)
	raw_input("press ENTER to return to menu...")

def test(vocs,stats, vocFile, statFile):
	variables = createVariableList(vocFile)
	correct = 0
	testTimes = len(vocs)
	incorrect = []
	for i in range(testTimes):
		word = random.choice(vocs)
		vocs.remove(word)
		stats[word][1] += 1
		os.system('clear')
		print(str((testTimes - i))+" Words to go")
		print("Verb: "+variables[word][0])
		userSimplePast = raw_input("Simple past: ")
		userPastParticiple = raw_input("Past participle: ")
		if userSimplePast == variables[word][1]:
			if userPastParticiple == variables[word][2]:
				print("Your answers were correct")
				raw_input("press ENTER to continue...")
				correct += 1
				stats[word][0] += 1
				stats[word][2] = int((float(stats[word][0]) / float(stats[word][1]))*100)
				continue
		stats[word][2] = int((float(stats[word][0]) / float(stats[word][1]))*100)
		printWrong(variables, word)
		incorrect.append(word)
	writeStats(statFile, stats)
	printResult(vocs, correct, testTimes, incorrect)

def lowest(statFile):
	sStats = sortStats(createStatisticList(statFile))
	lowest = []
	lowList = []
	for i in range(25):
		lowest.append(sStats[i][0])
	for i in range(10):							
		randomWord = random.choice(lowest)
		while randomWord in lowList:
			randomWord = random.choice(lowest)
		lowList.append(randomWord)
	return lowList

def lowTest(vocFile, statFile):
	vocs = lowest(statFile)
	test(vocs, createStatisticList(statFile), vocFile, statFile)

def miniTest(vocFile, statFile):
	length = int(raw_input("Length of the Test (Words): "))
	vocs = createMini(length, vocFile)
	test(vocs, createStatisticList(statFile), vocFile, statFile)

def fullTest(vocFile, statFile):
	vocs = allKeys(vocFile)
	test(vocs, createStatisticList(statFile), vocFile, statFile)

def showStats(vocFile, statFile):
	os.system('clear')
	file = open(statFile, 'r')
	for i in file.readlines():
		print(i[:-1])
	file.close()
	raw_input("press ENTER to return to menu...")

def kill(vocFile, statFile):
	choice = raw_input("Are you sure? [y/n]: ")
	if choice == "y":
		return False
	elif choice == "n":
		return True

def menu():
	running = True
	options = {"1": fullTest, "2": miniTest, "3": lowTest, "4": showStats, "5": kill}
	vocFile = 'Vocs.txt'
	statFile = 'ZuLernen.txt'
	while running:
		os.system('clear')
		print("[1] Full Test")
		print("[2] Small Test")
		print("[3] Low Test")
		print("[4] Show stats")
		print("[5] Exit")
		#try:
		running = options[raw_input("Choice: ")](vocFile, statFile)
		if running == None:
			running = True
		#except:
			#print("Not a valid choice...")
			#raw_input("press ENTER to continue")

menu()
	