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
import re

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

def perfectSquare(lower, upper):
    ret = []
    for i in range(0, upper):
        if i*i >= lower and i*i <= upper:
            ret.append(i*i)
    return ret

def CamelToSnake(word):
    return re.sub('([A-Z]+)', r'_\1',word).lower()

def fizzBuzz(n):
    arr = []
    for i in range(0, n):
        if (i%3 == 0 and i%5 == 0):
            arr.append('fizzbuzz')
        elif(i%3 == 0):
            arr.append('fizz')
        elif(i%5 == 0):
            arr.append("buzz")
        else:
            arr.append('')
    return arr

def reverseString(word):
    return word[::-1]

def mono(arr):
    croissant= True
    decroissant = True
    for i in range(len(arr)-1):
        if (arr[i] <= arr[i+1]):
            decroissant = False
        if (arr[i] >= arr[i+1]):
            croissant = False
    return croissant or decroissant

def growing_path(A,B):
    A.sort()
    B.sort()
    seta = set(A) 
    setb = set(B)
    setAB = setb - seta
    return A+list(setAB) 

def completeTrou(A):
    res = []
    valid = 0
    for i in A:
        if i is None:
           res.append(valid)
        else:
            res.append(i)
            valid = i
    return res

def even_odd_sort(list):
    even = []
    odd = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort(reverse=True)
    return even + odd

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+ 1] = arr[j+1], arr[j]
    return arr

def listPremier(val):
    prime = []
    for num in range(val):
        if num > 1 :
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime.append(num)
    return prime


def premier(val):
    prime = []

    for num in range(val):
        if num > 1:
            isPrime = True
            for j in range(2, num):
                if num % j == 0:
                    isPrime = False
            if isPrime:
                prime.append(num)
    return prime
            
def checkifPremier(val):
    if val < 1:
        return False
    if val == 1:
        return True
    for i in range(2, val // 2):
        if val % i == 0:
            return False
    return True

print(checkifPremier())
