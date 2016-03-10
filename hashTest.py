import time
start_time = time.time()

with open('newDic.txt', 'r') as fileopen:
    values = [line.strip() for line in fileopen]

# Setting up lists here use of generating your anagram
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

# After displaying the anagram, this alpabetises it, allow for some pretty fast searching
sanagram = (''.join(sorted(anagram)))

# All of this here is from me testing using a dict.
################################################################################################################
################################################################################################################

#keys = []
#for items in values:
#    keys += [(''.join(sorted(items)))]
#   keys = sorted(values[a])
#   print (keys)
#print (keys)
#anagram = ['a','u','c','t','i','o','n','e','d']
#dictionary = dict(zip(keys, values))

#print (dictionary.get("a"))
#print (keys)
#print (values [1])
#print (dictionary.get(sanagram))

#list_values = [keys for values, values in dictionary.items() if "estt" in keys]
#print(list_values)

#If key in sanagram
#i = 0
#for item in dictionary:
#    if dictionary.keys() in sanagram:
#        print (key)

#print (list(dictionary.items()))


################################################################################################################
################################################################################################################

# And this is the list method I found a whole lot easier

# This loops through the list of imported words from the dictionary file
# It then checks if the alphabetised word in the list is in the alphabetised anagram
# Then it returns the results
for item in values:
    if (''.join(sorted(item))) in sanagram:
        print (item)

print("--- %s seconds ---" % (time.time() - start_time))
