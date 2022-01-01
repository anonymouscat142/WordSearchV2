#set uppy stuff
word = "none selected"
i=0
lines = []

#read grid
with open('C:/Users/Lhotse/Desktop/Python/code/wordsearch.txt') as f:
    lines = f.readlines()
count = 0
for line in lines:
    count += 1    
print(lines)
numOfLines = len(lines)
#line = input("enter the first line")
word = input("enter word to find: ")
while(i<len(lines)):
    line = lines[i]
    #check lines foreward
    print("checking foreward...")
    if word in line:
        print("at index " + str(line.index(word)) + ", line " + str(i+1))
        print(line.replace(word,word.upper()))
        lines[i] = line
        quit()
    #check line backwards
    print("checking backwards...")
    lineBackwards = line [::-1]
    if word in lineBackwards:
        print("at index " + str(lineBackwards.index(word)) + str(i+1))
        lineBackwards = lineBackwards.replace(word,word.upper())
        line = lineBackwards [::-1]
        print(line)
        lines[i] = line
        quit()
    else:
        print("not in line " + str(i + 1))
        print("line searched: " + line)
        print("_____________________")
    i+=1
print("___________________________________________________")

print("searching virticals")
tempLine = lines[0]
i = 0
i2 = 0
lineLength = len(tempLine)
while(i2<len(tempLine)):
    i=0
    virticalLine = ""
    while(i<lineLength):
        try:
            tempLine = lines[i]
            virticalLine = virticalLine + tempLine[i2]
        except:
            break
        i+=1
    line = virticalLine
    print(virticalLine)

    #check lines foreward
    print("checking down...")
    if word in line:
        print("at index " + str(line.index(word)) + ", line " + str(i+1) + " " + "line " + str(i2))
        print(line.replace(word,word.upper()))
        quit()
    #check line backwards
    print("checking up...")
    lineBackwards = line [::-1]
    if word in lineBackwards:
        print("at index " + str(lineBackwards.index(word)) + str(i+1) + " " + "line " + str(i2))
        lineBackwards = lineBackwards.replace(word,word.upper())
        line = lineBackwards [::-1]
        print(line)
        quit()
    else:
        print("not in line " + str(i + 1))
        print("line searched: " + line)
        print("_____________________")
    i2+=1
print("_________________________________________")
i=0
i2=0
repeat = len(line)
print("checking diagonals left to right")
while(i2<repeat):
    #get diagonal
    i=0
    DiagonalLine = ""
    while(i<numOfLines):
        try:
            tempLine = lines[i]
            DiagonalLine = DiagonalLine + tempLine[i+i2]
        except:
            break
        i+=1
    line = DiagonalLine
    #check lines foreward
    print("checking diagonal top left to bottom right...")
    if word in line:
        print("at index " + str(line.index(word)) + ", line " + str(i+1))
        print(line.replace(word,word.upper()))
        lines[i] = line
        quit()
    #check line backwards
    print("checking diagonal botton right to top left...")
    lineBackwards = line [::-1]
    if word in lineBackwards:
        print("at index " + str(lineBackwards.index(word)) + str(i+1))
        lineBackwards = lineBackwards.replace(word,word.upper())
        line = lineBackwards [::-1]
        print(line)
        lines[i] = line
        quit()
    else:
        print("not in line " + str(i + 1))
        print("line searched: " + line)
        print("_____________________")
    i2+=1
print("___________________________________________________")
i2=0
while(i2<repeat):
    #get diagonal
    i=0
    DiagonalLine = ""
    while(i<numOfLines):
        try:
            tempLine = lines[i+i2]
            DiagonalLine = DiagonalLine + tempLine[i]
        except:
            break
        i+=1
    line = DiagonalLine
    #check lines foreward
    print("checking diagonal top left to bottom right...")
    if word in line:
        print("at index " + str(line.index(word)) + ", line " + str(i+1) + " " + "line " + str(i2))
        print(line.replace(word,word.upper()))
        lines[i] = line
        quit()
    #check line backwards
    print("checking diagonal botton right to top left...")
    lineBackwards = line [::-1]
    if word in lineBackwards:
        print("at index " + str(lineBackwards.index(word)) + str(i+1) + " " + "line " + str(i2))
        lineBackwards = lineBackwards.replace(word,word.upper())
        line = lineBackwards [::-1]
        print(line)
        lines[i] = line
        quit()
    else:
        print("not in line " + str(i + 1))
        print("line searched: " + line)
        print("_____________________")
    i2+=1
print("___________________________________________________")

print("checking diagonals right to left...")

i=0
i2=0
repeat = len(line)
while(i2<repeat):
    #get diagonal
    i=0
    DiagonalLine = ""
    while(i<numOfLines):
        try:
            tempLine = lines[i]
            tempLine = tempLine[:: -1]
            DiagonalLine = DiagonalLine + tempLine[i+i2]
        except:
            break
        i+=1
    line = DiagonalLine
    #check lines foreward
    print("checking diagonal top left to bottom right...")
    if word in line:
        print("at index " + str(line.index(word)) + ", line " + str(i+1))
        print(line.replace(word,word.upper()))
        lines[i] = line
        quit()
    #check line backwards
    print("checking diagonal botton right to top left...")
    lineBackwards = line [::-1]
    if word in lineBackwards:
        print("at index " + str(lineBackwards.index(word)) + str(i+1))
        lineBackwards = lineBackwards.replace(word,word.upper())
        line = lineBackwards [::-1]
        print(line)
        lines[i] = line
        quit()
    else:
        print("not in line " + str(i + 1))
        print("line searched: " + line)
        print("_____________________")
    i2+=1
print("___________________________________________________")
i2=0
while(i2<repeat):
    #get diagonal
    i=0
    DiagonalLine = ""
    while(i<numOfLines):
        try:
            tempLine = lines[i+i2]
            tempLine = tempLine[:: -1]
            DiagonalLine = DiagonalLine + tempLine[i]
        except:
            break
        i+=1
    line = DiagonalLine
    #check lines foreward
    print("checking diagonal top right to bottom left...")
    if word in line:
        print("at index " + str(line.index(word)) + ", line " + str(i+1) + " " + "line " + str(i2))
        print(line.replace(word,word.upper()))
        lines[i] = line
        quit()
    #check line backwards
    print("checking diagonal botton left to top right...")
    lineBackwards = line [::-1]
    if word in lineBackwards:
        print("at index " + str(lineBackwards.index(word)) + str(i+1) + " " + "line " + str(i2))
        lineBackwards = lineBackwards.replace(word,word.upper())
        line = lineBackwards [::-1]
        print(line)
        lines[i] = line
        quit()
    else:
        print("not in line " + str(i + 1))
        print("line searched: " + line)
        print("_____________________")
    i2+=1
print("___________________________________________________")

print("not found!")
quit()