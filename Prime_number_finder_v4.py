from math import *
import time

file1 = open("primes.txt","r")
data = file1.read()
file1.close()
short = data[1:-1]
spit = short.split(",")
primes = []

for y in range(len(spit)):
    primes.append(int(spit[y]))

c = primes[-1]
l = int((int(input("How many numbers you wanna check? ")))//2)
start = time.time()
        
for x in range(l):
    c += 2
    if c > 10000:
        print("Time to 10,000: " + str(time.time() - start) + "s")
        quit()
    s = sqrt(c)
    v = 0
    
    if c % s != 0:
        while primes[v] < s:
            if (c % (primes[v])) == 0:
                s  = primes[v+1]
            v += 1
            
        if primes[v] > s:
            print(c)
            primes.append(c)


file2 = open("primes.txt","w")        
file2.write(str(primes))
file2.close()
