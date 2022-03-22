import BestFSKakurasu,BFSKakurasu
import random, time
size = 4
total = [0,0]
for i in range(500):
    test_row = []
    for row in range(size):
        test_col = []
        for col in range(size):
            test_col.append(random.choice([True, False]))
        test_row.append(test_col)
    col_run, row_run = [], []
    for run in range(size):
        col_run.append(0)
        row_run.append(0)
    for row in range(size):
        for col in range(size):
            if test_row[row][col] == True:
                col_run[col]+=(col+1)*(row+1)
                row_run[row]+=(col+1)*(row+1)
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