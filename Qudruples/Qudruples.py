#There is one problem in this code 
#It is not able to format this type of string t1=-8+9
#So updated code is in update.py file

def enteryList():
    #Taking number of entries 
    numberOfInputs = int(input("Number of entries: "))
    entry = 0
    mainList = []

    #By using while loop we will insert values in an array 
    while(entry<numberOfInputs):
        wordEntry = input("Enter the value: ")
        mainList.append(wordEntry)
        entry += 1

    #We will get our final result in this format
    final = [["result", "left", "operator", "right"]]

    for i in mainList:
        splitList = i.split("=")
        temp = [0,0,0,0]

        #If there is only assignment operator(=) and left and right value
        #Example t=8
        if(len(splitList[1]) <= 2):
            temp[0]=" "
            temp[1]=splitList[0]
            temp[2]="="
            temp[3]=splitList[1]

        #If there is result also present in the expression
        #Example t1=3-5
        else:
            temp[0]=splitList[0]
            right=""
            left=""
            operator=""
            rightTurn = False
            for i in range(len(splitList[1])):
                if(rightTurn == True):
                    right += splitList[1][i]
                    temp[3] = right
                if(splitList[1][i] == "*" or splitList[1][i] =="+" or splitList[1][i] =="/" or splitList[1][i] == "-"):
                    temp[2]=splitList[1][i]
                    rightTurn = True
                if(rightTurn == False):
                    left += splitList[1][i]
                    temp[1] = left
        final.append(temp)
    
    #Log the values
    for i in final:
        print(i)

#Function call
enteryList()


# output Example
# Number of entries: 3
# Enter the value: t1=8+9
# Enter the value: t2=t3-t6
# Enter the value: t=9
# ['result', 'left', 'operator', 'right']
# ['t1', '8', '+', '9']
# ['t2', 't3', '-', 't6']
# [' ', 't', '=', '9']