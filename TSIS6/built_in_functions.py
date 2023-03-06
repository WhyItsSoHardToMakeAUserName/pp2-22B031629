import math
import time

# 1
num_list=[1,3,4,5]

print(math.prod(num_list))

# 2
text="HelloolleH"
upper=0
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in text:
    if i in up:
        upper+=1
print(upper)

# 3
def list_to_string(txt):
    list=[]
    string=""
    list.extend(txt)
    list.reverse()
    for i in list:
        string+=i
    return(bool(txt==string))

print(list_to_string(text))

#4
def timed_sqrt(sec,num):
    time.sleep(sec)
    return ("Square root of " +str(num)+ " after " +str(sec) +" miliseconds is "+str(math.sqrt(num)))

print(timed_sqrt(1,25))

#5
tup=(True,True,True)
print(all(tup))