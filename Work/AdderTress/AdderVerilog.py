''' this code is written to generate Verilog for Prefix Adders

Co = Gn + PnGn-1 + PnPn-1Gn-1 + .... + PnPn-1...P1P0G0
Co = Gn + Pn:i*(Gn:i + Pi-1:0Gi-1:0)


'''

from AdderTree import StructureTree;

def generateVerilog(bitwidth,treetype):
    verilog_file = open("Adder.v","w");
    verilog_file.write("module prefixadder( \n")
    verilog_file.write("input  [%s : 0] A,\n" %(bitwidth-1));
    verilog_file.write("input  [%s : 0] B, \n" % (bitwidth-1));
    verilog_file.write("output  [%s : 0] Sum, \n" % (bitwidth-1));
    verilog_file.write("output  Cout, \n");
    verilog_file.write("output  [%s : 0] Cg); \n" % (bitwidth-1));
    #from AdderTree import StructureTree;

    Tree = StructureTree(bitwidth,0,treetype);
    Depth = len(Tree);
    verilog_file.write("wire [%s : 0] p; \n"%(bitwidth-1));
    verilog_file.write("wire [%s : 0] g; \n" % (bitwidth-1));
    for pi in range(0, bitwidth):
        verilog_file.write("assign p[{0}] = A[{0}] ^ B[{0}]; \n".format(pi));
        verilog_file.write("assign g[{0}] = A[{0}] & B[{0}]; \n".format(pi));


    for i in range(0,Depth):
        for j in range(0,bitwidth):
            verilog_file.write("wire cp{0}[{1}],cg{0}[{1}];\n".format(i,j));



    verilog_file.close();


generateVerilog(8,1)