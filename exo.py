def get30(T):
    l = len(T)
    for i in range(0, l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                res = T[i] * T[j] * T[k]
                if res == 30:
                    return (T[i],T[j],T[k])


                
def palindrome(word):
    return word[::-1] == word

def getMax(T):
    if T == []:
        return 
    currentMax = T[0]
    for i in T[1:]:
        if i > currentMax:
            currentMax = i
    return currentMax

def inverseInt(x):
    sign = 1
    if x < 0:
        sign = -1
    ret = int((str(abs(x)))[::-1]) * sign
    return ret

import string

def averageLen(p):
    p = p.translate(str.maketrans('', '', string.punctuation))
    splited = p.split()
    totalchar = 0
    for x in splited:
        totalchar += len(x)
    return round(totalchar/len(splited), 2)

def fibo(n):
    if n < 0:
        print("nique toi")
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def addString(first, second):
    return str(int(first) + int(second))

def dico(T, n):
    l = len(T)
    mid = l // 2
    if T[mid] == n:
        return mid
    if T[mid] > n:
        return dico(T[:mid], n)
    else:
        return mid + dico(T[mid:], n)

import collections

def firstUniqueChar(word):
    word = word.lower()
    count = collections.Counter(word)
    for i in range(len(word)):
        print(count[word[i]])
        if count[word[i]] == 1:
            return word[i]           