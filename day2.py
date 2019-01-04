import string

#Solves Part 1
#Counts each letter in each line of the input
#If there is 1, increased count and enables the flag so we have EXACTLY one per line
#Multiplies the double and triple count
def part1():
    letters = list(string.ascii_lowercase)
    countDouble = 0
    doubleFlag = False
    countTriple = 0
    tripleFlag = False
    with open("input.txt") as f:
        for line in f:
            doubleFlag = False
            tripleFlag = False
            for value in letters:
                if line.count(value) == 2 and doubleFlag is False:
                    countDouble += 1
                    doubleFlag = True
                if line.count(value) == 3 and tripleFlag is False:
                    countTriple += 1
                    tripleFlag = True

    print(countDouble*countTriple)

#Solves Part 2
#Iterates through input line by line
#Compares each individual letter with the corresponding letters of another line
#If the it differs by 1 letter, print the string without that letter
######Terrible Complexity of O(N^3)
######Need to try zip() method next
def part2():
    boxID = []
    answer = " "
    differing = 0
    with open("input.txt") as f:
        for line in f:
            boxID.append(line)
    for i in range(0, len(boxID)):
        for j in range(i+1, len(boxID)):
            for k in range(0, len(boxID[0])):
                if(boxID[i][k] != boxID[j][k]):
                    differing += 1
                elif(boxID[i][k] == boxID[j][k]):
                    answer += boxID[i][k]
                if differing > 1:
                    differing = 0
                    answer = []
                    break
            if differing == 1:
                print("".join(answer))

if __name__ == "__main__":
    part1()
    part2()