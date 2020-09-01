# Heap Data Structure

## Definition: 

- A heap is a special tree based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types: 

### Max heap: 

- In a Max-Heap the key present at the root node must be the greatest among all the keys present at all of it's children. The same property must be reursively true for all sub-trees in 
that Binary Tree. 

### Min heap: 

- In a Min-Heap they key present all the root node must be minimum among the keys present at all of its children. The same property must recurslvely true for 
all sub-trees in that Binary Tree. 


![alt text](/MinHeapAndMaxHeap.png)

## Complete Binary Tree: 

### Definition: 

- Complete binary tree is a binary tree in which all levels are completely filled except possibly the lowest one, which is filled from the left. 
- A complete binary tree is similar to a full binary tree except that: 

1. All the leaf element must lean toward the left
2. The last leaf element might not have a right sibling, or a complete binary tree doesn't have to be a full binary tree. 


## Heap-Queue implementation: 

### Definition: 

- Python has a built in heapq library for min-heap which store the number of minimum element at the top of the heap.  




