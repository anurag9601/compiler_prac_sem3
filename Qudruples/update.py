def Quadruples():
    numerOfInput = int(input("Number of input: "))
    count = 0
    mainList = []
    operators = ["+","-","*","/","%"]
    result = [["result","left","operator","right"]]
    while(count < numerOfInput):
        entry = input(f"Entry ({count+1}) : ")
        mainList.append(entry)
        count += 1
    for i in mainList:
        temp_lst = []
        first_operator = False
        splitList = i.split("=")
        temp_lst.append(splitList[0])
        for i in operators:
            if(splitList[1][0] == i):
                first_operator = True
        if(first_operator == True):
            temp_str = ""
            right_turn = False
            temp_str += splitList[1][0]
            for j in range(1,len(splitList[1])):
                if(right_turn == True):
                    temp_str += splitList[1][j]
                else:
                    for i in operators:
                        if(splitList[1][j] == i):
                            temp_lst.append(temp_str)
                            temp_str = ""
                            temp_str += splitList[1][j]
                            temp_lst.append(temp_str)
                            temp_str = ""
                            right_turn = True
                    if(right_turn == False):
                        temp_str += splitList[1][j]
            temp_lst.append(temp_str)
            result.append(temp_lst)
        else:
            is_operator = False
            for i in operators:
                for j in splitList[1]:
                    if(i==j):
                        is_operator = True
            if(is_operator):
                for i in splitList[1]:
                    for j in operators:
                        if(i==j):
                            short_split = splitList[1].split(i)
                            temp_lst.append(short_split[0])
                            temp_lst.append(i)
                            temp_lst.append(short_split[1])
                            result.append(temp_lst)
                            break
            else:
                temp_lst.append(" ")
                temp_lst.append("=")
                temp_lst.append(splitList[1])
                result.append(temp_lst)
    for i in result:
        print(i)
                          
Quadruples()
    