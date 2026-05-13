#!/usr/bin/env python3   
import sys   
# Read input line by line   
for line in sys.stdin:   
    line = line.strip()   
    words = line.split()   
    for word in words:   
        print(f'{word}\t1')
        
        
        
'''type input.txt | python mapper.py | sort | python reducer.py'''
        
        
        
        
        
        
        
        
        
        
'''Explain Mapper Line by Line
mapper.py
#!/usr/bin/env python3

Say:

“This line tells the operating system to execute the file using Python 3.”

import sys

Say:

“This imports the sys module which helps us read input from standard input.”

for line in sys.stdin:

Say:

“This reads the input file line by line.”

line = line.strip()

Say:

“This removes extra spaces and newline characters.”

words = line.split()

Say:

“This splits the sentence into individual words.”

Example:

hello world

becomes

['hello', 'world']
for word in words:

Say:

“This loop processes each word one by one.”'''       
        
'''Viva Questions and Answers
1. What is MapReduce?

MapReduce is a programming model used to process large amounts of data in parallel.

2. What are the two phases of MapReduce?
Mapper Phase
Reducer Phase
3. What is the role of Mapper?

Mapper converts input data into key-value pairs.

Example:

hello → 1
4. What is the role of Reducer?

Reducer combines same keys and calculates total count.

Example:

hello → 2
5. Why is sort used between mapper and reducer?

sort groups identical words together so reducer can count them properly.

6. What does sys.stdin mean?

It reads input from standard input (keyboard/file/pipe).

7. Why do we use split()?

To separate words from a sentence.

8. What is key-value pair in this program?

Example:

hello   1
Key = hello
Value = 1
9. What is Hadoop?

Apache Hadoop is an open-source framework used for distributed storage and processing of big data.

10. What is the output of this program?

The output is the frequency/count of each word in the input file.

11. Why do we use Reducer after Mapper?

Mapper only generates data. Reducer performs aggregation and final counting.

12. What happens if sort is not used?

Reducer will not receive grouped words, so counting may become incorrect.'''