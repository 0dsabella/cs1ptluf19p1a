import random

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
        
    #So far I have got the list to become randomized and stored into a new list.
    #I am trying to find a way to get the entire code to repeat to keep adding new combinations to newList.      
    for i in range(n):
      newList = []
      random.shuffle(list)
      newList.append(list)

    return newList

#Max # of vowels is 6
print(charList(4))
