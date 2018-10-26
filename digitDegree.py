def digitDegree(n):
    ### set counter for while loop to 0
    t = 0
    
    ###change n to a string, so length can be calculated
    strN = str(n)

    ### while the length of the number is more than one character:
    ### change to int, sum all characters, change back into string
    while len(strN) > 1:
        listN = list(strN)
        listInts = [int(i) for i in listN]
        newInt = sum(listInts)
        strN = str(newInt)
        t += 1
    ### return how many loops had to be done to reduce n's length to 1
    return int(t)
