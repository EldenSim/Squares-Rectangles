import numpy as np
import random
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
    print(sbsrectlist)
gridsize()
rectangle()
rectplacer()
print(len(sbsrectlist))
