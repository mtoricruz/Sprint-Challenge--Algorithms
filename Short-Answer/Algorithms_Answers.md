#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Constant - O(1): The number of operations remains the same no matter how large n gets


b) Linear - O(n): While looping in range of n can mean nothing could happen if n < 1. However
as the bigger n gets, the number of operations will increase based on how many times j will be < n. 


c) Logarithmic - O(logn): Recursive functions mean that every slight increase in input, the number of operations will increase significantly as it moves farther and farther from base case.

## Exercise II
I would use a binary search tree to find which floor the egg will break if dropped from.

Start at the midpoint of the list of floor numbers. If egg breaks from initial midpoint, set new
max to left of midpoint.

If it doesn't break, find new maximum height and set minimum to right of initial midpoint.

Each iteration, move to the side of the BST until a midpoint is found where the egg does not break yet
is right below the max value(floor where egg will break) of the list of floors.

Runtime complexity: O(logn)


