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

######################
#Helper Function

##dupTable is used to duplpicate the matrix that represent the table
def dupTable(base):
    newer=[]
    for i in base:
        newer.append(list(i))
    return newer

##Function check is used to determine whether the table has reached goal state.
def check(row,col):
    for i in row:
        if(i!=0):
            return False
    for i in col:
        if(i!=0):
            return False
    return True

##Function newNext is used to create a new list which represent the next position to be checked.
def newNext(cur,size):
    if(cur[1]==size-1):
        if(cur[0]==size-1): return [-1,-1]
        else:
            return [cur[0]+1,0]
    else:
        return [cur[0],cur[1]+1]


def mark(item1,temp):
    item1.base[temp.cur[0]][temp.cur[1]]=1
    item1.col[temp.cur[0]]=item1.col[temp.cur[0]]-(temp.cur[1]+1)
    item1.row[temp.cur[1]]=item1.row[temp.cur[1]]-(temp.cur[0]+1)


def createStep(res,seq):
    if(res.prev!=[[]]):
        createStep(res.prev,seq)
    seq.append(res.base)
######################
#### Main ####
#Read Input
def main(size,col,row):
    #Init queue for BFS
    init=Item([[0]*size for i in range(size)],[0,0],list(col),list(row),[[]])
    queue=[init]
    found=False
    res=[[]]

    generated=[]
    while(len(queue)):
        temp=queue[0]
        queue.pop(0)
        generated.append(temp.base)
        nextPos=newNext(temp.cur,size)
        found=check(temp.row,temp.col)
        
        if(found):
            res=temp
            break

        if(temp.cur[0]==-1): continue
        queue.append(Item(dupTable(temp.base),nextPos,list(temp.col),list(temp.row),temp))
        curCol=list(temp.col)
        curRow=list(temp.row)
        if(curRow[temp.cur[1]]>=temp.cur[0]+1 and curCol[temp.cur[0]]>=temp.cur[1]+1):
            newTable=dupTable(temp.base)
            newItem=Item(newTable,list(nextPos),curCol,curRow,temp)
            mark(newItem, temp)
            #The new item is updated and valid to be printed
            queue.append(newItem)
    seq=[]
    if(res!=[[]]): createStep(res,seq)
    return seq,generated