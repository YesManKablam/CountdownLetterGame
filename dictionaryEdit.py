with open('wordlist.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

# Sorts the word list by length
sortedwords = sorted(words, key=len)

# Reverses the list, so that 9 letter characters are at the top
invertedDic = reversed(sortedwords)
f = open("newDic.txt","w")

# Writes each word to the new text file, as long as they are less than 10 characters long
for item in invertedDic:
    if len(item) < 10:
        f.write("%s\n" % item)


# All of this is is done because when using the brute force approach,
# Word placement in the list mattered a whole lot

# Create the alpahbitized words list for the dict
# This should make the dict even faster


#Also, fuzzy matching isn't going to work out
