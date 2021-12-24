import numpy as np
from numpy import *
import csv

contents = load('Complied data.npy')
compliedlist = contents
def mlwithoutdatasplit():
    with open("data.csv", "w", newline = "") as file:
        w = csv.writer(file)
        w.writerow(["AreaOfShaped", "Squared", "Square/Rectangle"])
        for i in range(len(compliedlist)):
            readingdata(i)
            
            w.writerow([numofones, squared, shape])


def readingdata(x):
    global shape
    global numofones
    global numofzeros
    global gridarea
    global squared
    data = compliedlist[x]
    shape = ''
    numofones = 0
    numofzeros = 0
    gridarea = len(data[0]) ** 2
    print(gridarea)
    L = 0
    B = 0
    length = 0
    x = 0
    '''
    for i in data:

        for y in range(0, len(i)):
            if i[x][y] == 1:
                length += 1
            for x in range(len(i)):
                if i[y][x] == 1:
                    breath += 1

    print(length, "Length")
    print(breath, "Breath")
    '''   
    for i in data:
        for y in i:
            if y == 0:
                numofzeros += 1
    numofones = gridarea - numofzeros
    squared = numofones ** 0.5
    check = squared // 1
    print(check ** 2)
    print(squared)
    if int(check ** 2) == int(numofones):
        shape = "Square"
    else:
        shape = "Rectangle"
    

    










    
def mlwithdatasplit():
    splitdata()
    print(setsofdata)
def splitdata():
    while True:
        global setsofdata
        setsofdata = 0
        inp = input("Enter the total number of data sets needed: ")
        if inp.isdigit() == False or int(inp) < 2:
            print("Invalid input. Please input only a positive integer.")
        else:
            setsofdata = int(inp)
            break
        



def final():
    while True:
        inp = input("Do you want to split data files(Yes/No): ")
        if inp.isdigit():
            print("Invalid input, plese input only yes or no.")
        else:
            inp = inp.lower()
            if inp == "yes":
                mlwithdatasplit()
                break
            elif inp == "no":
                mlwithoutdatasplit()
                break
            else:
                print("Invalid input. Please input only yes or no.")


mlwithoutdatasplit()

