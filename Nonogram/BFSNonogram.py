import numpy as np
class Item:
    def __init__(self,table,cur,prev):
        self.base=table
        self.cur=cur
        self.prev=prev

def check(row,col,size,matrix):
    for i in range(size):
        temp_list=[]
        temp=0
        for j in range(size):
            if(matrix[i][j]==0):
                if(temp!=0):
                    temp_list.append(temp)
                    temp=0
            else: temp+=matrix[i][j]
        if(temp!=0): temp_list.append(temp)
        if(temp_list!=col[i]): return False
        
        temp_list=[]
        temp=0
        for j in range(size):
            if(matrix[j][i]==0):
                if(temp!=0): 
                    temp_list.append(temp)
                    temp=0
            else: temp+=matrix[j][i]
        if(temp!=0): temp_list.append(temp)
        if(temp_list!=row[i]): return False
    return True
 
def valid (matrix, row,size):
    check_list=[]
    for i in range(0,size):
        temp_list=[]
        temp=0
        for j in range(0,size):
            if(matrix[j][i]==0):
                if(temp!=0):
                    temp_list.append(temp)
                    temp=0
            else: 
                temp+=matrix[j][i]
        if(temp!=0): temp_list.append(temp)
        check_list.append(temp_list)
    for i in range(0,size):
        temp=check_list[i]
        for j in range(0,len(temp)):
            if(j>=len(row[i])): return False
            if(row[i][j] < temp[j]): return False

    return True

def gen_row(w, s):
    ''' w=size, s=row'''
    """Create all patterns of a row or col that match given runs."""
    def gen_seg(o, sp):
        if not o:
            return [[0] * sp]
        return [[0] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]
 
    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]

def DFS(row,col,size):
    init=Item(np.full((size,size),0),0,[[]])
    stack=[init]
    res=init
    state_list=[]
    generated=[]
    for i in range(size):
        temp=gen_row(size,col[i])
        state_list.append(temp)
    while(len(stack)):
        temp=stack[-1]
        stack.pop()
        nextPos=temp.cur+1
        if(check(row,col,size,temp.base)):
            res=temp
            break

        if(temp.cur==size): continue
        temp_list=state_list[nextPos-1]
        for i in temp_list:
            new_item=list(temp.base)
            new_item[nextPos-1]=i
            new_item=np.array(new_item)
            if(nextPos-1==0 or valid(new_item,row,size)):
                stack.append(Item(new_item.copy(),nextPos,temp.base.copy()))

    return res

size=10
row=[[4,3],[2,1,3],[8],[3,3],[3,1],[2],[1,1,2],[1,4],[1,3],[1,1,2]]
col=[[2,2,3],[7],[1,3,1],[4],[1],[3],[5,4],[4,3],[1,1,3],[2]]
x=DFS(row,col,size).base
print(x)