# B-VZXR
B-VZXR is a robot living in a predefined 2-dimensional space called universe. 
This project implements a Python script that initializes the robot's position, moves it in its universe by reading a list of instructions while plotting its successive positions and returns its final position.

The universe of the robot is defined by a width and a height stored in the universe.txt file:
```
width: 120
height: 100
```
The instructions are defined in the instructions_list.txt file:
```
right, 6
left, 10
left, 8
left, 1
right, 7
...
```
The robot's initial position is (0, 0). By reading the first instruction, the robot has to pivot to the right by 90° and move by 6 units: its position is now (6, 0). When reading the second instruction, the robot has to pivot to the left by 90° and move by 10 units from its current position: its position will be (6, 10). And so on until the instructions end. If the robot encounters the universe bounds, it must stop moving and go on to the next instruction.

## Requirements
Pior to running `get_final_position.py`, run the following command in a terminal to install the required packages:
```
pip install -r requirements.txt
```
## Execution
You can run the script by running the following command in a terminal:
```
python3 get_final_position.py
```
## Expected outputs
While the script runs, the successive positions of the robot are plotted on a matplotlib scatterplot. 
![bvzxr_screenshot](https://github.com/oli2v/b-vzxr/assets/25934512/def1636f-9b10-4263-8820-87991ffe63f6)

When the program ends, it should output the robot's final position like so:
```
The final (x, y) position of B-VZXR is (45, 84)
```

## Author
[Olivier Valenduc](https://github.com/oli2v)
