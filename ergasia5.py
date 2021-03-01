import random

SOS = []
print("give height of the board: ")
height = input()
height = int(height)
print("give length of the board: ")
length = input()
length = int(length)
for m in range(100):
    line1 = []
    line1len = (height*length)
    line1len2 = float(line1len)
    for i in range(line1len):
            if i > line1len2/2:
                line1.append("O")
            else:
                line1.append("S")
    random.shuffle(line1)
    line2 = []
    for y in range(height):
        line2.append([])
        for x in range(length):
                line2[y].append(line1.pop(0))
    SOS.append(0)
    for x in range(length-2):
        for y in range(height):
            if line2[y][x] == "S" and line2[y][x+1] == "O" and line2[y][x+2] == "S":
                SOS[m] += 1
    for x in range(length):
        for y in range(height-2):
            if line2[y][x] == "S" and line2[y+1][x] == "O" and line2[y+2][x] == "S":
                SOS[m] += 1
    for x in range(length-2):
        for y in range(height-2):
            if line2[y][x] == "S" and line2[y+1][x+1] == "O" and line2[y+2][x+2] == "S":
                SOS[m] += 1
summarySOS=0
for k in range(len(SOS)-1):
    summarySOS += SOS[k]
averageSOS = summarySOS/len(SOS)
print("The average of this sequence in a range of 100 times is: ", averageSOS)
