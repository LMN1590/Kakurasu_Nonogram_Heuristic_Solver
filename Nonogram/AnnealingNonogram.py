import random
from math import exp

#Function to generate a random table to begin with.
def genRandomTable(size):
    table=[[(1 if random.random()>0.5 else 0) for i in range(size)] for j in range(size)]
    return table

#Function to duplicate a table
def dupTable(base):
    newer=[]
    for i in base:
        newer.append(list(i))
    return newer

#Function to calculate the current cost/errors of the current table when compared to the constraints
def calCost(table,row,col):
    cost = 0

    curRow=[]
    for i in row:
        curRow.append(list(i))
    curCol=[]
    for i in col:
        curCol.append(list(i))
    #Array to check whether the previous index is black or white. False for white and True for black
    lastCheckedRow=[False for i in range(len(table))]
    lastCheckedCol=[False for i in range(len(table))]

    for indexRow in range(len(table)):
        for indexCol in range(len(table)):
            if(table[indexRow][indexCol]==1):
                #If current index is black while the constraint of either the row or column is zero, the cost will rise by 1 and the other(column/row) will be unaffected

                curRow[indexCol][0]-=1
                curCol[indexRow][0]-=1
                #If the current line of the row or/and the column is smaller than 0, it will be add to the cost/errors
                if(curRow[indexCol][0]<0): cost+=1
                if(curCol[indexRow][0]<0): cost+=1

                lastCheckedRow[indexRow]=True
                lastCheckedCol[indexCol]=True

            else:
                #If there is still remaining black tiles in a line but it is cut off by a white tile, cost/errors will increase
                if(len(curRow[indexCol])>0 and lastCheckedCol[indexCol]):
                    if(curRow[indexCol][0]>0):
                        cost+=1
                        curRow[indexCol][0]-=1
                    else:
                        del curRow[indexCol][0]
                lastCheckedCol[indexCol]=False
                if(len(curCol[indexRow])>0 and lastCheckedRow[indexRow]):
                    if(curCol[indexRow][0]>0):
                        cost+=1
                        curCol[indexRow][0]-=1
                    else:
                        del curCol[indexRow][0]
                lastCheckedRow[indexRow]=False
            if(len(curRow[indexCol])==0): 
                curRow[indexCol].append(0)
            if(len(curCol[indexRow])==0): 
                curCol[indexRow].append(0)
        #The remaining uncounted lines in a row will be added to the cost/errors
        for num in curCol[indexRow]:
            if(num>0): cost+=num

    #The remaining uncounted lines in all columns will be added to the cost/errors
    for indexCol in range(len(table)):
        for num in curRow[indexCol]:
            if(num>0): cost+=num
    return cost
#Evaluate the probability that the current state will move to a new state
#   The probability will be 1/e^((next-cur)/(1-t/lim))
def createProb(cur,next, temp):
    if(cur>next): return 1
    else: return exp(-(next-cur)/temp)

def luyenkim(table,row,col,seq):
    curTable=dupTable(table)
    size=len(table)
    lim=30000
    for t in range(1,lim):
        newTable=dupTable(curTable)
        #Choosing a random position to change
        newRow=int(random.random()*size)
        newCol=int(random.random()*size)
        if(newTable[newRow][newCol]==0):newTable[newRow][newCol]=1
        else: newTable[newRow][newCol]=0
        #Calculate the current cost/errors
        cur_cost=calCost(curTable,row,col)
        if(cur_cost==0):
            return curTable
        #Calculate the next cost/errors
        next_cost=calCost(newTable,row,col)

        if(createProb(cur_cost,next_cost,float(lim-t)/lim)>=random.random()):
            seq.append(newTable)
            curTable=newTable

    return -1


def main(size,col,row):
    generated = []
    while(True):
        newTable=genRandomTable(size)
        seq=[]
        res=luyenkim(newTable,row,col,seq)
        generated.extend(seq)
        if(res!=-1): return generated