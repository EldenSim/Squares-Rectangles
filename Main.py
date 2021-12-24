import numpy as np
from numpy import *
import random
global sbs
def gridsize():
    global gridsizeinputted
    gridsizeinputted = 0
    while True:
        size = input("Enter prefered grid size (E.g enter ""16"" for a gridsize of 16x16): ")
        if (size.isdigit() == False) or int(size) < 0:
            print("Invalid input, please input a positive interger only.")
        else:
            break
    gridsizeinputted = int(size)
def square():
    global squarelimit
    global squarelist
    global numSquares
    squarelist = []
    numSquares = 0
    while True:
        numSquares = input("Enter number of squares to be created: ")
        if (numSquares.isdigit() == False)  or int(numSquares) < 0:
            print("Invalid input, try again.")
        else:
            numSquares = int(numSquares)
            break
    for i in range(numSquares):
        rand = random.randint(1, gridsizeinputted)
        squarelimit = gridsizeinputted - rand
        oneslists = np.array([1])
        lists = np.repeat(oneslists, rand * rand)
        square = lists.reshape(rand, rand)
        squarelist.append(square)
        print(square.shape)
def rectangle():
    global x_rectanglelimit
    global y_rectanglelimit
    global rectanglelist
    global numofrandlines
    rectanglelist = []
    numofrandlines = 0
    while True:
        numofrandlines = input("Enter number of rectangle to be created: ")
        if (numofrandlines.isdigit() == False) or int(numofrandlines) < 0:
            print("Invalid input, try again")
        else:
            numofrandlines = int(numofrandlines)
            break
    for i in range(numofrandlines):
        while True:
            rand = random.randint(1, gridsizeinputted)
            rand2 = random.randint(1, gridsizeinputted)
            if rand != rand2:
                break
        x_rectanglelimit = gridsizeinputted - rand
        y_rectanglelimit = gridsizeinputted - rand2
        oneslists = np.array([1])
        lists = np.repeat(oneslists, rand * rand2)
        rectangle = lists.reshape(rand, rand2)
        rectanglelist.append(rectangle)
        print(rectangle.shape)
def squareplacer():
    global sbssquarelist
    sbssquarelist = []
    for i in range(0, len(squarelist)):
        lists = np.array([0])
        gridsetup = np.repeat(lists, gridsizeinputted * gridsizeinputted)
        sbs = gridsetup.reshape(gridsizeinputted, gridsizeinputted)
        sizeinterim = squarelist[i].shape
        size = sizeinterim[0]
        limitedby = size
        possibleposition = gridsizeinputted - size
        if possibleposition == 0:
            sbsfull = np.repeat(np.array([1]), gridsizeinputted * gridsizeinputted)
            sbsfullfinal = sbsfull.reshape(gridsizeinputted, gridsizeinputted)
            sbssquarelist.append(sbsfullfinal)
        else:
            x_randposnum = random.randint(1, possibleposition)
            newXvalue = x_randposnum
            y_randposnum = random.randint(1, possibleposition)
            newYvalue = y_randposnum
            randaxis = random.randint(1, 2)
            for i in range(0, limitedby):
                if randaxis == 1:
                    start = sbs[x_randposnum][y_randposnum]
                    for y in range(0, limitedby):
                        sbs[newXvalue, y_randposnum + i] = 1
                        newYvalue = y_randposnum + i
                        sbs[x_randposnum + y, newYvalue] = 1
                        newXvalue = x_randposnum + y
                else:
                    for i in range(0, limitedby):
                        start = sbs[y_randposnum][x_randposnum]
                        for y in range(0, limitedby):
                            sbs[newYvalue, x_randposnum + i] = 1
                            newXvalue = x_randposnum + i
                            sbs[y_randposnum + y, newXvalue] = 1
                            newYvalue = y_randposnum + y
            sbssquarelist.append(sbs)
def rectplacer():
    global sbsrectlist
    sbsrectlist = []
    for i in range(0, len(rectanglelist)):
        lists = np.array([0])
        gridsetup = np.repeat(lists, gridsizeinputted * gridsizeinputted)
        sbs = gridsetup.reshape(gridsizeinputted, gridsizeinputted)
        randaxis = random.randint(1, 2)
        sizeinterim = rectanglelist[i].shape
        if randaxis == 1:
            ysize = sizeinterim[0]
            xsize = sizeinterim[1]
        else:
            ysize = sizeinterim[1]
            xsize = sizeinterim[0]
        ylimitedby, xlimitedby = ysize, xsize
        ypossibleposition = gridsizeinputted - ysize
        xpossibleposition = gridsizeinputted - xsize
        if ypossibleposition == 0:
            y_randposnum = 0
            x_randposnum = random.randint(1, xpossibleposition)
        elif xpossibleposition == 0:
            x_randposnum = 0
            y_randposnum = random.randint(1, ypossibleposition)
        else:
            y_randposnum = random.randint(1, ypossibleposition)
            x_randposnum = random.randint(1, xpossibleposition)
        newXvalue = x_randposnum
        newYvalue = y_randposnum
        for i in range(0, ylimitedby):
            for y in range(0, xlimitedby):
                start = sbs[newXvalue][y_randposnum]
                sbs[x_randposnum + y, y_randposnum] = 1
            y_randposnum += 1
            newXvalue = x_randposnum
        sbsrectlist.append(sbs)
def final():
    global compliedlist
    gridsize()
    square()
    squareplacer()
    rectangle()
    rectplacer()
    compliedlist = []
    selectedlist =[]
    counter = 0
    for i in range(0, len(sbsrectlist) + len(sbssquarelist)):
        positiondecider = 0
        decider = random.randint(1, 2)
        if len(sbsrectlist) == 0:
            decider = 0
        if len(sbssquarelist) == 0:
            decider = 1
        if decider == 1:
            counter += 1
            selectedlist = sbsrectlist
            if len(compliedlist) != 0:
                positiondecider = random.randint(0, len(selectedlist) - 1)
                compliedlist.append(selectedlist[positiondecider])
                del selectedlist[positiondecider]
            else:
                compliedlist.append(selectedlist[0])
                del selectedlist[0]
        else:
            selectedlist = sbssquarelist
            if len(compliedlist) != 0:
                positiondecider = random.randint(0, len(selectedlist) - 1)
                compliedlist.append(selectedlist[positiondecider])
                del selectedlist[positiondecider]
            else:
                compliedlist.append(selectedlist[0])
                del selectedlist[0]
    print("Final data set \n")
    print(compliedlist)
final()
save('Complied data.npy', compliedlist)

    



