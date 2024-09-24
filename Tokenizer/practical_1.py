import nltk
import re

input_program = input("Enter your code: ")
input_program_tokens = nltk.wordpunct_tokenize(input_program)
print(input_program_tokens)

re_keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
re_operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
re_numbers = "^(\d+)$"
re_special_characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
re_identifier  = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
re_Headers = "([a-zA-Z]+\.[h])"

for token in input_program_tokens:
    if(re.findall(re_keywords,token)):
        print(f"KEYWORD-{token}")
    elif(re.findall(re_operators,token)):
        print(f"OPERATOR-{token}")
    elif(re.findall(re_numbers,token)):
        print(f"NUMBER-{token}")
    elif(re.findall(re_special_characters, token)):
        print(f"SEPCIAL_CHAR-{token}")
    elif(re.findall(re_identifier, token)):
        print(f"IDETIFIER-{token}")
    elif(re.findall(re_Headers, token)):
        print(f"HEADER-{token}")
    else:
        print(f"UNKNOWN VALUE-{token}")

# output: 
# Enter your code: Sum=3 + 2;
# ['Sum', '=', '3', '+', '2', ';']
# IDETIFIER-Sum
# OPERATOR-=
# NUMBER-3
# OPERATOR-+
# NUMBER-2
