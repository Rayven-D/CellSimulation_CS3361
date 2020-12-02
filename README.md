# Cell Simulation
### This project is for Concepts of Programming Languages CS3361 

- This project makes use of multiprocessing and other concepts we learned in class. 

><sub>I am running the larger jobs on the High Performance Computing Center(HPCC) at Texas Tech University, in the Quanah cluster.
Throughout this project, apart from the main goal of the project, I have learned to use Quanah, as well as request jobs by creating my own testing **shell scripts**.

### How to run:
    
```
python RayvenJan_Deray_R11558709_final_project.py -i <input_file_name> -o <output_file_name> [ -t <number_of_threads/processes>]
```
<sub>Input `-i` and ouput `-o` are required. Default thread count is `1`

### Current Times <sub><sup>`in seconds`:
```
    100x100 array
	1   thread:		3.772849668
	2   threads:		1.299805564 
	4   threads:		.925376691 
	8   threads:		.615411383 
	16  threads:		.650742211 
	32  threads:		.797888589 

    1000x1000 array
	1   thread:		194.638022486 
	2   threads:		108.095379187 
	4   threads:		61.740447382 
	8   threads:		37.819331245 
	16  threads:		21.854849613 
	32  threads:		18.995629146 

    10000x10000 array
	9   threads:	    	2780.860638662 
	18  threads:	    	1658.370904022 
	36  threads:	    	1086.316807469 

    Wall-Clock Time: ~ 1h 40m
```


<br/>

## Description 
>The cell simulation will go through 100 steps, and during each step, each cell is evaluated against its neighbors to determine if the cell is alive or dead.

Cell States:

- Dead:  &nbsp; .
- Alive: &nbsp; O

&nbsp;

Cell Neighbors:

<sub><sup>C is the current cell <br> X are the neighboring cells</sub></sup>

### &nbsp;&nbsp;&nbsp;&nbsp;XXX<br>
### &nbsp;&nbsp;&nbsp;&nbsp;XCX<br>
### &nbsp;&nbsp;&nbsp;&nbsp;XXX

&nbsp;

Determining Factors:

- Alive cell stays alive if:

    - Has 2 - 4 `alive` neighbors
- Dead cell becomes alive if:

    - Has an positive non-zero even number of `alive` neighbors

- Otherwise:

    - The cell `dies`

&nbsp;

Example:

```
Starting Colony:
    ........O..OO...O.................O.OO...
    ..O............O..O.O..OO...............
    .......O.......O.....O...........O...OO.
    ....O..O.........O......O.............O.
    ........O.....O.O......O.......O........
    .......O.....O..........................
    .O...........O............O.......OO.O..
    ..O....O...O....OO......................
    .O.O...........O................O.......    
    O..........O.........O.............O....
    ......O........O.......O..........O.....
    ..OO..............O.........O...O.O...O.
    .....OO.O..O.O.....O.O..................
    O........O....OO.....O.....OO.O.........
    O............O............O..O......O...
    ...OO.......O...............O.........O.
    O.............O............O.........O..
    .........O.....O..............O...O.....
    ........................................
    .O........O...............O......O.O....


After 100 Steps:
    OOOOOOO.O..OOOO..OOO..OOOOOOOO...O...OOO
    .OO.OO.OOO.OO.OOO.OO..OOO...O.OO.OO..O..
    ....OOO..OOOOOO.......OOOO.......O...OO.
    .OOO..OO.....OO.......O.OO.O....OOOOOO..
    ..O..OOOOOO.O.OO...OOO..O.OOO..O..OO.O..
    ..O...O.O.O.O.OOO...O..OO.OO...OO...OO..
    OOO.O...OOO....OOOOOO..O.OO...OO..OOOO.O
    ..........O.OO..OO...O..OOOO.O....OOOOOO
    OOOO.O.OOOO.OOOOO.O.....O.OO..O...OOO.OO
    O..OO..OO.OOOOOO.O...OO.OOO..OO..O.O....
    OO.....OO..OOOOOOOO...O......O.OOO.OO...
    OO..OOOOOO.OOO.O.OO....O..O..OO....O.OO.
    OO.OO..O.OOOO.OOOOO...OOOOO..OO....OO..O
    .O..OO.OOO..O.O...O....OO...OO....O.O...
    O.O.O.OOO..OO..OO.O.O.O.OOOO.OO...OO...O
    .O...OOOO.OO..OO...O.OO.OOOO........O..O
    OOOOO...OO.OO.....OO..O.OO......OOOO....
    .OO.O..OO.OO.O.O.OOO....OOO.....OOOO....
    O.OOO.O...O.OOO..OOO...O.O.O....O.OOO...
    OO.OOO.O..O.OOOOO..O..OOOOOO.....O.O.O..
```

### Compare .py
>   Compares two input files to check if the files are *exactly* the same
```
python compare.py <file1> <file2>
```

### CreateTestFile .py
>   Creates a test file from specified inputs. Supports multithreading
```
python CreateTestFile.py <number_rows> <number_columns> <number_threads>
```
<sub><sup>All 3 inputs are required
