# Efficient (Fast) Algorithm

In this directory I provide the solution for the *batch paint optimizer*
problem by implementing a backtracking algorithm.

The structure of the problem does not simply allow a polynomial time 
solution for the worst case scenario. 

I modelled the problem as an optimization research problem as follows:

![model](http://latex2png.com/output//latex_1b48cb37b6819a6d899274f8184dcfcb.png)   

 
where *matte* and *glossy* are two binary indicator vectors, 
*MPref* and *GPref* are two separate matrix that indicate the binary 
preference for matte and glossy respectively.

The model tells us that the solution has to have the minimum number of matte colors subject to the satisfaction of at least one preference for each customer.
Furthermore, it tells us that each color can be either matte or glossy. 


The problem can be reduced to a **constraint satisfaction problem** 
which can be solved with a backtracting algorithm.   
Constraint Satisfaction Problem are in NP, therefore 
the worst case solution is always exponential. 
However, working with backtracking allows for incrementally 
build a candidate solution and abandon a candidate "backtrack" 
as soon as it determines that the candidate cannot possibly be completed to a valid solution. 