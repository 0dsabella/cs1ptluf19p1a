import random

def charList(n):
    count = 9
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    list = []

    for i in range(n):
        count = count - 1
        list.append(random.choice(vowels))

    for i in range(count):
        list.append(random.choice(letters))

    return list

print(charList(2))
