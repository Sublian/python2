"""HackerRank Task
You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

Input Format
A single line of input containing  space separated integers.

Output Format
Print the X NumPy array.

Sample Input
1 2 3 4 5 6 7 8 9

Sample Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

import numpy

lst=list(map(int,input().split()))
array=numpy.array(lst)
print(numpy.reshape(array,(3,3)))