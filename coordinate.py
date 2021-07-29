# look at the libraries used
import cv2 as cv
import numpy as np
x_cord=[]
y_cord=[]
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(resized_image,(x,y),2,(255,255,255),-1)
        x_cord.append(x)
        y_cord.append(y)
path_initial="/home/arjun/Desktop/DESIGN_LAB_PROJECT/"#change the path
orig_image=cv.imread(path_initial+"graph3.png")#and name of the image accordingly
orig_image=cv.cvtColor(orig_image,cv.COLOR_BGR2GRAY)
new_dim=(250,250)#(width,height) can be changed accordingly
resized_image=cv.resize(orig_image,dsize=new_dim)
binary=(resized_image>150)*1
# this is going to print binary values of our image , copy  it to .mif file.
for i in range(len(binary)):

    for j in binary[i]:
        print(j)

cv.imshow('Please click on node centers starting from  node 1  to node 23',resized_image)
cv.setMouseCallback('Please click on node centers starting from  node 1  to node 23',draw_circle)

while(1):

    cv.imshow('Please click on node centers starting from  node 1  to node 23',resized_image)
    if cv.waitKey(20) & 0xFF == 27:

        cv.imwrite(path_initial+"resized_graph.png", resized_image)
        break
cv.destroyAllWindows()

get_bin = lambda x, n: format(x, 'b').zfill(n)


# case for the encoder bock
#  paste the generated code  in the .v file
print("case(k)")
for i in range(len(x_cord)):
    value=x_cord[i]+y_cord[i]*250
    index=i+1
    print("16'b"+get_bin(value,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value+1,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value-1,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value-250,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value+250,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value-249,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value-251,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value+251,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
    print("16'b"+get_bin(value+249,16)+ ": index_bar=5'b"+get_bin(index,5)+";")
print("default : index_bar=5'b00000;")
print("endcase")



