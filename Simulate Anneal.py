import math
import random

# each time the tempreture decrease T *
decreaseRate = 0.9999
# when the tempreture lower than the lowest tempreture it will stop
lowestT = 0.0000001
# this is the intial tempreture
T = 10000

# this function is used for generate a random number
# the shake shakeRange use for make sure every time a random number in a certain and reasonable range
def getRandomNum(num, shakeRange):
    highest = num + shakeRange
    lowest = num - shakeRange

    if highest > 1:
        highest = 1
    elif lowest < -1:
        lowest = -1

    result = random.uniform(lowest, highest)
    return result


# this is 2a f(u) function 
def qu2a(u):
    result = u * (math.sin(1 / (0.01 + u ** 2))) + (u ** 3) * math.sin(1 / (0.001 + u ** 4))
    return result


# this method use for get the value of dE
def getdE(newState, currentState):
    result = newState - currentState
    return result


# this the mian function of 2a
def SAStart2a(valueU):
    currentState = valueU
    t = T
    iterTime = 0
    print("----------------------------------------------Initial---------------------------------------------------")
    print("the tempreture: %f \t the value of u: %f \t the value of function f(u): %f \t" % (t, currentState, qu2a(currentState)))
    print("--------------------------------------------------------------------------------------------------------")
    while t > lowestT:
        iterTime += 1
        newState = getRandomNum(currentState, 0.2)
        dE = getdE(qu2a(newState), qu2a(currentState))
        if (dE) >= 0:
            currentState = newState
        else:
            e = math.exp(dE / t)
            if e >= random.uniform(0, 1):
                currentState = newState
        t *= decreaseRate
        print("iter time: %d \t the tempreture: %f \t the value of u: %f \t the value of function f(u): %f" % (iterTime, t, currentState, qu2a(currentState)))

    print("when iter time : %d u = %f , the function u has max value = %f" % (iterTime, currentState, qu2a(currentState)))
    print("Initial value: u=%f" % (valueU))

# start with 0
#SAStart2a(0)

# start with random value
#SAStart2a(random.uniform(-1, 1))

# start with a specified value
#SAStart2a(0.5)

# this is fuction of f(u,v)
def qu2b(u, v):
    result = 0
    result = u * v ** 2 * (math.sin(v / (0.01 + u ** 2))) + (u ** 3) * (v ** 2) * math.sin((v ** 3) / (0.001 + u ** 4))
    return result

# main function of 2b
def SAStart2b(u, v):
    currentU, currentV = u, v
    currentFunctionValue2B = qu2b(currentU, currentV)
    iterTime = 0
    t = T
    print("----------------------------------------------Initial---------------------------------------------------")
    print("t: %f \t u: %f \t v: %f \t func: %f" % (t, currentU, currentV, currentFunctionValue2B))
    print("--------------------------------------------------------------------------------------------------------")
    while t > lowestT:
        iterTime += 1
        newU, newV = getRandomNum(currentU, 0.5), getRandomNum(currentV, 0.5)
        dE = getdE(qu2b(newU, newV), qu2b(currentU, currentV))
        if (dE) >= 0:
            currentU, currentV = newU, newV
        else:
            e = math.exp(dE / t)
            if e >= random.uniform(0, 1):
                currentU, currentV = newU, newV
        t *= decreaseRate
        print("iter time: %d \t t: %f \t u: %f \t v: %f \t func: %f" % (iterTime, t, currentU, currentV, qu2b(currentU, currentV)))
    print("when u = %f , v = %f the function u has max value = %f" % (currentU, currentV, qu2b(currentU, currentV)))
    print("Initial value: u=%f v=%f" % (u,v))

# start with 0
#SAStart2b(0,0)

# start with random value
#SAStart2b(random.uniform(-1, 1),random.uniform(-1, 1))

# start with a specified value
#SAStart2b(0.5,-0.5)

def qu2c(u, v, w):
    partA = (u * (v ** 2) + math.sin(math.pi * w)) * (math.sin(v / (0.01 + u ** 2))) * math.sin(math.pi * w / 2)
    partB = (u ** 3) * (v ** 2) * w * math.sin(
        (v ** 3) / (0.001 * (math.sin(math.pi * w / 2) + (u ** 4) + (w - 1) ** 2) ** 2))
    result = partA + partB
    return result


def SAStart2c(u, v, w):
    currentU, currentV, currentW = u, v, w
    currentFunctionValue2C = qu2c(currentU, currentV, currentW)
    t = T
    iterTime = 0
    print("----------------------------------------------Initial---------------------------------------------------")
    print("t: %f \t u: %f \t v: %f \t w: %f \t func: %f" % (t, currentU, currentV, currentW, currentFunctionValue2C))
    print("--------------------------------------------------------------------------------------------------------")
    while t > lowestT:
        iterTime += 1
        newU, newV, newW = getRandomNum(currentU, 0.2), getRandomNum(currentV, 0.2), getRandomNum(currentW, 0.2)
        dE = getdE(qu2c(newU, newV, newW), qu2c(currentU, currentV, currentW))
        if (dE) >= 0:
            currentU, currentV, currentW = newU, newV, newW
        else:
            e = math.exp(dE / t)
            if e >= random.uniform(0, 1):
                currentU, currentV, currentW = newU, newV, newW
        t *= decreaseRate
        print("iter time : %d \t t: %f \t u: %f \t v: %f \t w: %f \t func: %f" % (iterTime, t, currentU, currentV, currentW, qu2c(currentU, currentV, currentW)))
    print("when iter time : %d  u = %f , v = %f , w = %f the function u has max value = %f" % (iterTime, currentU, currentV, currentW, qu2c(currentU, currentV, currentW)))
    print("Initial value: u=%f v=%f w=%f " % (u,v,w))

# start with 0
#SAStart2c(0,0,0)

# start with random value
#SAStart2c(random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1))

# start with a specified value
#SAStart2c(0.5,-0.5,0.5)

def qu2d(u, v, w, y):
    result = y * qu2c(u, v, w)
    return result

def SAStart2d(u, v, w, y):
    currentU, currentV, currentW, currentY = u, v, w, y
    currentFunctionValue2d = qu2d(currentU, currentV, currentW, currentY)
    t = T
    iterTime = 0
    print("----------------------------------------------Initial---------------------------------------------------")
    print("t: %f \t u: %f \t v: %f \t w: %f \t y: %f \t func: %f" % (t, currentU, currentV, currentW, currentY, currentFunctionValue2d))
    print("--------------------------------------------------------------------------------------------------------")
    while t > lowestT:
        iterTime += 1
        newU, newV, newW = getRandomNum(currentU, 0.2), getRandomNum(currentV, 0.2), getRandomNum(currentW, 0.2)
        # to find max function value there is no need to generate a random value for y,
        # because if qu2c(u,v,z) > 0
        # we just let y = 1
        # if qu2c(u,v,z) < 0
        # we just let y = -1
        # this is more efficient
        if qu2c(newU, newV, newW) > 0:
            newY = 1
        else:
            newY = -1
        currentY = newY
        dE = getdE(qu2d(newU, newV, newW, newY), qu2d(currentU, currentV, currentW, currentY))
        if (dE) >= 0:
            currentU, currentV, currentW = newU, newV, newW
        else:
            e = math.exp(dE / t)
            if e >= random.uniform(0, 1):
                currentU, currentV, currentW = newU, newV, newW
        t *= decreaseRate
        print("iter time: %d \t t: %f \t u: %f \t v: %f \t w: %f \t y: %f \t func: %f" % (iterTime, t, currentU, currentV, currentW, currentY, qu2d(currentU, currentV, currentW, currentY)))
    print("when iter time: %d, u = %f , v = %f , w = %f, y = %f the function u has max value = %f" % (iterTime, currentU, currentV, currentW, currentY, qu2d(currentU, currentV, currentW, currentY)))
    print("Initial value: u=%f v=%f w=%f y=%f" % (u,v,w,y))

# start with 0
#SAStart2d(0,0,0,0)

# start with random value
#SAStart2d(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1))

# start with specified value
#SAStart2d(-0.5, 0.5, -0.5, -0.1)

# simple user interface
def startWholeProcess():
    while True:
        a = input("this is process A \n type 1 start with f(0) \n type 2 start with a random value \n type 3 start with a user-specified value \n type 4 Eixt \n :")
        a = int(a)
        if a == 4:
            break
        elif a == 1:
            SAStart2a(0)
        elif a == 2:
            SAStart2a(random.uniform(-1,1))
        elif a == 3:
            u = input("please in put a number for value U between -1 and 1:")
            u = float(u)
            if u <= 1 and u >= -1:
                SAStart2a(u)
            else:
                print("invaild input, please input again")
        else:
            print("invaild input, please input again")

    while True:
        a = input("this is process B \n type 1 start with f(0,0) \n type 2 start with a random value \n type 3 start with a user-specified value \n type 4 Eixt \n :")
        a = int(a)
        if a == 4:
            break
        elif a == 1:
            SAStart2b(0,0)
        elif a == 2:
            SAStart2b(random.uniform(-1,1),random.uniform(-1,1))
        elif a == 3:
                u = input("please in put a number for value U between -1 and 1:")
                u = float(u)
                v = input("please in put a number for value V between -1 and 1:")
                v = float(v)
                if (u <= 1 and u >= -1) and (v >= -1 and v <= 1):
                    SAStart2b(u,v)
                else:
                    print("invaild input, please input again")
        else:
            print("invaild input, please input again")

    while True:
        a = input("this is process C \n type 1 start with f(0,0,0) \n type 2 start with a random value \n type 3 start with a user-specified value \n type 4 Eixt \n :")
        a = int(a)
        if a == 4:
            break
        elif a == 1:
            SAStart2c(0, 0, 0)
        elif a == 2:
            SAStart2c(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1,1))
        elif a == 3:
                u = input("please in put a number for value U between -1 and 1:")
                u = float(u)

                v = input("please in put a number for value V between -1 and 1:")
                v = float(v)

                w = input("please in put a number for value W between -1 and 1:")
                w = float(w)

                if ((u <= 1 and u >= -1) and (v >= -1 and v <= 1)) and (w >= -1 and w <= 1):
                    SAStart2c(u, v, w)
                else:
                    print("invaild input, please input again")
        else:
            print("invaild input, please input again")

    while True:
        a = input("this is process D \n type 1 start with f(0,0,0,0) \n type 2 start with a random value \n type 3 start with a user-specified value \n type 4 Eixt \n :")
        a = int(a)
        if a == 4:
            break
        elif a == 1:
            SAStart2d(0, 0, 0, 0)
        elif a == 2:
            SAStart2d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1,1), random.uniform(-1,1))
        elif a == 3:
                u = input("please in put a number for value U between -1 and 1:")
                u = float(u)

                v = input("please in put a number for value V between -1 and 1:")
                v = float(v)

                w = input("please in put a number for value W between -1 and 1:")
                w = float(w)

                y = input("please in put a number for value Y between -1 and 1:")
                y = float(y)

                if ((u <= 1 and u >= -1) and (v >= -1 and v <= 1)) and ((w >= -1 and w <= 1) and (y >= -1 and y <= 1)):
                    SAStart2d(u, v, w, y)

                else:
                    print("invaild input, please input again")
        else:
            print("invaild input, please input again")

startWholeProcess() #<--Start Here!!!!!!!