import pygame as p
import time
pd=p.display
d=255
TS=10
SS=500
TH=int(SS/TS)
p.init()
s=pd.set_mode([SS,SS])
b=[[0 for x in range(TH)] for y in range(TH)] 
b[20][20]=b[20][21]=b[20][22]=b[19][22]= b[18][21]=1
b[40][20]=b[40][21]=b[40][22]=b[39][22]= b[38][21]=1
b[10][11]=b[11][11]=b[12][11]=1
b[20][11]=b[21][11]=b[22][11]=1
b[10][11]=b[11][11]=b[12][11]=1
b[20][11]=b[21][11]=b[22][11]=1
b[30][24]=b[31][24]=1
b[30][25]=b[31][25]=1

b[30][25]=b[31][25]=b[32][25]=b[33][25]=1
b[30][26]=b[31][26]=b[32][26]=b[33][26]=1
b[30][27]=b[32][27]=b[30][28]=b[32][28]=1

def c(x,y,b):
    return b[x%TH][y%TH]
while 1:
    for event in p.event.get():
        pass
    for i in range(0,TH):
        for j in range(0 ,TH):
                p.draw.rect(s,((d,d,d) if b[i][j]==1 else (0,0,0)),(i*TS,j*TS,TS,TS))
    nb=[[0 for x in range(TH)] for y in range(TH)] 
    for i in range(0,TH):
        for j in range(0 ,TH):
            n=c(i-1,j-1,b)+c(i,j-1,b)+c(i+1,j-1,b)+c(i-1,j,b)+c(i+1,j,b)+c(i-1,j+1,b)+c(i,j +1,b)+c(i+1,j+1,b)
            if(b[i][j]==1):
                if(n<2): 
                    nb[i][j]=0
                if(n==2 or n==3):
                    nb[i][j]=1
                if(n> 3):
                    nb[i][j]=0
            elif(n==3):
                nb[i][j]=1
    b=nb
    pd.flip()
    time.sleep(0.25)