#Loop optimization 

import time
t1 = time.time()
time.sleep(.1)
for i in range(1, 100+1):
    print(i, end=" ")
t2 = time.time()
print()
print(f"Process time: {t2 - t1:6f}")
time.sleep(.1)
for i in range(1, 100+1):
    print(i, end=" ")
    print(i+1, end=" ")
    print(i+2, end=" ")
    print(i+3, end=" ")
    print(i+4, end=" ")
t3 = time.time()
print()
print(f"Process time: {t3 - t2:6f}") # :6f for six digit after the decimal point so result will be like 4894778.447759


