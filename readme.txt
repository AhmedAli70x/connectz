Before writing the code for connectz, I start reading around it to help understand the task. I divided the program into function blocks where I can program and test each function individually. The program comprises 14 functions. The program tests the submitted file for the error (4 -9) and before processing it and checking the valid game state (0-4).

The codes are defined as follows:
Code:Reason
0:Draw
1:Win for player 1
2:Win for player 2
3:Incomplete
4:Illegal continue
5:Illegal row
6:Illegal column
7:Illegal game
8:Invalid file
9:File error

connectZ:
* requirements: the script will run natively without the need to install any external libraries
* The program takes 2 parameters when running: Python connectz.py(parameter1) and file path  (parameter2), if the programing takes one parameter, it asks for the file to apply the script.

If the file path exists, the program checks the first line only and checks if the board parameters are valid. If they are valid, the program reads the rest of the moves and checkss them for illegal row, column and game. The first line should have the numbersfor 3 parameters needed to check the connectz game. First parameter represents number of the rows(x), second parapmet represent numberof the row(y), and third parameter represnt the number of valid moves to win(z)

The most challenging part is finding out who wins the game player 1 or player 2. The check- function is triggered after each play it check_win vertical to the last move. If false, check horizontally. If false, check diagonally. This function could be improved for a better search technique.
