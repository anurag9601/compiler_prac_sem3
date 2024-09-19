#Loop optimization 

import time

t1  = time.time()
for i in range(1,100+1):
    print(i,end=" ")
t2 = time.time()
print(f"Total execution taken by first function is {t2-t1}")
for i in range(1,100+1):
    print(i,end=" ")
    print(i+1,end=" ")
    print(i+2,end=" ")
    print(i+3,end=" ")
    print(i+4,end=" ")
t3 = time.time()
print(f"Total execution taken by second function is {t3-t2}")
