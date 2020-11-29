# Sudoku
This is a python program that one can use to play the classic puzzle game, Sudoku. It displays a 9x9 board with 30 empty cells that the player needs to fill in. 

The program begins by creating a blank board. A random number is placed in the first row in a random cell. Then, a solution is created using a backtracking algorithm given this one cell. Another board is copied from this solution board except with 30 empty cells. This ensures a solution exists. 
