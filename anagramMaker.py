import time
start_time = time.time()

import random
anagram = []
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

# Loops here will append the required vowels and consonants to the anagram
# It then fills the remaining space with either consonants or vowels
for i in range (0,3):
    anagram.append(random.choice(vowels))
for i in range (0,4):
    anagram.append(random.choice(consonant))
for i in range (0,2):
    anagram.append(random.choice(vowels + consonant))

# Imports the shuffle function and jumbles the anagram so that it doesn't really look like it follows a format
from random import shuffle
shuffle(anagram)
print (''.join(anagram))

# Some static anagrams here for test purposes
#anagram = ['a','b','c','d']
anagram = ['z','a','u','c','t','i','o','n','e','d']
#anagram = ['t','e','s','t']
#from itertools import permutations
#perms = [''.join(p) for p in permutations(anagram)]
#print ('\n'.join(perms))

# Brute force approaches here, involving swapping positions in the anagram
# Prints the anagram, removing things like commas
#print (''.join(anagram))
#perms = []
#for i in range (0,9):
#    a = anagram[0]
#    b = anagram[i]
#    c = a
#    a = b
#    b = c
    #c = (''.join(anagram[2:9]))
    #perms = (a + b + c)
    #print (perms)
#print (a + b)

#k = 0

#print ('\n\n')

# A better attempt at the swapping I made, but it stil didn't work out.
#for i in range (0,len(anagram)):
#    j += 1
#    for i in range (j,len(anagram)):
        #print (i)
        #print (anagram[j] + anagram[i])
#        anagram[j] anagram[i] = anagram[i], anagram[j]
#        print (''.join(anagram))

# I did a little digging after the last attempt, and found this.
# It's pretty much the same as mine, but the items are swapped back before the it loops
# The lack of a swap back was the issue with mine
#http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
#def perm(a,k=0):
#  if(k==len(anagram)):
#      return (a)
#  else:
#      for i in range(k,len(anagram)):
#         a[k],a[i] = a[i],a[k]
#         perm(a, k+1)
#         a[k],a[i] = a[i],a[k]

#perm(anagram)

# Another brute force approach that I found.
# It works, but I wasn't all that fond of it
# http://stackoverflow.com/questions/6284396/permutations-with-unique-values
#def unique_permutations(elements):
#    if len(elements) == 1:
#        yield (elements[0],)
#    else:
#        unique_elements = elements
#        for first_element in unique_elements:
#            remaining_elements = list(elements)
#            remaining_elements.remove(first_element)
#            for sub_permutation in unique_permutations(remaining_elements):
#                yield (first_element,) + sub_permutation

#a = list(unique_permutations(anagram))
#print(len(a))


# Write up I saw on alpabetising the items you work with so there is no need to brute force the anagram finder
# Is fast for exact matching.
# However, if there is no exact match, removing parts of the anagram is a huge hit on running time.
# I was barking up the wrong tree with this approach, but the idea of alphabetising stuck with me.
# http://andrew.io/weblog/2010/03/finding-anagrams-with-python/
def anagrams(word):
    words = [w.rstrip() for w in open('newdic.txt')]
    sword = sorted(word)
    a = [w for w in words if sorted(w) == sword]
    i = 0
    while not a:
        sword = sorted(word)
        temp = sword[i]
        del sword[i]
        i += -1
        a = [w for w in words if sorted(w) == sword]
    return (a)

print (anagrams(anagram))





print("--- %s seconds ---" % (time.time() - start_time))
