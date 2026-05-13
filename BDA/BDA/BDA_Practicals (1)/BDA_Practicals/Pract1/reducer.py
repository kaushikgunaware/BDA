#!/usr/bin/env python3  
import sys  

current_word = None  
current_count = 0  

# Input comes from standard input  
for line in sys.stdin:  
    word, count = line.strip().split('\t')  
    
    try:  
        count = int(count)  
    except ValueError:  
        continue  
        
    if current_word == word:  
        current_count += count  
    else:  
        if current_word:  
            print(f'{current_word}\t{current_count}')  
        current_word = word  
        current_count = count  
 
# Output the last word  
if current_word:  
    print(f'{current_word}\t{current_count}')
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''Explain Reducer Line by Line
reducer.py
#!/usr/bin/env python3

Say:

“This executes the reducer using Python 3.”

import sys

Say:

“This imports sys module for reading mapper output.”

current_word = None
current_count = 0

Say:

“These variables store the current word and its count.”

for line in sys.stdin:

Say:

“This reads mapper output line by line.”

word, count = line.strip().split('\t')

Say:

“This separates word and count using tab space.”

Example:

hello   1

becomes:

word = hello
count = 1
count = int(count)

Say:

“This converts count from string to integer.”

if current_word == word:

Say:

“This checks whether the same word appears again.”

current_count += count

Say:

“If the word is same, count is increased.”

Example:

hello 1
hello 1

becomes:

hello 2
else:

Say:

“If a new word comes, previous word count is printed.”

print(f'{current_word}\t{current_count}')

Say:

“This prints final count of the previous word.”

current_word = word
current_count = count

Say:

“Now reducer starts counting the new word.”

if current_word:
    print(f'{current_word}\t{current_count}')

Say:

“This prints the last word and its frequency.”'''

'''| Part            | Meaning                    |
| --------------- | -------------------------- |
| `cat input.txt` | Reads input file           |
| `mapper.py`     | Creates key-value pairs    |
| `sort`          | Groups same words together |
| `reducer.py`    | Counts total frequency     |
'''