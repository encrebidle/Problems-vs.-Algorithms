#Problem Explanation Done 8:55 pm 30/05/20 , working for continuous from 11 am .
## Problem 1
The idea is to find the largest integer i whose square is less than or equal to the given number. The idea is to use Binary Search to solve the problem. The values of i * i is monotonically increasing, so the problem can be solved using binary search.
Complexity Analysis:
Time complexity: O(log n).
The time complexity of binary search is O(log n).
Space Complexity: O(1).
Constant extra space is needed.
## Problem 2
The idea is to find the pivot point, divide the array in two sub-arrays and call binary search.
The main idea for finding pivot is – for a sorted (in increasing order) and pivoted array, pivot element is the only element for which next element to it is smaller than it. Using above criteria and binary search I got pivot element in O(logn) time.
As for the space complexity, it is independent of the input, requiring pointers to different array locations; O(1).
Time Complexity O(logn).
Space complexity O(1)

## Problem 3
To rearrange a list of digits into two large numbers I first reverse quick sort the list. Quick sort time complexity is O(n log(n))
The time complexity is O(n+ n log(n)) , which simplifies to O(n log(n)) ,Just sort it and then apply the pattern iterating the array in reverse. 
The space complexity of quick sort is O(logn) i.e quicksort recursive stacl.

## Problem 4
Space complexity is O(1) since only a few variables are used to keep track of indexes, and sorting is done in place. 
Time complexity is O(n) since we must iterate through each item of the array to determine whether to send a 0 to the front or a 2 to the back.
Time Complexity O(n)
Space O(1)

## Problem 5 
"""Autocomplete with Tries
>Please complete the notebook for this project problem and download it for your submission."""
I already submitted the .pynb file , now I've done the .py for the same .
The time complexity is O(n), since to find all the suffixes, we have to traverse all nodes in the tree.
Space complexity is O(1)

## Problem 6
Traversing the array of ints has a time complexity of O(n) and a space complexity of O(1). 
We iterate through each number in a list of integers, and we set two variables, min and max, which we will update as check the min and max of each no. If the current number is larger than the max, it becomes the new max.
Similarly, if the current number is less than the min, it becomes the new min.

## Problem 7
The time and space complexity is negligible for our Route Trie. This is because a url will never be longer than a few hundred characters at most.
the block of code - 
        for path in paths:
            if path not in node.children:
            
determines the complexity of the insert/lookup function used. Complexity: O(n * m) where n is the length word and m is the average of trienodes encountered down the trie.
this is because the operation element in list|dict|set as a worst case complexity of O(n) .