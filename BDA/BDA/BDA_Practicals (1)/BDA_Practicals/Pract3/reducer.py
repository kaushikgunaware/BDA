import sys

for line in sys.stdin:
    name, marks = line.strip().split('\t')
    marks = int(marks)
    
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print(f"{name}\t{grade}")

    
    '''“The mapper reads student data from the input file and separates student 
    name and marks using comma delimiter. It sends the data in key-value format
    to the reducer. The reducer receives marks, converts them into integer values,
    checks grading conditions
    using if-elif statements, assigns grades,
    and prints final student grades.”'''
    
    '''“This line removes extra spaces and newline characters using strip(), 
    then split() separates the student name and marks using tab delimiter,
    and finally both values are stored into variables name and marks.”'''
    
    
    
    
''' In Ubuntu, you use cat instead of type.

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