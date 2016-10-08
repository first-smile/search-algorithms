'''
Created on Oct 8, 2016

Desc : Sequential Search 

@author: Ajay
'''
from numpy import random, math

dataArray=range(3,100,3)
key = math.ceil(random.random()*10)

def searchInArray(key,dataArray):
    for i in dataArray:
        if i==key :
            return True
    return False


print()

if __name__ == '__main__':
    print("Search Space ",dataArray)
    print("key",key)
    print("found key = ",searchInArray(key,dataArray))
    print("found key = ",searchInArray(3,dataArray))
    print("found key = ",searchInArray(4,dataArray))
    pass