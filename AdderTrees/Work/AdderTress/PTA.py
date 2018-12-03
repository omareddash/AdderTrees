import math
def PTA(n,levels,Fin,Fout):
    loopindex = [0 for x in range(levels)];
    Node = [x[:] for x in [[0] * n] * (levels)];
    bitspan = [0 for x in range(n)];
    for lv in range (0,levels):
        if lv == 0:
            loopindex[lv] = 3
        else:
             loopindex[lv] = 2**(lv+1) + 2**(lv) +1
        for i in range (n-1,loopindex[lv]-2, -2):
             msbTR = i
             lsbTR = i - 2**(lv) + 1
             msbnonTR = lsbTR - 1
             lsbnonTR = i - 2**(lv+1) + 1
             Node[lv][i] = [[msbTR,lsbTR],[msbnonTR,lsbnonTR]]
             bitspan[i] = lsbnonTR
    lv = levels-1
    bitspan[1] = 1
    for i in range (1, n,2):
            msbTR = i
            lsbTR = bitspan[i]
            msbnonTR = lsbTR - 1
            lsbnonTR = 0
            Node[lv][i] = [[msbTR,lsbTR],[msbnonTR,lsbnonTR]]
    return Node
def PTA_mfo(Node):
    for i in range(n-1,1,-2):
        getLFN(Node,i)



def getLFN(Node,i):
    templevel = len(Node)
    ithcol = [0 for x in range(len(Node))]
    for lv in range (len(Node), 1 , -1):
        for n in range(len(Node[lv]),i,-1):
            if(Node[lv][n] == 0):
                continue
            elif(Node[lv][n][2][1] == i):
                templevel = lv-1
                ithcol[lv-1]=1


N= PTA(16,4,2,2)
for p in range (0,len(N)):
    print(N[p])
