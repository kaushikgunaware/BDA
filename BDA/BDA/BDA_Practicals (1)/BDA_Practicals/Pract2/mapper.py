#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Removed the extra spaces and added the missing '='
    tokens = line.strip().split(',')
    
    if tokens[0] == 'A':
        for k in range(0, 2): # assuming output matrix has 2 columns
            # Fixed spacing
            print(f"{tokens[1]},{k}\tA,{tokens[2]},{tokens[3]}")
            
    elif tokens[0] == 'B':
        for i in range(0, 2): # assuming output matrix has 2 rows
            # Added missing closing bracket for tokens[1]
            print(f"{i},{tokens[2]}\tB,{tokens[1]},{tokens[3]}")
            
            
            
'''Mapper Code Explanation

Your mapper distributes matrix values so reducer can calculate multiplication.

#!/usr/bin/env python3
import sys
Explanation
#!/usr/bin/env python3
→ tells Hadoop to run using Python 3
import sys
→ used to read input from standard input
for line in sys.stdin:
Explanation

Reads input line by line from Hadoop.

tokens = line.strip().split(',')
Explanation
strip() removes spaces/new line
split(',') separates values using comma

Example:

A,0,1,2

becomes

['A','0','1','2']
Mapper for Matrix A
if tokens[0] == 'A':

Checks whether current element belongs to Matrix A.

for k in range(0, 2):

Loop runs for all columns of output matrix.

Since output matrix is 2×2, loop runs 2 times.

print(f"{tokens[1]},{k}\tA,{tokens[2]},{tokens[3]}")
Explanation

Mapper emits:

key        value

Example output:

0,0    A,1,2

Meaning:

Output position = (0,0)
Matrix A column index = 1
Value = 2
Mapper for Matrix B
elif tokens[0] == 'B':

Checks whether element belongs to Matrix B.

for i in range(0, 2):

Runs for all rows of output matrix.

print(f"{i},{tokens[2]}\tB,{tokens[1]},{tokens[3]}")
Explanation

Example output:

0,1    B,0,7

Meaning:

Output position = (0,1)
Matrix B row index = 0
Value = 7'''

'''type input.txt | python mapper.py | sort | python reducer.py'''