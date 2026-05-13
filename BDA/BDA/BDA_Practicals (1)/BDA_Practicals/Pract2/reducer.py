import sys
from collections import defaultdict

# Fixed variable naming (removed spaces)
current_key = None
A_vals = defaultdict(float)
B_vals = defaultdict(float)

for line in sys.stdin:
    # Added missing '='
    key, value = line.strip().split('\t')
    matrix, index, val = value.split(',')
    
    if current_key and current_key != key:
        # Added missing '=' and '*' operator
        result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
        print(f"{current_key}\t{result}")
        
        # Fixed variable names
        A_vals.clear()
        B_vals.clear()
        
    current_key = key
    
    if matrix == 'A':
        A_vals[index] = float(val)
    else:
        # Fixed fragmented lines and missing assignment
        B_vals[index] = float(val)

# Output the last key
if current_key:
    # Fixed typos ('fork', 'kin') and missing operators
    result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
    print(f"{current_key}\t{result}")
    
    
    
    
    
    '''Reducer Code Explanation
Reducer performs actual multiplication and addition.

import sysfrom collections import defaultdict
Explanation


sys → reads mapper output


defaultdict → stores matrix values easily



current_key = NoneA_vals = defaultdict(float)B_vals = defaultdict(float)
Explanation


current_key
→ stores current matrix position


A_vals
→ stores A matrix values


B_vals
→ stores B matrix values



for line in sys.stdin:
Reads mapper output line by line.

key, value = line.strip().split('\t')
Separates key and value.
Example:
0,0    A,1,2
becomes:


key = 0,0


value = A,1,2



matrix, index, val = value.split(',')
Separates:


Matrix name


Index


Value



Key Change Logic
if current_key and current_key != key:
When reducer gets a new key:


calculate previous matrix position result


print output



Matrix Multiplication Formula
Reducer calculates:
Cij=∑kAikBkjC_{ij}=\sum_{k}A_{ik}B_{kj}Cij​=∑k​Aik​Bkj​

result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
Explanation
This performs:
(Aik×Bkj)(A_{ik} \times B_{kj})(Aik​×Bkj​)
and adds all values.

print(f"{current_key}\t{result}")
Prints final result.
Example:
0,0    17

Final Output Calculation
For position (0,0):
(1×5)+(2×6)=17(1\times5)+(2\times6)=17(1×5)+(2×6)=17
For position (0,1):
(1×7)+(2×8)=23(1\times7)+(2\times8)=23(1×7)+(2×8)=23
For position (1,0):
(3×5)+(4×6)=39(3\times5)+(4\times6)=39(3×5)+(4×6)=39
For position (1,1):
(3×7)+(4×8)=53(3\times7)+(4\times8)=53(3×7)+(4×8)=53

Final Output Matrix
[17233953]\begin{bmatrix}
17 & 23 \\
39 & 53
\end{bmatrix}[1739​2353​]

Short Viva Explanation
You can say:

“In this practical, I implemented matrix multiplication using MapReduce.
The mapper distributes matrix elements based on output positions, and the reducer performs multiplication and summation to generate the final matrix.
Mapper handles data mapping, while reducer computes the final matrix values.”
'''



'''Matrix Multiplication Logic

For matrix multiplication:

C
ij
	​

=∑
k
	​

A
ik
	​

B
kj
	​


This means:

Multiply corresponding elements
Then add the results
Example for Position (0,0)

Reducer calculates value at output position (0,0).

From matrices:

A=[
1
3
	​

2
4
	​

]
B=[
5
6
	​

7
8
	​

]

For (0,0):

Take:

Row 0 from A → (1,2)
Column 0 from B → (5,6)

Multiply:

(1×5)+(2×6)

Then add:

5+12=17

So:

0,0    17
Example for Position (0,1)

Take:

Row 0 from A → (1,2)
Column 1 from B → (7,8)

Multiply and add:

(1×7)+(2×8)=23'''


'''In Ubuntu, you use cat instead of type.

Run this command in terminal:

cat input.txt | python3 mapper.py | sort | python3 reducer.py
Step-by-Step in Ubuntu
1. Open Terminal

Press:

Ctrl + Alt + T
2. Go to Your Folder

Example:

cd ~/Documents

or where your files are stored.

3. Check Files

Run:

ls

You should see:

input.txt
mapper.py
reducer.py
4. Give Execute Permission (Optional)
chmod +x mapper.py reducer.py
5. Run the Program
cat input.txt | python3 mapper.py | sort | python3 reducer.py'''