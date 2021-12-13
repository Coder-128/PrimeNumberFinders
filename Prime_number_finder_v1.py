import time
start = time.time()

c = 0
while True:
    c += 1
    if c > 10000:
        print("Time to 10,000: " + str(time.time() - start) + "s")
        quit()
    prime = True
    for x in range (c-2):
        if (c % (x+2)) == 0:
            prime = False
    if prime == True:
        print(c)
