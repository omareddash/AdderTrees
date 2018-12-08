''' this code is written to investigate different adder tree structures and use dynamic programming to find the optimal approach'

'Co = Gn + PnGn-1 + PnPn-1Gn-1 + .... + PnPn-1...P1P0G0
Co = Gn + Pn:i*(Gn:i + Pi-1:0Gi-1:0)


'''
import math;
import array;
def StructureTree(n,restricitons,type):
    n = int(n);
    res = restricitons;
    type = type;
    Tree = [];
    if (res == 0):
        if type == 1 :
            #build a BK adder tree and return it

            Depth = 2*int(math.log2(n)) - 1;
            levels = int(math.log2(n));
            Tree =  [x[:] for x in [[0] * n] * Depth];
            for j in range (0,levels):
                nodes = ((n//(2**(j+1))));
                for k in range (0,nodes):
                    temp1 = ((2 ** (j + 1)) * (k + 1)) - 1;
                    if (k == 0):
                        Tree[j][temp1] = [temp1,temp1-(2**j),2];
                    else:
                        #Tree[j][temp1] = [2**(j+1)*k+1+2**j,2**(j+1)*k+1, 1];
                        Tree[j][temp1] = [2 ** (j + 1) * (k + 1) -1 , 2 ** (j + 1) * (k + 1)-1-(2**j), 1];
            levels2 = int(math.log2(n));
            for j in range (levels2,Depth):
                x = int(j-math.log2(n));
                for k in range (1,int((2**(x+1)))):
                    index2 = int((k*n//(2**(x+1))-1)+(n//(2**(x+2))));
                    mainnode = int((k*n/(2**(x+1))-1)+(n/(2**(x+2))));
                    secondarynode = int((k*n/(2**(x+1)))-1);
                    Tree[j][ index2] = [mainnode, secondarynode, 2];
        elif type == 2:     #Han Carlson
            Depth = int(math.log2(n))+1
            Tree = [x[:] for x in [[0] * n] * Depth];
            for j in range (0,Depth):
                if j==0:
                    Node0=1
                    rooted = 1
                    Nodes = int((n - Node0 + 1) / 2)
                    preNode = 2**j
                elif (j==Depth-1):
                    Node0=2
                    rooted = 100
                    Nodes = int((n/2)-1)
                    preNode = 1
                else:
                    Node0 = 1 + 2**j
                    rooted = 2**(j-1)
                    Nodes = int((n-Node0+1)/2)
                    preNode = 2 ** j
                for k in range(0,Nodes):
                    indexk = Node0 + (2*k)
                    if (k>rooted-1):
                        Tree[j][indexk] = [indexk,indexk-preNode,1]
                    else:
                        Tree[j][indexk] = [indexk, indexk - preNode, 2]
        elif type == 3: #Sklansky
            Tree = [[0,[1,0,2],0,[3,2,1],0,[5,4,1],0,[7,6,1],0,[9,8,1],0,[11,10,1],0,[13,12,1],0,[15,14,1]],
                    [0,0,[2,1,2],[3,1,2],0,0,[6,5,1],[7,5,1],0,0,[10,9,1],[11,9,1],0,0,[14,13,1],[15,13,1]],
                    [0,0,0,0,[4,3,2],[5,3,2],[6,3,2],[7,3,2],0,0,0,0,[12,11,1],[13,11,1],[14,11,1],[15,11,1]],
                    [0,0,0,0,0,0,0,0,[8,7,2],[9,7,2],[10,7,2],[11,7,2],[12,7,2],[13,7,2],[14,7,2],[15,7,2]]]

        elif type == 4: #Knowles
            Tree = [[0, [1,0,2], [2,1,1], [3,2,1], [4,3,1], [5,4,1], [6,5,1], [7,6,1], [8,7,1], [9,8,1], [10,9,1], [11,10,1], [12,11,1], [13,12,1], [14,13,1], [15,14,1]],
                    [0,0,[2,0,2],[3,1,2],[4,2,1],[5,3,1],[6,4,1],[7,5,1],[8,6,1],[9,7,1],[10,8,1],[11,9,1],[12,10,1],[13,11,1],[14,12,1],[15,13,1]],
                    [0,0,0,0,[4,0,2],[5,1,2],[6,2,2],[7,3,2],[8,4,1],[9,5,1],[10,6,1],[11,7,1],[12,8,1],[13,9,1],[14,10,1],[15,11,1]],
                    [0,0,0,0,0,0,0,0,[8,1,2],[9,1,2],[10,3,2],[11,3,2],[12,5,2],[13,5,2],[14,7,2],[15,7,2]]]
        elif type == 5: #KoggeStone
            Tree = [[0, [1,0,2], [2,1,1], [3,2,1], [4,3,1], [5,4,1], [6,5,1], [7,6,1], [8,7,1], [9,8,1], [10,9,1], [11,10,1], [12,11,1], [13,12,1], [14,13,1], [15,14,1]],
                    [0,0,[2,0,2],[3,1,2],[4,2,1],[5,3,1],[6,4,1],[7,5,1],[8,6,1],[9,7,1],[10,8,1],[11,9,1],[12,10,1],[13,11,1],[14,12,1],[15,13,1]],
                    [0,0,0,0,[4,0,2],[5,1,2],[6,2,2],[7,3,2],[8,4,1],[9,5,1],[10,6,1],[11,7,1],[12,8,1],[13,9,1],[14,10,1],[15,11,1]],
                    [0,0,0,0,0,0,0,0,[8,0,2],[9,1,2],[10,2,2],[11,3,2],[12,4,2],[13,5,2],[14,6,2],[15,7,2]]]
        elif type == 6: #Ladner Fischer Direct
            Tree = [
                [0, [1, 0, 2], 0, [3, 2, 1], 0, [5, 4, 1], 0, [7, 6, 1], 0, [9, 8, 1], 0, [11, 10, 1], 0, [13, 12, 1],
                 0, [15, 14, 1]],
                [0, 0, 0, [3, 1, 2], 0, 0, 0, [7, 5, 1], 0, 0, 0, [11, 9, 1], 0, 0, 0, [15, 13, 1]],
                [0, 0, 0, 0, 0, [5, 3, 2], 0, [7, 3, 2], 0, 0, 0, 0, 0, [13, 11, 1], 0, [15, 11, 1]],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, [9, 7, 2], 0, [11, 7, 2], 0, [13, 7, 2], 0, [15, 7, 2]],
                [0,0,[2,1,2],0,[4,3,2],0,[6,5,2],0,[8,7,2],0,[10,9,2],0,[12,11,2],0,[14,13,2],0]]

        elif type == 100: #Ladner Fischer
            Depth = int(math.log2(n)) + 1
            Tree = [x[:] for x in [[0] * n] * Depth];
            for j in range(0, Depth):
                if j == 0:
                    Node0 = 1
                    rooted = 1
                    Nodes = int((n - Node0 + 1) / 2)
                    preNode = 2 ** j
                    sectionsize = 1
                    sections = int(n / (2 ** (j + 1)))
                    step = (2 ** (j+1))
                elif (j == Depth - 1):
                    Node0 = 2
                    rooted = n+1
                    sections = int((n / 2) - 1)
                    preNode = 1
                    sectionsize = 1
                    step = 2
                else:
                    Node0 = 1 + 2 ** (j)
                    rooted = 2 ** (j+1)
                    Nodes = int((n/4))
                    sectionsize = 2**(j-1)
                    sections = int(n / (2**(j+1)))
                    preNode = 2
                    setp = (2 ** (j+1))
                for k in range(0, sections):
                    for s in range(0,sectionsize):
                        indexk = Node0 + step*k + (2*s)
                        if (indexk > rooted ):
                           Tree[j][indexk] = [indexk, indexk - preNode - (2*s), 2]
                        else:
                            Tree[j][indexk] = [indexk, indexk - preNode  - (2*s), 1]
        #elif type == 0: #Polynomial Time Algorithm
            
    return Tree;


def BuildTree():
    Tree = StructureTree(16,0,1);
    for i in range (0,len(Tree)):
        print(Tree[i]);
        print('\n');

    print(len(Tree));
    print();

BuildTree()
