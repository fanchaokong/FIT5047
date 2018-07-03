import copy as cp
'''
goal list is the order of goal state
inState list is the initial state 
puzzle list is a list provide each cell 
'''
#test1 = [5, 1, 2, 3, 9, 6, 7, 4, 13, 10, 12, 8, 0, 14, 11, 15]
#test2 = [0, 1, 2, 3, 5, 6, 7, 4, 9, 10, 12, 8, 13, 14, 11, 15]
goal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
inState = [1,2,3,4,5,6,7,8,9,10,12,0,13,14,11,15]
puzzle = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]

def findIt(number,state):
    result = 0
    for i in range(len(state)):
        if state[i] == number:
            return i

# getHur function mianing use for current state
def getHur(state):
    H = 0
    for index, i in enumerate(state):
        if i == goal[index] or i == 0:
            h1 = 0
            h2 = 0
        else:
            x = findIt(i,goal)
            h1 = ((puzzle[index][0]-puzzle[x][0])**2+(puzzle[index][1]-puzzle[x][1])**2)**0.5
            h2 = 1
        H += h1 + h2
    return H

# 
def findItLocation(location):
    for index,i in enumerate(puzzle):
        if i == location:
            return index

def upBlank(state):
    result = []
    index = findIt(0, state)
    y = puzzle[index][0]
    x = puzzle[index][1]
    if y != 0:
        temp = state[index]
        state[index] = state[findItLocation([y-1, x])]
        state[findItLocation([y-1, x])] = temp
    result = state
    return result

def downBlank(state):
    result = []
    index = findIt(0, state)
    y = puzzle[index][0]
    x = puzzle[index][1]
    if y != 3:
        temp = state[index]
        state[index] = state[findItLocation([y+1, x])]
        state[findItLocation([y+1, x])] = temp
    result = state
    return result

def leftBlank(state):
    result = []
    index = findIt(0, state)
    y = puzzle[index][0]
    x = puzzle[index][1]
    if x != 0:
        temp = state[index]
        state[index] = state[findItLocation([y, x-1])]
        state[findItLocation([y, x-1])] = temp
    result = state
    return result


def rightBlank(state):
    result = []
    index = findIt(0, state)
    y = puzzle[index][0]
    x = puzzle[index][1]
    if x != 3:
        temp = state[index]
        state[index] = state[findItLocation([y, x+1])]
        state[findItLocation([y, x+1])] = temp
    result = state
    return result
#when move blank cell, and add different huristics in a dictionary
def findSamllest(dic):
    temp = 10000000
    result = ""
    for i in dic:
        if dic[i]<temp:
            temp = dic[i]
            result = i
    return result
# this function is used to find the path about how to move the cell
def path(inState):
    result = []
    g = 1
    H = 0
    t= 0
    temp = cp.copy(inState)
    while True:
        print(temp)
        dic = {}
        state1 = upBlank(cp.copy(temp))
        if state1 != temp:
            H1 = getHur(state1) + g
            dic["up"] = H1
        state2 = downBlank(cp.copy(temp))
        if state2 != temp:
            H2 = getHur(state2) + g
            dic["down"] = H2
        state3 = leftBlank(cp.copy(temp))
        if state3 != temp:
            H3 = getHur(state3) + g
            dic["left"] = H3
        state4 = rightBlank(cp.copy(temp))
        if state4 != temp:
            H4 = getHur(state4) + g
            dic["right"] = H4
        
        result.append(findSamllest(dic))
        print("different huristics of different way to move blank cel\n", dic)
        if result[-1] == "down":
            temp = downBlank(temp)
        elif result[-1] == "up":
            temp = upBlank(temp)
        elif result[-1] == "left":
            temp = leftBlank(temp)
        else:
            temp = rightBlank(temp)
        print("move: ", findSamllest(dic))
        print("<--Next-->")
        g += 1
        if temp == goal:
            break
    print(result)
    return result

path(inState)

#path(test1)
#path(test2)

