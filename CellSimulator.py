import multiprocessing as mp
import CreateTestFile
import PrintResult
import time

array = []
rows = 0
cols = 0

#Reads in the lines of the input file
#   and puts it in an array.
#Each line is being processed by their own process
def readLines(line):
    line = line.strip()
    return list(line)

#Prepares the Matrix to be processed
#  Get's the row to work on, and surrounds it with the row before and after
#   so that each process only takes on 3 rows at atime
def processMatrix(matrix):
    poolData = list()
    for row in range(rows):
        m = [matrix[(row-1)%rows], matrix[row], matrix[(row+1)%rows]] #[<row_prev>, <working_row>, <row_next>]
        poolData.append(m)
    del(matrix)
    return poolData

#Process the row of the matrix
#Index 1 is the row we will modify
#Index 0 and 2 are the neighboring rows of the modifying row
#   that are needed to change the current working row
def time_step(x):
    global cols
    global array
    array = x
    cols = len(array[0])
    array2 = list()
    for y in range(cols):    
        array2.append(check_neighbors(array[1][y], y))

    return array2

#The same as time_step() function wise
#However, instead of returning an array, it returns a string to the map
#   where each string is a row of the final result
#   after 100 steps. Each row is followed by a \n character
def final_step(x):
    global cols
    global array
    array = x
    cols = len(array[0])
    array2 = ""
    for y in range(cols):    
        array2 += check_neighbors(array[1][y], y)
    array2 = array2 + "\n"
    return array2

#Checks the current element against its neighbors
#   to determine if it is alive or dead
def check_neighbors(cur_cell, y_pos):
    neighbors_array = [0,0,0,0,0,0,0,0] 
    y_prev = (y_pos-1)%cols
    y_next = (y_pos+1)%cols
    neighbors_array[0] = array[0][ y_prev]
    neighbors_array[1] = array[0][(y_pos)]
    neighbors_array[2] = array[0][ y_next]
    neighbors_array[3] = array[1][y_prev]
    neighbors_array[4] = array[1][y_next]
    neighbors_array[5] = array[2][y_prev]
    neighbors_array[6] = array[2][(y_pos)]
    neighbors_array[7] = array[2][y_next]


    alive_neighbors = neighbors_array.count('O')
    char_val = '.'

    if cur_cell == 'O' and 2 <= alive_neighbors <= 4:
        char_val = 'O'
    elif cur_cell == '.'and alive_neighbors % 2 == 0 and alive_neighbors > 0 :
        char_val = 'O'
    return char_val


def main():
    CreateTestFile.main()
    global array
    global rows
    start = time.time()
    
    num_threads = 1
    correct_input = False
    while not correct_input:
        try:
            num_threads = int(input("Enter number of processes to spawn: "))
            correct_input = True
        except Exception:
            print("Incorrect Input")

    pool = mp.Pool(processes=num_threads)

    try:
        with open("test_file.dat") as f:
            array = pool.map(readLines, f)


    except IOError:
        print("COULD NOT READ FILE")
        exit(4)


    rows = len(array)

    tempArray = processMatrix(array) 
    for _ in range(99):
        tempArray = pool.map(time_step, tempArray)
        tempArray = processMatrix(tempArray)

    tempArray = pool.map(final_step, tempArray) #the 100th step
    fullString = ''.join(tempArray)#joins the whole array into a string



    try:
        with open("output.out", 'w') as f:
            f.write(fullString)
            
            
    except IOError:
        print("COULD NOT CREATE FILE")
        exit(5)
    end = time.time()
    print("\nTotal execution time:: ")
    print(end-start)
    PrintResult.main(end-start)
    exit(0)

if __name__ == "__main__":
   
    main()