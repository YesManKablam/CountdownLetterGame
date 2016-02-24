# G00301273
# John Conor Kenny
# Countdown Letter Game

# Imports a timer function to see how long it takes to run the program
import time
start_time = time.time()

# Opens the wordlist and asigns it to a list
with open('wordlist.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

# Imports the random function and sets up lists for the final anagram, the vowels and the consonants
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

# Prints the anagram, removing things like commas
print (''.join(anagram))

# Imports the permuation function from itertools and sets up our counter and list for the total permutations
from itertools import permutations
j = 1
perms = []

# This looops 9 times, since the anagram will always be 9 characters long
# The permutations function finds every combo of words characters that you give it
# You can specify how many charaters you actually want to use, for example if you did:
# perms += [''.join(p) for p in permutations("test", 2)]
# You will get "te, et" as your output
# So, we feed it our generated anagram, then will start at 1 and increase every time it loops intil it get's to 9
# This will give you every possible combination of charcters in the word we give it, since the word will always be 9 characters long
for i in range (0,9):
    perms += [''.join(p) for p in permutations(anagram, j)]
    j += 1

# Here, results will be given only the words that are both in the perms list and in the word list
# They are converted to sets, which only display the unique items in a list.
results = (set(words) & set(perms))

# This line here will allow you to order the output by the length of the words
sortedwords = sorted(results, key=len)

# This prints out all of the overlap between the lists, and it also prints out the longest word in that list
print (results)
print (sortedwords[-1])

# Displays running time of the project
print("--- %s seconds ---" % (time.time() - start_time))
