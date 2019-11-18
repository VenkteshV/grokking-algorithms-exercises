from ArrayStack import ArrayStack
import os 
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def reverse_file(filename):
    S = ArrayStack()
    original = open(os.path.join(__location__, filename))
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    output = open(os.path.join(__location__,'output.txt'), 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

reverse_file('example.txt')