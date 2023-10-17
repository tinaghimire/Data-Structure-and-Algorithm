# Data Structure and Algorithm in Python

**These are not my words. I created this for future revision.**

## I. Linked Lists

- Sequence of data connected through links.
- Each element, called node, has two parts: Data and pointer to the next element. 
- Used to implement other data structures:
    -Stacks
    -Queues
    -Graphs
- Access information by navigating backward and forward
    -Web Browser
    -Music Playlist

### Operations:
1. Insert at beginning
2. Remove at beginning
3. Insert at end
4. Remove at end
5. Insert at position
6. Remove at position
7. Search

## II. Big O notation

- Measure the worst case complexity of an algorithm.
- Does not use seconds/bytes.

### Simplifying Big O notation

1. Remove constants
2. Different variables for different inputs
3. Remove smaller terms

## III. Stack

- Last In First Out (LIFO) type
- Push and pop operation 

**LifoQueue in Python: (Like Stack)**

## IV. Queue

- First In First Out (FIFO) type
- Enqueue (only insert at end) and Dequeue (only remove from head) operation
- Other kinds of queue:
  - Doubly ended queues
  - Circular queues
  - Priority queues

**SimpleQueue in Python: (Like Queue)**

## V. Hash table

- Stores a collection of items
- Key value pairs (Dictionaries in python)
- Each position in hash is called slots/ buckets.
- Every time a hash function is applied, it must return the same value for the same input
- If different inputs get the same output or slot area, then there occurs collision.

## VI. Trees 

- Node-based data structures
- Each node can have links to more than one node.
- Binary tree is a tree that can have atmost two children in each node.

## VII. Graphs

- A collection of nodes that have data and are connected to other nodes.
- A graph can be directed, undirected or bidirected.
- A weighted graph contains numeric values associated with the edges and can be either directed or undirected.

### Differences between Trees and Graphs

- Trees cannot have cycles but graph can.
- In trees, all nodes must be connected but in graphs, there may be unconnected nodes.
- Both are used for searching and sorting algorithm.

## VIII. Recursion

- Function calling itself
- Example: Factorial, TowerOfHanoi

### How recursion works (Example: Factorial)

- factorial(5) starts
- Before factorial(5) finishes -> factorial(4) starts 
- Before factorial(4) finishes -> factorial(3) starts 
- Before factorial(3) finishes -> factorial(2) starts 
- Before factorial(2) finishes -> factorial(1) starts 
- factorial(1) finishes and returns 1
- Then the execution of factorial(2) starts and after completion next starts.

### Dynamic Programming

- Optimization technique
- Mainly applied to recursion
- Can reduce the complexity of recursive algorithms
- Used for:
  - Any problems that can be divided into smaller subproblems
  - Subproblems overlap
- Solutions of subproblems are saved, avoiding the need to recalculate













