#Declaration of class Item
#   base: the matrix representing the table
#   cur: the current position that is branching into 2 scenarios: marked and unmarked
#   row: the target row: from left to right
#   col: the target column from top to bottom
#   prev: the previous state
class Item:
    def __init__(self,table,cur,col,row,prev):
        self.base=list(table)
        self.cur=cur
        self.row=row
        self.col=col
        self.prev=prev

#getPos: Get the new index of the next diagonal line whose sum of row and column equals to bestChoice
def getPos(bestChoice,size):
    if(bestChoice<0): return [-1,-1]
    row=min(bestChoice,size-1)
    col=bestChoice-row
    return [row,col]

#validPos: Check if curPosition is a valid position concerning the size
def validPos(curPosition,size):
    if(curPosition[0]>=size or curPosition[0]<0):return False
    if(curPosition[1]>=size or curPosition[1]<0):return False
    return True

#Copying a two-dimensional matrix, base
def dupTable(base):
    newer=[]
    for i in base:
        newer.append(list(i))
    return newer

#check: Check to see an Item has reached the goal state
def check(row,col):
    for i in row:
        if(i!=0):
            return False
    for i in col:
        if(i!=0):
            return False
    return True

def mark(item1,temp):
    item1.base[temp.cur[0]][temp.cur[1]]=1
    item1.col[temp.cur[0]]=item1.col[temp.cur[0]]-(temp.cur[1]+1)
    item1.row[temp.cur[1]]=item1.row[temp.cur[1]]-(temp.cur[0]+1)

def createStep(res,seq):
    if(res.prev!=[[]]):
        createStep(res.prev,seq)
    seq.append(res.base)

#Input
def main(size,col,row):
    #Sum array used for checking the end condition, whether the remaining unchecked slots can be added up to the target
    sum_array=[0]
    for i in range(size-1):
        sum_array.append(sum_array[-1]+i+1)

    #Basic Variable
    bestChoice=(size-1)*2
    init=Item([[0]*size for i in range(size)],getPos(bestChoice,size),list(col),list(row),[[]])
    queue=[init]
    res=[[]]

    #Best First Search
    #Heuristic Function: The sum of the remaining number on array col and row
    #The Item with lower value will be prioritized
    #Therefore, the index from bottom right will be checked first
    #   (as checking it means that the maximum substraction from the sum is achieved) 
    #   and moving toward the top left position.

    #When examining a position, two branch will be created, one where it is a 0 and one where it is a 1
    #The branch with a 1 will be examined next as it has a lower overall sum.
    #However, when choosing between two branch with equal sum, the one with more positions checked will be chosen.
    #    as it will be closer to the final result.
    generated=[]
    while(len(queue)):
        #Getting the next position
        currentItem=queue[-1]
        queue.pop()
        generated.append(currentItem.base)
        #Check for goal state
        if(check(currentItem.row,currentItem.col)):
            res=currentItem
            break

        #Check for invalid position, signalling no more branch can be created
        if(currentItem.cur[0]==-1): continue

        #Getting next position
        nextPos=[currentItem.cur[0]-1,currentItem.cur[1]+1]
        if(not validPos(nextPos,size)):
            bestChoice=currentItem.cur[0]+currentItem.cur[1]-1
            nextPos=getPos(bestChoice,size)
        
        #Creating the branch where the position is marked with a 0 and appending it to the end. 
        #   If the remaining number can't add up to the target of its row or column, it is abandoned.
        if((currentItem.row[currentItem.cur[1]] <= sum_array[currentItem.cur[0]]) and (currentItem.col[currentItem.cur[0]] <= sum_array[currentItem.cur[1]])):
            newTable=dupTable(currentItem.base)
            queue.append(Item(newTable,nextPos,list(currentItem.col),list(currentItem.row),currentItem))

        #Creating the branch where the position is marked with a 1 and appending it to the end. 
        #   If the sum of its row/column exceed the target, it is abandoned.
        if((currentItem.row[currentItem.cur[1]] >= currentItem.cur[0]+1) and (currentItem.col[currentItem.cur[0]] >= currentItem.cur[1]+1)):
            newTable=dupTable(currentItem.base)
            curCol=list(currentItem.col)
            curRow=list(currentItem.row)
            newItem=Item(newTable,nextPos,curCol,curRow,currentItem)
            mark(newItem,currentItem)
            #newItem is updated and can be printed
            queue.append(newItem)
    seq=[]
    if(res!=[[]]): createStep(res,seq)
    return seq,generated