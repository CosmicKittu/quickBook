---
title: Python DSA Reference
logo: Python DSA Guide
sidebartitle: Python Data Structures
sidebarsub: DSA Reference
herotitle: Python <span>Collections</span> DSA
herodesc: A comprehensive quick reference for Python data structures and algorithms. Covers lists, stacks, queues, heaps, sets, dicts, deques, strings, and more — everything you need for DSA and coding interviews.
tags: Python, Interview Ready
---

## 00 — PYTHON | Getting Started

```python
# Python does not need imports for basic types.
# For advanced containers, use:
import collections   # deque, Counter, defaultdict, OrderedDict
import heapq         # min-heap operations
import bisect        # binary search on sorted lists
import itertools     # combinatorics, permutations
import functools     # caching, reduce

print("Hello, World!")
```

## 01 — PYTHON | List

Lists are Python's dynamic arrays — the most versatile data structure.

```python
# ========== Working Principle ========== #
# Dynamic array — stores elements in contiguous memory.
# O(1) random access via index.
# Amortized O(1) append. O(n) insert/delete in middle.

# ========== Declaration ========== #
v = []                          # empty list
v = [1, 2, 3, 4, 5]            # initialized
v2 = v.copy()                  # shallow copy
v3 = list(v)                   # another way to copy
v4 = [0] * 10                  # list of 10 zeros

# 2D list (m x n matrix initialized with 0)
m, n = 3, 3
mat = [[0] * n for _ in range(m)]

# ========== Adding Elements ========== #
v.append(13)                   # add to end — O(1) amortized
v.insert(0, 10)                # insert at index 0 — O(n)
v.extend([14, 20, 25])         # add multiple elements at end
v += [30, 35]                  # also extends

# ========== Deleting Elements ========== #
v.pop()                        # remove & return last element — O(1)
v.pop(0)                       # remove & return element at index — O(n)
v.remove(14)                   # remove first occurrence of value — O(n)
del v[1]                       # delete element at index
v.clear()                      # remove all elements

# ========== Accessing Elements ========== #
v = [10, 20, 30, 40, 50]
v[0]                           # first element → 10
v[-1]                          # last element → 50
v[1:3]                         # slice → [20, 30]
v[::-1]                        # reversed list → [50, 40, 30, 20, 10]

# ========== Other Important Methods ========== #
len(v)                         # number of elements
v.index(30)                    # index of first occurrence of 30
v.count(20)                    # count occurrences of 20

# Sorting — O(n log n) Timsort
v.sort()                       # ascending (in-place)
v.sort(reverse=True)           # descending (in-place)
sorted_v = sorted(v)           # returns new sorted list (non-mutating)

# Custom sort — sort by absolute value
v.sort(key=abs)

v.reverse()                    # reverse in-place

max(v)                         # maximum value
min(v)                         # minimum value
sum(v)                         # sum of all elements

# Binary search (needs sorted list)
import bisect
idx = bisect.bisect_left(v, 30)   # index where 30 would be inserted
found = idx < len(v) and v[idx] == 30

# Iterating
for num in v:
    print(num)

for i, num in enumerate(v):
    print(i, num)

# List comprehension
squares = [x ** 2 for x in range(10)]
evens = [x for x in v if x % 2 == 0]

# Swap two elements
v[0], v[1] = v[1], v[0]

# Unpack
a, b, *rest = v
```

## 02 — PYTHON | Stack

Python lists can be used directly as stacks (LIFO).

```python
# ========== Working Principle ========== #
# LIFO → Last In First Out
# list.append() is push, list.pop() is pop. Both O(1).

# ========== Declaration ========== #
stack = []

# ========== Push ========== #
stack.append(23)
stack.append(34)
stack.append(45)

# ========== Pop ========== #
top = stack.pop()              # removes & returns 45

# ========== Peek ========== #
top = stack[-1]                # returns top without removing

# ========== Other Methods ========== #
len(stack)                     # size
not stack                      # True if empty (Pythonic way)
bool(stack)                    # True if non-empty

# Iterating (destructive — empties the stack)
while stack:
    print(stack.pop())
```

## 03 — PYTHON | Queue

Use `collections.deque` for an efficient FIFO queue.

```python
from collections import deque

# ========== Working Principle ========== #
# FIFO → First In First Out
# deque gives O(1) append and popleft.
# Do NOT use list for queues — list.pop(0) is O(n)!

# ========== Declaration ========== #
que = deque()

# ========== Enqueue (add to back) ========== #
que.append(1)
que.append(2)
que.append(3)

# ========== Dequeue (remove from front) ========== #
front = que.popleft()          # removes & returns 1

# ========== Peek ========== #
front = que[0]                 # front element
back = que[-1]                 # back element

# ========== Other Methods ========== #
len(que)                       # size
not que                        # True if empty
que.clear()                    # remove all

# Iterating (non-destructive)
for item in que:
    print(item)

# Iterating (destructive)
while que:
    print(que.popleft())
```

## 04 — PYTHON | Deque

`collections.deque` supports O(1) operations on both ends.

```python
from collections import deque

# ========== Working Principle ========== #
# Double-ended queue. O(1) append/pop on both sides.
# Implemented as a doubly-linked list of fixed-size blocks.

# ========== Declaration ========== #
dq = deque()
dq = deque([1, 2, 3])
dq = deque(maxlen=5)           # bounded deque (auto-drops oldest)

# ========== Adding Elements ========== #
dq.append(10)                  # add to right
dq.appendleft(5)               # add to left
dq.extend([20, 30])            # extend right
dq.extendleft([2, 1])          # extend left (items reversed)

# ========== Removing Elements ========== #
dq.pop()                       # remove from right
dq.popleft()                   # remove from left
dq.remove(10)                  # remove first occurrence of value
dq.clear()                     # remove all

# ========== Accessing Elements ========== #
dq = deque([10, 20, 30, 40])
dq[0]                          # first → 10
dq[-1]                         # last → 40

# ========== Rotation ========== #
dq.rotate(1)                   # rotate right by 1 → [40, 10, 20, 30]
dq.rotate(-1)                  # rotate left by 1  → [10, 20, 30, 40]

# ========== Other Methods ========== #
len(dq)
dq.count(20)
dq.index(30)
dq.reverse()
```

## 05 — PYTHON | Heap (Priority Queue)

Use the `heapq` module for a min-heap built on top of a list.

```python
import heapq

# ========== Working Principle ========== #
# Min-Heap by default: smallest element at index 0.
# heapq operates on a regular Python list.
# No max-heap built-in — negate values to simulate one.

# ========== Declaration ========== #
heap = []

# ========== Push ========== #
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
# heap is now [10, 30, 20] (min-heap property)

# ========== Pop (smallest) ========== #
smallest = heapq.heappop(heap)     # returns 10

# ========== Peek ========== #
top = heap[0]                      # smallest element without removing

# ========== Push + Pop in one step ========== #
heapq.heappushpop(heap, 5)         # push 5, then pop smallest
heapq.heapreplace(heap, 50)        # pop smallest, then push 50

# ========== Heapify an existing list ========== #
arr = [5, 3, 8, 1, 2]
heapq.heapify(arr)                 # in-place O(n) — arr is now a heap

# ========== Max-Heap Trick ========== #
# Negate values on push, negate again on pop
max_heap = []
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
largest = -heapq.heappop(max_heap) # returns 30

# ========== N Largest / N Smallest ========== #
data = [5, 3, 8, 1, 2, 9, 4]
heapq.nlargest(3, data)            # [9, 8, 5]
heapq.nsmallest(3, data)           # [1, 2, 3]

# ========== Heap with Tuples (priority, value) ========== #
task_heap = []
heapq.heappush(task_heap, (2, "medium task"))
heapq.heappush(task_heap, (1, "urgent task"))
heapq.heappush(task_heap, (3, "low task"))

priority, task = heapq.heappop(task_heap)  # (1, "urgent task")

# Iterating in sorted order (destructive)
while heap:
    print(heapq.heappop(heap))
```

## 06 — PYTHON | Set

Unordered collection of unique elements with O(1) average lookup.

```python
# ========== Working Principle ========== #
# Hash-based. No duplicates. Unordered.
# O(1) average for add, remove, contains.
# Equivalent to C++ unordered_set.

# ========== Declaration ========== #
s = set()
s = {1, 2, 3, 4, 5}
s = set([1, 2, 3])              # from a list

# ========== Adding Elements ========== #
s.add(10)                       # add single element
s.update([20, 30, 40])          # add multiple elements

# ========== Removing Elements ========== #
s.remove(10)                    # remove — raises KeyError if missing
s.discard(99)                   # remove — does nothing if missing (safe)
s.pop()                         # remove & return an arbitrary element
s.clear()                       # remove all

# ========== Lookup ========== #
s = {1, 2, 3, 4, 5}
3 in s                          # True — O(1)
99 not in s                     # True

# ========== Set Operations ========== #
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b                           # union        → {1, 2, 3, 4, 5, 6}
a & b                           # intersection  → {3, 4}
a - b                           # difference    → {1, 2}
a ^ b                           # symmetric diff → {1, 2, 5, 6}

a.issubset(b)                   # False
a.issuperset({1, 2})            # True
a.isdisjoint({7, 8})            # True (no common elements)

# ========== Other Methods ========== #
len(s)
not s                           # True if empty

# Frozen set (immutable — can be used as dict key or in another set)
fs = frozenset([1, 2, 3])

# Iterating
for item in s:
    print(item)
```

## 07 — PYTHON | Dictionary

Hash-based key-value store with O(1) average operations (like C++ unordered_map).

```python
# ========== Working Principle ========== #
# Hash map. Keys must be immutable (str, int, tuple).
# Insertion-ordered since Python 3.7+.
# O(1) average for get, set, delete.

# ========== Declaration ========== #
d = {}
d = {"apple": 1, "banana": 2, "cherry": 3}
d = dict(apple=1, banana=2)
d = dict.fromkeys(["a", "b", "c"], 0)   # {"a": 0, "b": 0, "c": 0}

# ========== Adding / Updating ========== #
d["date"] = 4                   # add or overwrite
d.update({"elderberry": 5, "fig": 6})

# ========== Deleting ========== #
del d["date"]                   # delete key — raises KeyError if missing
d.pop("fig")                    # remove & return value
d.pop("missing", None)          # safe pop with default
d.popitem()                     # remove & return last inserted (k, v)
d.clear()                       # remove all

# ========== Accessing ========== #
d = {"a": 1, "b": 2, "c": 3}
d["a"]                          # → 1 (raises KeyError if missing)
d.get("z", -1)                  # → -1 (safe access with default)
"a" in d                        # True — O(1)

# ========== Iterating ========== #
for key in d:                   # iterate over keys
    print(key, d[key])

for key, val in d.items():      # iterate over key-value pairs
    print(key, val)

for val in d.values():          # iterate over values only
    print(val)

# ========== Other Methods ========== #
len(d)
list(d.keys())
list(d.values())
list(d.items())

# Merge two dicts (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2               # {"a": 1, "b": 2}

# Dict comprehension
squares = {x: x**2 for x in range(6)}

# setdefault — get value or insert default
d.setdefault("new_key", 42)    # inserts 42 if "new_key" missing
```

## 08 — PYTHON | Counter (Multi-Set)

`Counter` counts hashable elements — equivalent to C++ `multiset` counting.

```python
from collections import Counter

# ========== Working Principle ========== #
# Subclass of dict that maps elements to their counts.
# Perfect for frequency counting in DSA problems.

# ========== Declaration ========== #
c = Counter()
c = Counter([1, 2, 2, 3, 3, 3])           # {3: 3, 2: 2, 1: 1}
c = Counter("abracadabra")                 # {'a': 5, 'b': 2, 'r': 2, ...}
c = Counter({"red": 4, "blue": 2})

# ========== Adding / Updating ========== #
c["green"] = 3
c["red"] += 1
c.update(["red", "blue", "blue"])          # add counts from iterable

# ========== Accessing Counts ========== #
c["red"]                                    # count of "red"
c["missing"]                                # 0 (never raises KeyError!)

# ========== Most / Least Common ========== #
c.most_common(2)                            # [('a', 5), ('b', 2)]
c.most_common()                             # all, sorted by frequency

# ========== Arithmetic Operations ========== #
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2                                     # Counter({'a': 4, 'b': 3})
c1 - c2                                     # Counter({'a': 2}) — drops zero/negative
c1 & c2                                     # min of each → Counter({'a': 1, 'b': 1})
c1 | c2                                     # max of each → Counter({'a': 3, 'b': 2})

# ========== Other Methods ========== #
sum(c.values())                             # total count
list(c.elements())                          # iterator over elements repeating by count
c.clear()

# Frequency of frequencies
data = [1, 1, 2, 2, 2, 3]
freq = Counter(data)                        # {2: 3, 1: 2, 3: 1}
freq_of_freq = Counter(freq.values())       # {1: 1, 2: 1, 3: 1}
```

## 09 — PYTHON | defaultdict

A dict that auto-creates missing keys with a factory function.

```python
from collections import defaultdict

# ========== Working Principle ========== #
# Like a regular dict, but accessing a missing key
# automatically inserts a default value.

# ========== Declaration ========== #
dd_int = defaultdict(int)          # default value: 0
dd_list = defaultdict(list)        # default value: []
dd_set = defaultdict(set)          # default value: set()

# ========== Usage: Frequency Count ========== #
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = defaultdict(int)
for w in words:
    freq[w] += 1
# freq → {'apple': 3, 'banana': 2, 'cherry': 1}

# ========== Usage: Group by Key ========== #
pairs = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana")]
groups = defaultdict(list)
for category, item in pairs:
    groups[category].append(item)
# groups → {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}

# ========== Usage: Adjacency List (Graphs) ========== #
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected
# graph → {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

# ========== Custom Default ========== #
dd_custom = defaultdict(lambda: "N/A")
dd_custom["missing_key"]          # → "N/A"
```

## 10 — PYTHON | Tuple & Named Tuple

Immutable sequences — Python's equivalent of C++ `std::pair` and structs.

```python
from collections import namedtuple

# ========== Tuple (Like std::pair) ========== #
# Immutable, hashable, can be used as dict keys or in sets.

t = (1, 2)
t = (10, "hello", 3.14)
a, b = (1, 2)                     # unpacking
x, y, z = (10, "hello", 3.14)

# Accessing
t[0]                               # first element
t[-1]                              # last element

# As a pair equivalent
pair = (3, 7)
first, second = pair

# Sorting list of tuples
pairs = [(2, "b"), (1, "a"), (3, "c")]
pairs.sort()                       # sorts by first element, then second
pairs.sort(key=lambda p: p[1])     # sort by second element

# Tuples as dict keys
grid = {}
grid[(0, 0)] = "start"
grid[(2, 3)] = "end"

# ========== Named Tuple ========== #
# Like a lightweight class / struct
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
p.x                                # 3
p.y                                # 7

# Can still unpack
x, y = p

# Use in heap for structured data
import heapq
Edge = namedtuple("Edge", ["weight", "src", "dest"])
edges = []
heapq.heappush(edges, Edge(5, 0, 1))
heapq.heappush(edges, Edge(2, 0, 2))
lightest = heapq.heappop(edges)    # Edge(weight=2, src=0, dest=2)
```

## 11 — PYTHON | String

Strings in Python are **immutable** sequences of characters.

```python
# ========== Declaration ========== #
s = "hello"
s = 'world'
s = """multi
line"""

# ========== Common Operations ========== #
len(s)                          # length
s[0]                            # first char → 'h'
s[-1]                           # last char → 'o'
s[1:4]                          # slice → "ell"
s[::-1]                         # reverse → "olleh"

# ========== Searching ========== #
s = "hello world"
s.find("world")                 # index → 6 (returns -1 if not found)
s.index("world")                # index → 6 (raises ValueError if not found)
"world" in s                    # True — O(n)
s.count("l")                    # 3
s.startswith("hello")           # True
s.endswith("world")             # True

# ========== Modification (returns new string) ========== #
s.upper()                       # "HELLO WORLD"
s.lower()                       # "hello world"
s.strip()                       # remove leading/trailing whitespace
s.lstrip()                      # remove leading whitespace
s.rstrip()                      # remove trailing whitespace
s.replace("world", "python")    # "hello python"
s.split()                       # ["hello", "world"]
s.split(",")                    # split by comma
"-".join(["a", "b", "c"])       # "a-b-c"

# ========== Character Checks ========== #
"abc".isalpha()                 # True
"123".isdigit()                 # True
"abc123".isalnum()              # True
"   ".isspace()                 # True

# ========== Conversion ========== #
ord("A")                        # 65 (char → ASCII)
chr(65)                         # "A" (ASCII → char)
int("42")                       # 42
str(42)                         # "42"

# ========== String Building (IMPORTANT!) ========== #
# Strings are immutable — concatenation in a loop is O(n²)!
# Use a list and join instead:
parts = []
for i in range(5):
    parts.append(str(i))
result = "".join(parts)         # "01234" — O(n)

# f-strings (formatted string literals)
name = "Alice"
age = 30
msg = f"{name} is {age} years old"
```

## 12 — PYTHON | Sorting & Comparisons

Python's sort is **Timsort** — O(n log n), stable.

```python
# ========== Basic Sorting ========== #
arr = [5, 2, 8, 1, 9]
arr.sort()                      # in-place ascending → [1, 2, 5, 8, 9]
arr.sort(reverse=True)          # in-place descending

new_arr = sorted(arr)           # returns new list (original unchanged)
new_arr = sorted(arr, reverse=True)

# ========== Custom Sort with Key ========== #
words = ["banana", "apple", "cherry"]
words.sort(key=len)             # sort by length
words.sort(key=str.lower)       # case-insensitive sort

# Sort by multiple criteria
students = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
students.sort(key=lambda s: (-s[1], s[0]))
# Sort by score descending, then name ascending

# ========== Custom Comparator (cmp_to_key) ========== #
from functools import cmp_to_key

def compare(a, b):
    if a < b: return -1
    if a > b: return 1
    return 0

arr.sort(key=cmp_to_key(compare))

# ========== Binary Search (bisect) ========== #
import bisect

arr = [1, 3, 5, 7, 9]
bisect.bisect_left(arr, 5)      # 2 — leftmost position to insert 5
bisect.bisect_right(arr, 5)     # 3 — rightmost position to insert 5
bisect.insort(arr, 6)           # insert 6 maintaining sorted order

# Check if element exists
def binary_search(arr, target):
    idx = bisect.bisect_left(arr, target)
    return idx < len(arr) and arr[idx] == target

# ========== Min / Max ========== #
max(arr)
min(arr)
max(arr, key=abs)               # max by absolute value

# Min/max with custom objects
max(students, key=lambda s: s[1])   # student with highest score
```

## 13 — PYTHON | Useful Built-ins

Python built-in functions that are essential for DSA.

```python
# ========== zip — iterate in parallel ========== #
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]
for name, score in zip(names, scores):
    print(name, score)

# Create dict from two lists
d = dict(zip(names, scores))

# ========== map / filter ========== #
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))     # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# ========== any / all ========== #
any([False, False, True])       # True — at least one True
all([True, True, True])         # True — all are True

# Check conditions over iterable
nums = [2, 4, 6, 8]
all(x % 2 == 0 for x in nums)  # True — all even
any(x > 5 for x in nums)       # True — at least one > 5

# ========== enumerate ========== #
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)               # 0 a, 1 b, 2 c

# ========== reversed ========== #
for x in reversed([1, 2, 3]):
    print(x)                    # 3, 2, 1

# ========== itertools ========== #
import itertools

# Permutations
list(itertools.permutations([1, 2, 3]))       # all orderings
list(itertools.permutations([1, 2, 3], 2))    # 2-length permutations

# Combinations
list(itertools.combinations([1, 2, 3, 4], 2)) # all 2-element combos
list(itertools.combinations_with_replacement([1, 2, 3], 2))

# Accumulate (prefix sums)
list(itertools.accumulate([1, 2, 3, 4]))       # [1, 3, 6, 10]

# Product (cartesian product)
list(itertools.product([0, 1], repeat=3))      # all 3-bit binary numbers

# ========== functools.lru_cache (Memoization) ========== #
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)   # instant — memoized

# ========== math module ========== #
import math
math.gcd(12, 8)                 # 4
math.lcm(4, 6)                  # 12 (Python 3.9+)
math.sqrt(16)                   # 4.0
math.ceil(3.2)                  # 4
math.floor(3.8)                 # 3
math.inf                        # positive infinity
-math.inf                       # negative infinity
math.log2(8)                    # 3.0
math.factorial(5)               # 120
```
