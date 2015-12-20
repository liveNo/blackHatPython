# coding=utf-8
#/usr/bin/python


# Function one
numbers = range(10)
size = len(numbers)
events = []
i = 0
while i < size:
    if i % 2 == 0:
        events.append(i)
    i += 1

print events


# Function two Equel to Function one
# 这种方法相比较上一种方法比较高效，而且更加简短，涉及元素也比较少。
event = [i for i in range(10) if i % 2 == 0]
print event


# Python 1 ===
i = 0
seq = ["one", "two", "three"]
for element in seq:
    seq[i] = '%d:%s' % (i, seq[i])
    i += 1

print seq

# Python 2 === Python 1

seq = ["one", "two", "three"]
for i,element in enumerate(seq):
    seq[i] = '%d:%s' % (i, seq[i])

print seq


# Python 3 ===

def _treatment (pos, element):
    return '%d:%s' % (pos, element)


seq = ["one", "two", "three"]

seq = [_treatment(i, el) for i, el in enumerate(seq)]

print seq