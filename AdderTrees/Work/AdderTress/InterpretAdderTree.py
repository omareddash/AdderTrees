


import math;
import numpy as np;
import matplotlib.pyplot as plt

from numpy import zeros

def InterpretAdderTree(AdderTree,n,Depth,p,g):
    #AdderTree Structure is compiled here as an actual dataflow
    elements = Depth#//n;
    pgs = [x[:] for x in [[0] * n] * (Depth+1)];
    #print('Depth')
    #print(Depth)
    #print(pgs);
    #print('Adder Tree '+'\n')
    #print(AdderTree)
    #print('\n')
    #p,g = [x[:] for x in [[0] * n]];
    for k in range (0,len(p)):
        pgs[0][len(p)-k-1]= [g[k],p[k]];
    #go row by row and have the initial inputs labeled as pn and gn
    for i in range (1,elements+1):
        for j in range (0,n):
            #print('pg'+(AdderTree[i][j]))
            if AdderTree[i-1][j] == 0 :
                #No Computation
                pgs[i][j]=pgs[i-1][j];

            else:
                if (AdderTree[i-1][j][2]==2):
                    IndexMaster = int(AdderTree[i-1][j][0]);
                    IndexSlave = int(AdderTree[i-1][j][1]);
                    pgs[i][j] = [0, 0]
                    pgs0 = pgs[i-1][IndexMaster][0] or (pgs[i-1][IndexMaster][1] and pgs[i-1][IndexSlave][0]);
                    pgs[i][j][0]= pgs0;
                    pgs1 = pgs[i-1][j][1];
                    pgs[i][j][1]= pgs1
                    #Only and or gate
                    #add area and time cost
                else:
                    IndexMaster = int(AdderTree[i-1][j][0]);
                    IndexSlave = int(AdderTree[i-1][j][1]);
                    pgs[i][j] =[0,0]
                    #print("i="+str(i))
                    #print("master"+str(IndexMaster))
                    #print("slave"+str(IndexSlave))
                    #print(len(pgs),len(pgs[0]))
                    pgs0 = pgs[i - 1][IndexMaster][0] or (pgs[i - 1][IndexMaster][1] and pgs[i - 1][IndexSlave][0]);
                    pgs[i][j][0] = pgs0
                    pgs1 = pgs[i - 1][IndexMaster][1] and pgs[i-1][IndexSlave][1];
                    pgs[i][j][1] = pgs1
                    #And or gate + and gate for propagates
                    #Add area and time cost
    return pgs;

def SimulateAdder(n):
        from  AdderTree import StructureTree;
        Tree = StructureTree(n,0,1);
        pgsstats = [[0] * n for i in range(len(Tree)+1)]
        pngsstats = [[0] * n for i in range(len(Tree)+1)]
        for index1 in range(0,len(pngsstats)):
            for index2 in range(0,len(pngsstats[index1])):
                pngsstats[index1][index2]=[0,0]

        xrand = np.random.normal(128, 10, 2 ** n)
        yrand = np.random.normal(128, 10, 2 ** n)

        for x in range (1,2**n):
        #x = 2**(n-2)
        #if (x>0):
            for y in range(1,2**n):
                #sum = x + y
                #xbin = bin(x)
                #ybin = bin(y)
                #xbin = '{0:08b}'.format(int(xrand[x]))
                #ybin = '{0:08b}'.format(int(yrand[y]))
                xbin = format(x,'016b')
                ybin = format(y,'016b')
                A = [int(xbin[i]) for i in range(0, n)]
                B = [int(ybin[i]) for i in range(0, n)]
                #A = xbin[0:];
                #B = ybin[0:];
                p =[]
                g =[]
                for i in range (0,n):
                    p.append(0)
                    g.append(0)
        #p=[];
        #g=[];
                #print(p);
                #print('A =')
                #print(A)
                #print ('B =')
                #print(B)
                    p[i]= A[i] or B[i];
                    g[i]= A[i] and B[i];
                #print ('p =')
                #print (p);
                #print('\n');
                #print('g =')
                #print(g);
                #print('\n');
                Depth = 2*int(math.log2(n)) - 1
                pgs = InterpretAdderTree(Tree,n,Depth,p,g);
                #print(pgs);
                for z in range(0,len(pgs)):
                    #print('pgs '+str(z)+'=')
                    #print(pgs[z]);
                    for zz in range(0,len(pgs[z])):
                        if (z>0):
                            if pgs[z][zz] != pgs[z-1][zz]:
                                #print(z,zz)
                                pgsstats[z][zz] +=1
                for z1 in range(0,len(pgs)):
                    #print('pgs '+str(z)+'=')
                    #print(pgs[z]);
                    for zz1 in range(0,len(pgs[z1])):
                        if (z1>0):
                            if pgs[z1][zz1][0] != pgs[z1-1][zz1][0]:
                                #print(z,zz)
                                pngsstats[z1][zz1][0] +=1
                            if pgs[z1][zz1][1] != pgs[z1-1][zz1][1]:
                                #print(z,zz)
                                pngsstats[z1][zz1][1] +=1



        #print('Stats')
        #print(pgsstats)
        #print('P and G stats')
        #print(pngsstats)


def SimulateAdderFilter(n,adder,filter):
    from AdderTree import StructureTree;
    Tree = StructureTree(n, 0, adder);
    from Filter_Image import LoadImageData;
    sobelx = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    sobely = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    Filter = sobelx
    FilterName = 'Sobel'
    if (filter == 1):
        Filter = sobelx
        FilterName = 'Sobel'
    elif(filter == 2):
        Filter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
        FilterName = 'Edge Detection I'
    elif(filter==3):
        Filter = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
        FilterName = 'Edge Detection II'
    elif(filter==4):
        Filter = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
        FilterName = 'Sharpen'
    elif(filter == 5):
        Filter = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9,1/9, 1/9]]
        FilterName = 'Box Blur'
    elif(filter == 6):
        Filter = [[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]]
        FilterName = 'Gaussian Blur'

    addarray = LoadImageData(Filter)
    pgsstats = [[0] * n for i in range(len(Tree) + 1)]
    pngsstats = [[0] * n for i in range(len(Tree) + 1)]
    for index1 in range(0, len(pngsstats)):
        for index2 in range(0, len(pngsstats[index1])):
            pngsstats[index1][index2] = [0, 0]

    xrand = np.random.normal(128, 10, 2 ** n)
    yrand = np.random.normal(128, 10, 2 ** n)
    xx2_grid = [(x, x2) for x in range(0,len(addarray)) for x2 in range(0,len(addarray[0]))]
    for x,x2 in (xx2_grid):
        # x = 2**(n-2)
        # if (x>0):
        if(addarray[x][x2][0])<0:
            temp = addarray[x][x2][0]+2**n
            xbin = format(int(temp), '016b')
            sum = int(temp)
        else:
            xbin = format(int(addarray[x][x2][0]), '016b')
            sum = int(addarray[x][x2][0])
        for y in range(1, len(addarray[x][x2])-1):
            # sum = x + y
            # xbin = bin(x)
            # ybin = bin(y)
            # xbin = '{0:08b}'.format(int(xrand[x]))
            # ybin = '{0:08b}'.format(int(yrand[y]))
            added = int(addarray[x][x2][y])
            if added <0:
                temp = added+ 2**n
                ybin = format(int(temp), '016b')
            else:
                ybin = format(int(added), '016b')
            A = [int(xbin[i]) for i in range(0, n)]
            B = [int(ybin[i]) for i in range(0, n)]
            # A = xbin[0:];
            # B = ybin[0:];
            p = []
            g = []
            for i in range(0, n):
                p.append(0)
                g.append(0)
                # p=[];
                # g=[];
                # print(p);
                # print('A =')
                # print(A)
                # print ('B =')
                # print(B)
                p[i] = A[i] or B[i];
                g[i] = A[i] and B[i];
            # print ('p =')
            # print (p);
            # print('\n');
            # print('g =')
            # print(g);
            # print('\n');
            #Depth = 2 * int(math.log2(n)) - 1
            Depth = len(Tree)
            pgs = InterpretAdderTree(Tree, n, Depth, p, g);
            # print(pgs);
            for z in range(0, len(pgs)):
                # print('pgs '+str(z)+'=')
                # print(pgs[z]);
                for zz in range(0, len(pgs[z])):
                    if (z > 0):
                        if pgs[z][zz] != pgs[z - 1][zz]:
                            # print(z,zz)
                            pgsstats[z][zz] += 1
            for z1 in range(0, len(pgs)):
                # print('pgs '+str(z)+'=')
                # print(pgs[z]);
                for zz1 in range(0, len(pgs[z1])):
                    if (z1 > 0):
                        if pgs[z1][zz1][0] != pgs[z1 - 1][zz1][0]:
                            # print(z,zz)
                            pngsstats[z1][zz1][0] += 1
                        if pgs[z1][zz1][1] != pgs[z1 - 1][zz1][1]:
                            # print(z,zz)
                            pngsstats[z1][zz1][1] += 1
            sum = sum + added
            if sum <0:
                temp = sum + 2**n
                xbin = format(temp, '016b')
            else:
                xbin = format(sum, '016b')
    #print('Stats')
    #print(pgsstats)
    pgstatsArray = np.array(pgsstats)
    pngstatsArray = np.array(pngsstats)
    #print(pgstatsArray)
    #print('P and G stats')
    pngstatsArray = pngstatsArray/(62*62*27)
    #print(pngstatsArray)
    Results = open(r"results6.txt", "a")
    Results.write('#######################################')
    Results.write('\n\n')

    AdderName = ''
    if (adder == 1):
        AdderName = 'Brent Kung'
    elif(adder == 2):
        AdderName = 'Han Carlson'
    elif(adder==3):
        AdderName = 'Sklansky'
    elif(adder==4):
        AdderName = 'Knowles'
    elif(adder==5):
        AdderName = 'KoggeStone'
    elif(adder==6):
        AdderName = 'Ladner Fischer'
    Results.write('This is  the results from %a for %a Adder'%(FilterName,AdderName))
    Results.write('\n\n')
    for line in range(0,len(pngstatsArray)):
        Results.write(str(pngstatsArray[line]))
        Results.write('\n')
    return pngsstats;

#ArrayAdd;

for count in range(1,7):
    if (count ==1):
        TreeLength = 7
    elif (count ==2 or 6):
        TreeLength = 5
    elif (count == 3 or 4 or 5):
        TreeLength = 4

    AdderArray = [[[0] * 16 for i in range(TreeLength)]for k in range(7)];
    for filter in range (1,7):
        Adder = SimulateAdderFilter(16,count,filter);
        #size = Adder.shape;
        #ArrayAdd[count, filter,size[0],size[1],size[2]] = Adder[filter]
        AdderArray[filter] = Adder
        #np.append(AdderArray,Adder)
    #Adder2 = np.array(Adder)
    fig, ax = plt.subplots(len(AdderArray[0]),len(AdderArray[0][0]))
    #plt.xticks(fontsize=5)
    #plt.yticks(fontsize=5)
    #plt.tight_layout()

    for a1 in range (1,len(AdderArray[0])):
        for a2 in range (0,len(AdderArray[0][0])):
            #print(a1)
            #print(AdderArray[0][a1][a2])
            datatemp = [AdderArray[x][a1][a2] for x in range(1,7)]
            data = [0 for var in range(len(datatemp))]
            for filter in range(0, 6):
               if datatemp[filter]==0:
                   data[filter] = 0
               else:
                   data[filter] = datatemp[filter][0]
            ax[a1-1][a2].bar([0.8*f for f in range(0,6)],data)
            ax[a1-1][a2].set_ylim([0,15000])
                #ax = fig.add_subplot(len(ArrayAdd), len(ArrayAdd[0]), a1*a2)

    #            #df[var_name].hist(bins=10, ax=ax)
    #            #plt.title(var_name + "Distribution")
    #            ax.plot(Array[count][filter][a1][a2])

    #fig.show()
plt.show()
plt.savefig("test1.png",bbox_inches='tight')
