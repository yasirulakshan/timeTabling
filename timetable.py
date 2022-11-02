import csv

inputFileName = input("Enter the name of the input file: ")
outputFileName = input("Enter the name of the output file: ")

inpt = []

#read input file
with open(inputFileName, 'r') as inputFile:
    csvReader = csv.reader(inputFile)

    for row in csvReader:
        inpt.append(row)

print(inpt)