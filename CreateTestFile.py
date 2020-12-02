import sys
import random
import threading
import time

rows = 1
cols = 1
num_threads = 1
output_string = ""

def create_string(y, lock):
    global output_string
    global num_threads, cols
    
    temp_string = ""
    while y < cols:
        temp_string += 'O' if random.randint(0,1) == 0 else '.'
        y += 1
    temp_string += "\n"
    lock.acquire()
    output_string += temp_string
    lock.release()

def main():
    global output_string
    global num_threads, cols
    start = time.time()
    if(len(sys.argv) == 4):
        rows  = int(sys.argv[1])
        cols = int(sys.argv[2])
        num_threads = int(sys.argv[3])

    for x in range(rows % num_threads):
        temp_str = ""
        for y in range(cols):
            temp_str += 'O' if random.randint(0,1) == 0 else '.'
        temp_str += "\n"
        output_string += temp_str

    threads = []
    lock = threading.Lock()

    for x in range(rows - (rows%num_threads)):
        t = threading.Thread(target=create_string, args=(0,lock,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    output_file = "test_" + str(rows) + 'x' + str(cols) + "_step_0.dat"
    with open(output_file,'w') as f:
        f.write(output_string)
    end = time.time()
    print("Total runtime: ")
    print(end-start)

if __name__ == '__main__':
    main()