import time
start_time = time.time()

with open('wordlist.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

from itertools import permutations
perms = []
perms += [''.join(p) for p in permutations("asdfghjkl")]

def betterSet(a):
    length = len(a)
    b = []
    for i in range (0, length):
        if a[i] not in b:
            b.append(a[i])
    #print (b)
#print (perms)

betterSet(perms)

print("--- %s seconds ---" % (time.time() - start_time))
