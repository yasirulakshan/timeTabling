import csv

# inputFileName = input("Enter the name of the input file: ")
# outputFileName = input("Enter the name of the output file: ")

inputFileName = "input_file.csv"
outputFileName = "output_file.csv"

inpt = []

# read input file
with open(inputFileName, 'r') as inputFile:
    csvReader = csv.reader(inputFile)

    for row in csvReader:
        inpt.append(row)

rooms = inpt.pop(-1)

