import csv
import os

fileToRead = "dataset/train_data.csv"  #file cvs di partenza
#fileToWrite = "train_data.arff" #se voglio l'arff file
fileToWrite = "dataset/train_data_mappato.csv" #nome del file output
relation = "Parrot" #relazione

writeFile = open(fileToWrite, 'w') #apertura file 
#Apertura e lettura file csv
f = open(fileToRead, 'r')
reader = csv.reader(f)
allData = list(reader)
attributes = allData[0] #attributi=sentiment e content
totalCols = len(attributes) #2 colonne
totalRows = len(allData) #30001 righe
f.close() 

'''
#Per file arff
#Relazioni
writeFile.write("@RELATION " + relation + "\n\n")
writeFile.write("@ATTRIBUTE text STRING" + "\n")
writeFile.write("@ATTRIBUTE @@class@@ {love, joy, surprise, anger, sadness, fear}" + "\n")
'''

writeFile.write("sentiment" "," "content" "\n")

i=1
while i<len(allData):
	if allData[i][0]=="enthusiasm":
		allData[i][0]="joy"

	if allData[i][0]=="worry":
		allData[i][0]="fear"

	if allData[i][0]=="fun":
		allData[i][0]="joy"

	if allData[i][0]=="worry":
		allData[i][0]="fear"

	if allData[i][0]=="hate":
		allData[i][0]="anger"

	if allData[i][0]=="happiness":
		allData[i][0]="joy"
	
	if allData[i][0]=="relief":
		allData[i][0]="joy"

	if allData[i][0]=="boredom":
		allData[i][0]="sadness"

	if allData[i][0]=="empty":
		allData.pop(i)
		i=i-1
	elif allData[i][0]=="neutral":
		allData.pop(i)
		i=i-1
	i=i+1



# Show Data
totalRowsfinal = len(allData)
#writeFile.write("\n@DATA\n")

for i in range(1,totalRowsfinal):
	#allData[i].reverse()
	#allData[i][0]="\""+allData[i][0]+"\""
	#print(allData[i][0])
	writeFile.write(','.join(allData[i])+"\n")
