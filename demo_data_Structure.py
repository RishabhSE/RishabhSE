"""
Dictionaries
    
"""



# Creating a dictionary
phonebook = { 'bob' :1234,
                'mob':2343,
                'cob':2323,
                'rob':4543,
             }

print(phonebook)

phonebook2  = dict()
phonebook2  = {}


# Operations like Insert, Update,Delete, Lookup

phonebook = { 'bob' :1234,
                'mob':2343,
                'cob':2323,
                'rob':4543,
             }
# phonebook['sob'] = 9999

# phonebook['sob'] = 0000
# print(phonebook)

# print(phonebook.keys())
# print(phonebook.values())

# print(phonebook['pob'])
# print(phonebook.get('pob') )

# phonebook.pop('mob')
# print(phonebook)

# del phonebook['cob']













# Case when insert-order into dictonary is important

 
 
 
 
 
 
from collections import OrderedDict
 
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
 
od['a'] = 99
for key, value in od.items():
    print(key, value)








#  Case when we dont want to catch keyerror or use get() method to handle unknown keys







from collections import defaultdict

      
d = defaultdict( lambda: -1)
# d = defaultdict( int )

d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])








# Case when we want our dictionay to be read only






from types import MappingProxyType

phonebook = { 'bob' :1234,
                'mob':2343,
                'cob':2323,
                'rob':4543,
             }

read_only = MappingProxyType(phonebook)

read_only['rob'] = 9999


























"""

Array Data Structure
    
"""

# List -- Dynamic arrays, loosly packed

from sys import getsizeof 
lst = [0,"s",1,2.34]

# lst[1] = 'qwerty'
# print(lst)

# del lst[1]
lst.append("bluepi")

# print(lst)

print(getsizeof(lst))





# tupple -- Dynamic arrays, loosly packed, immutable







tple = (0,"qwert")
tple[0] = "23"
print(tple)





# Case when we want to access dictonary by  index i.e iterable, 


# The namedtuple is a class factory. 
# In other words, it manufactures classes.








class Student:
    def __init__(self, student_no, first_name, last_name, birth_year, gender):
        self.student_no = student_no
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.gender = gender


s1 = Student(1,"bob","sharma",1990,"M")
print(s1.first_name)










from collections import namedtuple

Student = namedtuple('Student', 'student_no, first_name, last_name, birth_year, gender')

s1 = Student(1,"bob","sharma",1990,"M")

# print(s1.birth_year)
print(s1[1])





"""

Sets & Multisets
    
"""











num = {1,2,4,3,99,50,1,2}

# unique elements
print(num)

num.add(1)
num.add(1)
num.add(1)


print(num)








# case when a set, which can we used to count the number of occurances


word = "mississippi"
counter = {}


for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)




# Counter is a subclass of dict that’s specially designed for counting hashable objects in Python.
from collections import Counter

word = "mississippi"
# print(Counter(word))

lst = [1,2,3,4,1,1,1,2,2]
# print(Counter(lst))

# phonebook = { 'bob' :1234,
#                 'mob':2343,
#                 'cob':2323,
#                 'rob':4543,
#              }
# print(Counter(phonebook))



lst2 = [1,1,1,1,5,6,7,8]

cnt = Counter(lst)
cnt.update(lst2)
print(cnt)







"""

Stack, Queues & Priority Queues
    
"""



# List as stack


[1,2,3]
# Very Slow when insert/delete from front, O(n)

s= []
s.append(1)
s.append(2)
s.append(3)

s.pop()
s.pop()
s.pop()
s.pop()








# Fast & Robust Stack (LIFO)

from collections import deque
# Double linked list implementation

s = deque()

s.append(1)
s.append(2)
s.append(3)

s.pop()
s.pop()
s.pop()





# Queue 

from collections import deque
s = deque()

s.append(1)
s.append(2)
s.append(3)

s.popleft()
s.popleft()
s.popleft()





# Priority Queue
# O(nlogn)

q = []

q.append((2,'code'))
q.append((1,'eat'))
q.append((3,'sleep'))

q.sort(reverse=True)

print(q)








import heapq
# O(logn)
# heap sort

q= []
heapq.heappush(q,(2,'code'))
heapq.heappush(q,(1,'eat'))
heapq.heappush(q,(3,'sleep'))

print(q)

# heapq.heappop(q)

print(q)

