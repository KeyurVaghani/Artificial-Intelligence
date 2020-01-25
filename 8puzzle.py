from copy import copy, deepcopy
import sys
sys.setrecursionlimit(10 ** 6)

class Tree:

    def setParent(self,parentNode):
        self.parent = parentNode

    def addChild(self,childNode):
        self.childs.append(childNode)

    def setState(self,state):
        self.state = state

    def setLevel(self,level):
        self.level = level

    def setCost(self,cost):
        self.cost = cost

    def __init__(self):
        self.parent = None
        self.state = None
        self.childs = []
        self.level = None
        self.cost = None

def createNode(state,level,parent,cost):
    node = Tree()
    node.setState(state)
    node.setParent(parent)
    node.setLevel(level)
    node.setCost(cost)
    return node

def matrixIndexOf(matrix,element):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == element:
                return i,j
    return -1,-1

def printMatrix(x):
    for i in x:
        print(i)
    print()

def cost(current,final,level):
    count = 0
    for i in range(3):
        for j in range(3):
            if current[i][j] == final[i][j]:
                count+=1
    return 9-count

def initializeChilds(parentNode,finalState,level,visitedStates):

    xIndex, yIndex = matrixIndexOf(parentNode.state,0)

    xstart,xend,xstep = -1,2,2
    ystart, yend, ystep = -1, 2, 2
    if xIndex == 0:
        xstart,xend,xstep = 1,2,2
    if yIndex == 0:
        ystart,yend,ystep = 1,2,2
    if xIndex == 2:
        xstart, xend, xstep = -1, 0, 2
    if yIndex == 2:
        ystart, yend, ystep = -1, 0, 2

    for i in range(xstart,xend,xstep):
        # print('x',i)
        temp1 = deepcopy(parentNode.state)
        temp1[xIndex][yIndex],temp1[xIndex+i][yIndex] = temp1[xIndex+i][yIndex],temp1[xIndex][yIndex]
        if temp1 not in visitedStates:
            visitedStates.append(temp1)
            parentNode.childs.append(createNode(temp1,level,parentNode,cost(temp1,finalState,level)))
            # printMatrix(temp1)

    for i in range(ystart,yend,ystep):
        # print('y',i)
        temp2 = deepcopy(parentNode.state)
        temp2[xIndex][yIndex],temp2[xIndex][yIndex+i] = temp2[xIndex][yIndex+i],temp2[xIndex][yIndex]
        if temp2 not in visitedStates:
            visitedStates.append(temp2)
            parentNode.childs.append(createNode(temp2,level,parentNode,cost(temp1,finalState,level)))
            # printMatrix(temp2)

def takeCost(elem):
    return elem.cost

def treeGreneration(parentNode,finalState,level,visitedStates,parentCost,q):

    while (len(q) != 0):
        current = q[0]
        q.pop(0)
        q.sort(key=takeCost)
        initializeChilds(current,finalState,current.level + 1,visitedStates)
        for i in current.childs:
            if i.state == finalState:
                return i
            else:
                q.append(i)


def traceSolution(root):
    print('SOLUTION:')
    revlist = []
    while(root != None):
        revlist.append(root.state)
        root = root.parent
    return len(revlist), revlist[::-1]

def _8puzzle(rootState):
    q = []
    # rootState = [
    #                 [1, 8, 2],
    #                 [0, 4, 3],
    #                 [7, 6, 5]
    #             ]
    finalState = [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]
                 ]
    visitiedStates = [rootState]
    root = createNode(rootState,0,None,cost(rootState,finalState,0))
    q = [root]
    sol = treeGreneration(root,finalState,1,visitiedStates,root.cost,q)
    l, solution = traceSolution(sol)
    for i, s in enumerate(solution):
        printMatrix(s)
        if (i < l-1):
            print('\t|')
            print('\tV')
            print()

inputState = []
print('Enter the input state (Assumption: the input state is solvable):')
for i in range(3):
    s = input()
    inputState.append([int(x) for x in s.split()])

_8puzzle(inputState)
