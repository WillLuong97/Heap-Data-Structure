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

- Python has a built in heapq library for min-heap which store the number of minimum element at the top of the heap.  This also known as the Priority Queue algorithm 

- This implementation uses arrays for which ```heap[k] <= heap[2*k + 1]``` and ```heap[k] <= heap[2*k+2]``` for all k, counting elements from zero. 

- A key differences from this heap implementation with regular heap is that: 

a. We use zero-based indexing
b. Our pop method returns the the smallest items, not the largest. 

- To create a heap, use a list initialized to [], or you can transform a populated list into a heap by using heapify

### Provided function: 
```heapq.heappush(heap, item)```
+ Push the value item onto the heap, maintaining the heap invariant.

```heapq.heappop(heap)```
+ Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

```heapq.heappushpop(heap, item)```
+ Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

```heapq.heapify(x)```
+ Transform list x into a heap, in-place, in linear time.

```heapq.heapreplace(heap, item)```
+ Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.

+ This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.

+ The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.


```heapq.merge(*iterables)```
+ Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

+ Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).



```heapq.nlargest(n, iterable[, key])```
+Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]



```heapq.nsmallest(n, iterable[, key])```
+ Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key)[:n]









