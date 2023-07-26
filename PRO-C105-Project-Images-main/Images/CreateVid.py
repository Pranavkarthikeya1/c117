import os
import cv2
path="Images"
Images=[]
for file in os.listdir(path):
    name,extension=os.path.splitext(file)
    #print(name)
    if(extension in [".jpg",".png",".jpeg",".gif"] ):
        fileName=path+"/"+file
        print(fileName)
        Images.append(fileName)
count=len(Images)
frame=cv2.imread(Images[0])
height,width,channels=frame.shape
size=(width,height)
out=cv2.VideoWriter("project.mp4",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
for i in range(0,count-1):
    frame=cv2.imread(Images[i])
    out.write(frame)
out.release()
print("done")