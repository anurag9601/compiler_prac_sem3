def get_first():
    num_entries = int(input("How many enteries you are going to enter: "))
    count = 0
    grammer = {}
    while(count < num_entries):
        key = input(f"Enter the left value of expre({count+1}): ")
        value = []
        temp = ""
        while(temp != "exit"):
            lst_value = input(f"Enter the right value({count+1}) or type(exit) to exit: ")
            temp = lst_value
            if(lst_value != "exit"):
                value.append(lst_value)
        temp = ""
        grammer[key] = value
        value = []
        count += 1
    
    first = {}

    for key,value in grammer.items():
        temp = []
        for i in value:
            if(i[0:2] == "id"):
                temp.append(i[0:2])
            else:
                temp.append(i[0])
        first[key] = temp
    
    for keys,values in first.items():
        for index,value in enumerate(values):
            for key in first.keys():
                if value == key:
                    if("ε" in first[key]):
                        spacial_value = []
                        for gram_keys in grammer[keys]:
                            for gram_values in gram_keys:
                                for i in first.keys():
                                    if gram_values == i:
                                        for j in first[i]:
                                            if(j != "ε"):
                                                spacial_value.append(j)
                                            else:
                                                break
                        first[keys][index] = spacial_value
                    else:
                        first[keys][index] = first[key]
    return first

print(get_first())

#Example 1

#Problem
# S -> abc|def|ghi

#output
# How many enteries you are going to enter: 1
# Enter the left value of expre(1): S
# Enter the right value(1) or type(exit) to exit: abc
# Enter the right value(1) or type(exit) to exit: def
# Enter the right value(1) or type(exit) to exit: ghi
# Enter the right value(1) or type(exit) to exit: exit
# {'S': ['a', 'd', 'g']}

#Example 2

#Problem
# S -> ABC|ghi|jkl
# A -> a|b|c
# B -> b 
# D -> d 

#output
# How many enteries you are going to enter: 4
# Enter the left value of expre(1): S
# Enter the right value(1) or type(exit) to exit: ABC
# Enter the right value(1) or type(exit) to exit: ghi
# Enter the right value(1) or type(exit) to exit: jkl
# Enter the right value(1) or type(exit) to exit: exit
# Enter the left value of expre(2): A
# Enter the right value(2) or type(exit) to exit: a
# Enter the right value(2) or type(exit) to exit: b
# Enter the right value(2) or type(exit) to exit: c
# Enter the right value(2) or type(exit) to exit: exit
# Enter the left value of expre(3): B
# Enter the right value(3) or type(exit) to exit: b
# Enter the right value(3) or type(exit) to exit: exit
# Enter the left value of expre(4): D
# Enter the right value(4) or type(exit) to exit: d
# Enter the right value(4) or type(exit) to exit: exit
# { 'S': [['a', 'b', 'c'], 'g', 'j'],
# 'A': ['a', 'b', 'c'],
# 'B': ['b'],
# 'D': ['d'] }

#Example 3
# Enter the left value of expre(1): S
# Enter the right value(1) or type(exit) to exit: ABC
# Enter the right value(1) or type(exit) to exit: exit
# Enter the left value of expre(2): A
# Enter the right value(2) or type(exit) to exit: a
# Enter the right value(2) or type(exit) to exit: b
# Enter the right value(2) or type(exit) to exit: ε
# Enter the right value(2) or type(exit) to exit: exit
# Enter the left value of expre(3): B
# Enter the right value(3) or type(exit) to exit: c
# Enter the right value(3) or type(exit) to exit: d
# Enter the right value(3) or type(exit) to exit: ε
# Enter the right value(3) or type(exit) to exit: exit
# Enter the left value of expre(4): C
# Enter the right value(4) or type(exit) to exit: e
# Enter the right value(4) or type(exit) to exit: f
# Enter the right value(4) or type(exit) to exit: ε
# Enter the right value(4) or type(exit) to exit: exit
# { 'S': [['a', 'b', 'c', 'd', 'e', 'f']],
# 'A': ['a', 'b', 'ε'],
# 'B': ['c', 'd', 'ε'],
# 'C': ['e', 'f', 'ε'] }

#Example 4

#Problem 
# E -> TE`
# E`-> *TE`|ε
# T -> FT`
# T`-> ε|+FT`
# F -> id|(E

#output
# How many enteries you are going to enter: 5
# Enter the left value of expre(1): E
# Enter the right value(1) or type(exit) to exit: TE`
# Enter the right value(1) or type(exit) to exit: exit
# Enter the left value of expre(2): E`
# Enter the right value(2) or type(exit) to exit: *TE`
# Enter the right value(2) or type(exit) to exit: ε
# Enter the right value(2) or type(exit) to exit: exit
# Enter the left value of expre(3): T
# Enter the right value(3) or type(exit) to exit: FT`
# Enter the right value(3) or type(exit) to exit: exit
# Enter the left value of expre(4): T`
# Enter the right value(4) or type(exit) to exit: ε
# Enter the right value(4) or type(exit) to exit: +FT`
# Enter the right value(4) or type(exit) to exit: exit
# Enter the left value of expre(5): F
# Enter the right value(5) or type(exit) to exit: id
# Enter the right value(5) or type(exit) to exit: (E
# Enter the right value(5) or type(exit) to exit: exit
# { 'E': [[['id', '(']]],
# 'E`': ['*', 'ε'],
# 'T': [['id', '(']], 
# 'T`': ['ε', '+'], 
# 'F': ['id', '('] }
