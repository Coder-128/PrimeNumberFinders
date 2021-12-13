from math import *

file1 = open("primes.txt","r")
data = file1.read()
file1.close()
short = data[1:-1]
spit = short.split(",")
primes = []

for y in range(len(spit)):
    primes.append(int(spit[y]))

c = primes[-1]
z = c
l = int((int(input("How many numbers you wanna check? ")))//2)

for x in range(l):
    c += 2
    s = sqrt(c)
    v = 0
    
    if c % s != 0:
        while primes[v] < s:
            if (c % (primes[v])) == 0:
                s  = primes[v+1]
            v += 1
            
        if primes[v] > s:
            primes.append(c)
            if primes[v] > z:
                print(primes[v])
                z += 1000000


file2 = open("primes.txt","w")        
file2.write(str(primes))
file2.close()
print(primes[-1])
