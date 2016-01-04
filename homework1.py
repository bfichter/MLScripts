import random

ni = 0

def getRand():
    return random.random() * 2 - 1 #to get it in the domain space


def getRandPoint():
    point = [getRand(), getRand()]
    return point


def checkPoint(pointA, pointB, C):
    result = (pointB[0] - pointA[0]) * (C[1] - pointA[1]) - (pointB[1] - pointA[1]) * (C[0] - pointA[0])

    return sign(result)





def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    return 0










N = 100
w = [0, 0, 0]

pointA = getRandPoint()
pointB = getRandPoint()

xN = [None] * N
yN = [None] * N

for s in range(N):
    currPoint = getRandPoint()
    xN[s] = currPoint
    yN[s] = checkPoint(pointA, pointB, currPoint)


def main():
    
    #ok now input and output is populated
    #time to run Perceptron
    perceptron()
    print ni
    
 

def perceptron():
    #print "in perceptron"
    global ni
    hack = ni
    ni = hack + 1
    for i in range(N):
        
        currXN = xN[i]
        currYN = yN[i]
        wavyN = w[0] * 1 + w[1] * currXN[0] + w[2] * currXN[1]
        if sign(wavyN) != currYN:
	    #perceptron has fucked up
            #adjust the w and restart
            w[0] += currYN * 1
            w[1] += currYN * currXN[0]
            w[2] += currYN * currXN[1]
            perceptron()
            break           

    









main()
