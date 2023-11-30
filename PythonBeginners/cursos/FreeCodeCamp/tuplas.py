# Tuplas are like lists

x = ('Felipe', 'Marcella', 'Floop')
print(x[2])
y = (1, 2, 3)
print(y)
print(max(y))

for iter in y:
    print(iter)

# Tuplas are "immutable"
x = (5, 6, 7)
#x[2] = 8 -- Traceback: 'tuple' is immutable

# A tale of two sequences
i = list()

t = tuple()

# Tuples and Assignment
(x, y) = (4, 'fred')
print(y)
(a, b) = (99,98)
print(a)

# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['csen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

# Tuples are Comparable
(0, 1) < (5, 1)
(0, 1, 200) < (0, 2, 4)
('Sally') < ('Sam')
