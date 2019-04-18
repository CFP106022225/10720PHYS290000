fp = open('Alice.txt','r')

#read the first line from the file
line = fp.readline()
print(line)
print(type(line))

line = fp.readline()
print(line)

line = fp.readline()
print(line)

s = line.split()
print(s)
print(type(s))

#close the file 
fp.close()
fp = open('Alice.txt','r',encoding='UTF-8')

line = fp.readline()

while line:
        
     line = fp.readline()
     
fp.close()
import math
import matplotlib.pyplot as plt 
import numpy as np

fp = open('Alice.txt','r',encoding='UTF-8')
line = fp.readline()
my_dict = {}

while line:
    s = line.split()
    for x in s:
        if x not in my_dict:
             my_dict[x] = 1
        else:
             my_dict[x] += 1
    line = fp.readline()
    
fp.close()

num = []

for key in my_dict:
    num.append(my_dict[key])

print(len(num))
num.sort()
num.reverse()

plt.loglog(range(len(num)),num)
plt.xlabel('Rank of the word')
plt.ylabel('Number of the occurance')
plt.show()
lognum=np.log(num)
b=plt.hist(lognum,bins=40)


dx=(b[1][1]-b[1][0])
bin_center=np.array(b[1][0:-1])+dx/2


from scipy import optimize

def test_func(x,amp,alpha):
    return amp*x**alpha

params, params_covariance = optimize.curve_fit(test_func, bin_center,b[0])
print(params[0],params[1])
plt.show()

plt.plot(bin_center, test_func(bin_center, params[0],params[1]), "r*", label="fitted function")

plt.xlabel("Rank of the world")
plt.ylabel("Number of the occurance")
plt.show()