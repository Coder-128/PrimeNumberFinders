import time
start = time.time()
print("2")
c = 1
primes = []
while True:
    c += 2
    if c > 10000:
        print("Time to 10,000: " + str(time.time() - start) + "s")
        quit()
    prime = True
    for x in range (len(primes)):
        if prime == True:
            if (c % (primes[x])) == 0:
                prime = False
    if prime == True:
        print(c)
        primes.append(c)
        
