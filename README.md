# Heuristic-Method-1--HM-1-
 A method for solving Transportation Problem

Heuristic Method 1 Algorithm
Step 1: Calculate the difference between the two lowest costs cell (called Penalty) for each row and column. These are called as row and column penalties, P, respectively.
Step 2: Add the cost of cell for each row and column. These summations are called row and column cost, T, respectively.
Step 3: Compute the product of penalty P and the total cost T, that is PT for each row and column.
Step 4: Identify the row/column having lowest PT.
Step 5: Choose the cell having minimum cost in row/column identified in Step-4.
Step 6: Make maximum feasible allocation to the cell choosing in Step 5, if the cost of this cell is also minimum in it's row/column. Otherwise allocation is avoided and go to step-7.
Step 7: Identify the row/column having next to lowest PT.
Step 8: Choose the cell having minimum cost in row/column identified in Step 7.
Step 9: Make maximum feasible allocation to the cell choosen in Step 8.
Step 10: Cross out the satisfied row/column.
Step 11: Repeat the procedure until all the requirements are satisfied.

Source: http://cbom.atozmath.com/example/CBOM/Transportation.aspx?he=e&q=h1
