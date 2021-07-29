# # A denotes our directed graph
# A=[[0,1,0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,2,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,4,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,7,0,0,0,0,2,4,0,0],
#    [0,0,0,0,0,8,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,3,0,0,0,0,0,0,0,0],
#    [0,0,0,0,4,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,2,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,1,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0,6,3],
#    [0,0,0,0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0,0,2,0]]
import numpy as np
A=[[0 for i in range(23)] for j in range(23)]
A[0][1]=2
A[0][2]=4
A[0][4]=1
A[1][3]=1
A[2][5]=3
A[3][8]=7
A[4][7]=2
A[5][6]=1
A[6][20]=2
A[6][22]=2
A[7][8]=3
A[7][9]=4
A[8][9]=5
A[9][10]=1
A[9][13]=7
A[9][22]=4
A[10][11]=2
A[11][12]=3
A[12][13]=1
A[14][13]=1
A[15][13]=1
A[16][14]=1
A[17][16]=2
A[18][15]=2
A[18][21]=2
A[19][17]=1
A[19][18]=4
A[20][19]=1
A[20][21]=1
A[21][22]=3
print(np.array(A,dtype="uint8"))
l=len(A)
get_bin = lambda x, n: format(x, 'b').zfill(n)
edges=0
for j in range(l):
    for i in range(l):
        if A[i][j]!=0:
            dest=j+1
            source=i+1
            weight_edge_btw_ij=A[i][j]
            print(get_bin(weight_edge_btw_ij,4),get_bin(source,5),get_bin(dest,5),sep="")
           # print(weight_edge_btw_ij,source,dest)
            edges=edges+1

zero_rows=32-edges
for i in range(zero_rows):
	print("00000000000000")

