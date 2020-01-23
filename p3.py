'''
    Subject: AI
    Practical: Classical "water jug problem" using state space tree (Python)
    Author: Raj Dhanani (160420116013)
'''

class Tree:

    def setParent(self,parentNode):
        self.parent = parentNode

    def addChild(self,childNode):
        self.childs.append(childNode)

    def setState(self,state):
        self.state = state

    def __init__(self):
        self.parent = None
        self.state = None
        self.childs = []
        
def createNode(state,parent):
    node = Tree()
    node.setState(state)
    node.setParent(parent)
    return node

def initializeChilds(jug1,jug2,parentNode,visitedStates): # creating the child nodes using the rules...

    x = createNode((parentNode.state[0], jug2), parentNode)
    if x.state not in visitedStates:
        parentNode.addChild(x)
        visitedStates.append(parentNode.childs[-1].state)

    x = createNode((jug1, parentNode.state[1]), parentNode)
    if x.state not in visitedStates:
        parentNode.addChild(x)
        visitedStates.append(parentNode.childs[-1].state)

    x = createNode((parentNode.state[0], 0), parentNode)
    if x.state not in visitedStates:
        parentNode.addChild(x)
        visitedStates.append(parentNode.childs[-1].state)

    x = createNode((0, parentNode.state[1]), parentNode)
    if x.state not in visitedStates:
        parentNode.addChild(x)
        visitedStates.append(parentNode.childs[-1].state)

    for d in range(0,max(jug1,jug2)):
        a = parentNode.state[0] + d
        b = parentNode.state[1] - d
        if ((a >=0 and b >= 0 and a <= jug1 and b <= jug2) and (a == jug1 or (b == 0 and b >= 0))):
            x = createNode((a, b), parentNode)
            if x.state not in visitedStates:
                parentNode.addChild(x)
                visitedStates.append(parentNode.childs[-1].state)

        a = parentNode.state[0] - d
        b = parentNode.state[1] + d
        if ((a >=0 and b >= 0 and a <= jug1 and b <= jug2) and (b == jug2 or (a == 0 and a >= 0))):
            x = createNode((a, b), parentNode)
            if x.state not in visitedStates:
                parentNode.addChild(x)
                visitedStates.append(parentNode.childs[-1].state)

def treeGeneration(jug1,jug2,final_jug1,final_jug2,root,visitedStates):

    if(root.state == (final_jug1,final_jug2)):
        return root
    else:
        initializeChilds(jug1,jug2,root,visitedStates)
        for i in root.childs:
            initializeChilds(jug1,jug2,i,visitedStates)
        for i in root.childs:
            result = treeGeneration(jug1,jug2,final_jug1,final_jug2,i,visitedStates)
            if result != False:
                return result
        return False


def traceSolution(root):
    revlist = []
    while(root != None):
        revlist.append(root.state)
        root = root.parent
    return revlist[::-1]

def waterjug(jug1,jug2,initial_jug1,initial_jug2,final_jug1,final_jug2):

    parentNode = Tree()
    parentNode.setState((initial_jug1,initial_jug2))
    visitedStates = [(initial_jug1,initial_jug2)]
    solvable = False
    solution = treeGeneration(jug1,jug2,final_jug1,final_jug2,parentNode,visitedStates)
    if solution != False:
        steps = traceSolution(solution)
        print(steps)
    else:
        print("No Solution!!")

j1,j2,i1,i2,f1,f2 = input("Enter capacity of jug 1 & 2, initial states of jug 1 & 2, goal states of jug 1 & jug 2 (Everything space separated):").split()
j1,j2,i1,i2,f1,f2 = int(j1),int(j2),int(i1),int(i2),int(f1),int(f2)
waterjug(j1,j2,i1,i2,f1,f2)
