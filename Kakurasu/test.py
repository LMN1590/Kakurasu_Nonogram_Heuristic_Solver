import BestFSKakurasu,BFSKakurasu
import random, time
size = 5
total = [0,0]
for i in range(500):
    import numpy as np
    test_row=np.random.randint(0,2,(size,size))
    col_run, row_run = [], []
    for run in range(size):
        col_run.append(0)
        row_run.append(0)
    for row in range(size):
        for col in range(size):
            if test_row[row][col] == 1:
                col_run[col]+=(row+1)
                row_run[row]+=(col+1)
    print(col_run)
    print(row_run)
    start = time.time()
    BFSKakurasu.main(size,col_run,row_run)
    stop = time.time()
    total[0] += stop - start
    start = time.time()
    BestFSKakurasu.main(size,col_run,row_run)
    stop = time.time()
    total[1] += stop - start
    print(i+1)
print(total[0]/500)
print(total[1]/500)