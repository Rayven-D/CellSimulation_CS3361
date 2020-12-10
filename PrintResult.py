import time
def main(exec_time):
    print("Original: ")
    with open('test_file.dat', 'r') as f:
        for line in f:
            print(line, end='')
    print("\n\nAfter 100 steps: ")
    with open("output.out", 'r') as f:
        for line in f:
            print(line, end='')
    print(f"Total execution time of creating output: \n{exec_time} ")

if __name__ == "__main__":
    main(0)