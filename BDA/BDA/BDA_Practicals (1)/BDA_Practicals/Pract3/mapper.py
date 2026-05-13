import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        name, marks = line.split(',')
        print(f"{name}\t{marks}")
        
        
        
        
        '''PS C:\BDA\BDA_Practicals (1)\BDA_Practicals\Pract3> type input.txt | python mapper.py | sort | python reducer.py'''
        
'''1. mapper.py Explanation
import sys
Imports the sys module.
sys.stdin is used to read input from the terminal or Hadoop stream.
for line in sys.stdin:
Reads the input file line by line.

Example line:

alice,85
    line = line.strip()
Removes extra spaces and newline characters (\n).

Converts:

alice,85\n

into:

alice,85
    if line:
Checks whether the line is empty or not.
Prevents errors from blank lines.
        name, marks = line.split(',')
Splits the line using comma ,.

Example:

"alice,85".split(',')

becomes:

name = "alice"
marks = "85"
        print(f"{name}\t{marks}")
Prints output in key-value format separated by tab (\t).

Mapper output:

alice    85
bob      67
Here:
Key → Student Name
Value → Marks'''