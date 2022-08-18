import string
from itertools import count

def counter(start, end):
    print("inside counter func")
    while start <= end:
        yield start
        start += 1

print(counter(5, 10))
print("----")

for i in counter(5, 10):
    print(i)

def letter_generator():
    for l in string.ascii_uppercase:
        yield l

for l in letter_generator():
    print(l)