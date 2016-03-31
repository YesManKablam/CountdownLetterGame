import time
start_time = time.time()

with open('newDic.txt', 'r') as fileopen:
    values = [line.strip() for line in fileopen]


# Setting up lists here use of generating your anagram
# They are wieghted as they are in the game
import random
anagram = []
vowels =['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]
consonant =['q','w','w','r','r','r','r','r','r','t','t','t','t','t','t','y','y','p','p','s','s','s','s','d','d','d','d','f','f','g','g','g','j','k','l','l','l','l','z','x','c','c','v','v','b','b','n','n','n','n','n','n','m','m',]

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


# After displaying the anagram, this alpabetises it, allow for some pretty fast searching
sanagram = (''.join(sorted(anagram)))

def solver(word):
    answers = []
    for item in values:
        if (''.join(sorted(item))) in word:
            print (item)
            break

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: solver(sanagram))
    print (t.timeit(number=1))
