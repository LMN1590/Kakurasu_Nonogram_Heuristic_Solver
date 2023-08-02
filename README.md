# AI_Assignment1

Overviewe of assignment 1 of course Introduction to Artificial Intelligence, HCMUT.

## Heuristic Solution for Kakurasu and Nonogram game
### Nonogram
- Simulated Aneealing:
  + Generate a random table
  + Changing one element in the table
  + Calculate the new cost
  + If it is smaller then use the new table. If the cost is bigger then there is a chance that the new table will be used. This chance will deteriorate as more steps are done.
- Blind DFS:
  + For every row in the table, generate every possible situation of that row, concerning the constraint
  + Using a queue, all the possible rows will be stacked on top of each other until one valid solution is found.

### Kakurasu
- Blind BFS:
  + From the position \(1,1\), every position will have two posible values, 0 or 1. Every combination will be generated and checked against the constraint.
- BestFS:
  + Instead of going from the top-left position, the program starts from bottom-right position since it has the most impact on the constraint.
  + Check the 0 situation first, in order to order the queue in best-value-first order. If the constraint on either the row or column is too big for the remaining element to fulfill then it is discarded. Otherwise, it is added to the queue.
  + Check the 1 situation for the element, if it is bigger than the constraint then it is discarded. Otherwise, it is added to the queue. 
