import random

def main():


    correct_input = False
    while not correct_input:
        try: 
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if( 10 <= rows <= 100 and 10 <= cols <= 100):
                correct_input = True
            else:
                print("Please enter numbers between 10 and 100")
        except Exception:
            print("Please enter a integer number.")
    temp_str = ""
    for x in range(rows):
        for y in range(cols):
            temp_str += 'O' if random.randint(0,1) == 0 else '.'
        temp_str += "\n"


    output_file = "test_file.dat"
    with open(output_file,'w') as f:
        f.write(temp_str)
    print(f"Successfully created file with {rows} x {cols} cells.")

if __name__ == '__main__':
    main()