from math import *
import time

print("2\n3")
primes = [3]
c = 3
l = int(input("How many numbers you wanna check? "))
start = time.time()

for x in range(l):
    c += 2
    if c > 10000:
        print("Time to 10,000: " + str(time.time() - start) + "s")
        quit()
    prime = True
    s = sqrt(c)
    v = 0
    
    if c % s == 0:
         s  = primes[v+1]

    while primes[v] < s:
        if (c % (primes[v])) == 0:
            s  = primes[v+1]
        v += 1
        
    if primes[v] > s:
        print(c)
        primes.append(c)


file = open("primes.txt","w")        
file.write(str(primes))
file.close()
