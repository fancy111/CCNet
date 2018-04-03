# -*- coding: utf-8 -*-
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt



path = "C:/Users/fancy/Desktop/characters_48"
otherpath="C:/Users/fancy/Desktop/Other48.set"
files = os.listdir(path)

f=open('temp.txt','wb')
i=0
y=[]
namelist=[]

#先遍历文件名
for filename in files:
    if i==4:
        break
    filepath = path+'/'+filename
    file = open(filepath,'rb')
    for line in file.readlines():
        f.write(line)
    file.close()

    #更新y数组
    y_temp = np.arange(1000)
    y_temp.fill(i)
    y = np.concatenate((y,y_temp),axis=0)

     #更新名字数组
    namelist.append(filename[:-4])

    print(i)
    i = i+1

#打开其他类型的字模文件
othersize = os.path.getsize(otherpath)
unum = int(othersize/(48*48))
otherfile = open(otherpath,'rb')
for line in otherfile.readlines():
    f.write(line)
file.close()
#添加一类未知类
y_temp = np.arange(unum)
y_temp.fill(i)
y = np.concatenate((y,y_temp),axis=0)
namelist.append("unkonwn")

#关闭文件
f.close()

print(namelist)

tempfile = open('temp.txt','rb')
x = np.fromfile(tempfile, dtype = np.ubyte).reshape((i)*1000+unum,48*48)

try:
    with open('Xdata.txt','wb') as x_file:
        pickle.dump(x,x_file)
    with open('Ydata.txt','wb') as y_file:
        pickle.dump(y,y_file) 
    with open('label.txt','wb') as label_file:
        pickle.dump(namelist,label_file) 
except IOError as err:  
    print('File error: ' + str(err))  
except pickle.PickleError as perr:  
    print('Pickling error: ' + str(perr))  