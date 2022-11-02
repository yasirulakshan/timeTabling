import csv


# inputFileName = input("Enter the name of the input file: ")
# outputFileName = input("Enter the name of the output file: ")


class Subject:
    def __init__(self, id, varient, timeSlots, choosenTimeSlot, choosenRoom):
        self.id = id
        self.varient = varient
        self.timeSlots = timeSlots
        self.choosenTimeSlot = choosenTimeSlot
        self.choosenRoom = choosenRoom


def findCount(arr, element):
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count += 1
    return count


inputFileName = "input_file.csv"
outputFileName = "output_file.csv"

inpt = []

# read input file
with open(inputFileName, 'r') as inputFile:
    csvReader = csv.reader(inputFile)

    for row in csvReader:
        inpt.append(row)

rooms = inpt.pop(-1)

subjects = []

for i in inpt:
    subjects.append(Subject(i[0], i[1], i[2:], None, None))

compalsory = []
optional = []

subject_finalized = 0

while subject_finalized < len(inpt):
    subject = subjects[subject_finalized]
    timeGot = False
    for time in subject.timeSlots:
        if subject.choosenTimeSlot is None or time not in subject.choosenTimeSlot:
            if time not in compalsory:
                if subject.varient == "c":
                    compalsory.append(time)
                    subject.choosenTimeSlot = time
                    subject.choosenRoom = rooms[0]
                    subject_finalized += 1
                    timeGot = True
                    break
                else:
                    timeCount = findCount(optional, time)
                    if timeCount < len(rooms):
                        optional.append(time)
                        subject.choosenTimeSlot = time
                        subject.choosenRoom = rooms[timeCount]
                        subject_finalized += 1
                        timeGot = True
                        break

    if not timeGot:
        if subject.varient == "c":
            if subject.choosenTimeSlot in compalsory:
                compalsory.remove(subject.choosenTimeSlot)
        else:
            if subject.choosenTimeSlot in optional:
                optional.remove(subject.choosenTimeSlot)
        subject.choosenTimeSlot = None
        subject.choosenRoom = None
        subject_finalized -= 1

for subject in subjects:
    print(subject.id, subject.choosenTimeSlot, subject.choosenRoom)