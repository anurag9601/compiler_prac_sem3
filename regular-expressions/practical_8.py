def accept_string(input_string):
    if(len(input_string)<3):
        return "REJECTED"
    else:
        if(input_string[0]=="1"):
            if(input_string[1]=="0"):
                if(input_string[2]=="1"):
                    for i in range(3,len(input_string)):
                        if(input_string[i]!="1"):
                            return "REJECTED"
                    return "ACCEPTED"
                return "REJECTED"
            return "REJECTED"
        return "REJECTED"

test_lst = [
    "101",    # Should match
    "111",    # Should not match
    "1001",   # Should not match
    "1011",   # Should match
    "10",     # Should not match
    "101111"  # Should match
]

for i in test_lst:
    print(accept_string(i))

# Output 
# ACCEPTED
# REJECTED
# REJECTED
# ACCEPTED
# REJECTED
# ACCEPTED
