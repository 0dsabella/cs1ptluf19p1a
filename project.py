import random, math, itertools

def charList(n):

    count = 9
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    list = []

    #Append the vowels first
    for i in range(n):
        count = count - 1
        tempVowel = (random.choice(vowels))
        list.append(tempVowel)

    #Use remaining # of counts to append a # of consonants
    for i in range(count):
        tempVowel = (random.choice(consonants))
        list.append(tempVowel)

    return list
#Max # of vowels is 6
#print(charList(4))

#Formula found in https://www.calculatorsoup.com/calculators/discretemathematics/permutations.php
def numPermutations(objects, sample):
    return math.factorial(objects) / math.factorial(objects - sample)

def sumPermutations(objects, num):
    sample = 1
    outputNum = 0
    for i in (range(num)):
        outputNum = outputNum + numPermutations(objects, sample)
        sample = sample + 1
    return outputNum

#Referenced https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
def listToString(inputList):
    output = ""
    return output.join(inputList)

def permutationsTest(input):
    output = itertools.permutations(input)
    return output
#Found itertool usage in https://kite.com/python/examples/4675/itertools-iterate-over-all-permutations-of-a-list-of-strings
#Documentation for itertools https://docs.python.org/3/library/itertools.html
def wordCombos(inputList):
    print(inputList)

    count = 0

    trackerList = []
    outputList = []

    #Var count as tracker. Outputs permutations of characters in "trackerList",
    #coverts to string, then appends to the "outputList"
    while count < 9:
        trackerList.append(inputList[count])
        for i in itertools.permutations(trackerList):
            outputList.append(listToString(i))
        count = count + 1
    return outputList
print(wordCombos(charList(3)))

#Found how to use "pass" in https://stackoverflow.com/questions/19632728/how-do-i-get-a-python-program-to-do-nothing/19632742
def checkWord(inputList):
    outputList = ""
    for i in inputList:
        pass
        #If "i" isn't a word, pass
        #If "i" is a word, outputList.append(i)
    outputList.sort()
    return outputList
