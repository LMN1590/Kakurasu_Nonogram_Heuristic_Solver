import BestFSKakurasu,BFSKakurasu
import tracemalloc
size = 4
test = 500
total = [0,0]
for i in range(test):
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
    
    print(i+1)
    tracemalloc.start()
    BFSKakurasu.main(size,col_run,row_run)
    total[0] += tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
    tracemalloc.start()
    BestFSKakurasu.main(size,col_run,row_run)
    total[1] += tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()
print(total[0]/test)
print(total[1]/test)