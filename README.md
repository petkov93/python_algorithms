# 📝 Algorithms Cheatsheet

A structured reference for common algorithms used in coding interviews, LeetCode, HackerRank, and competitive programming.

---

## 1. Binary Search

**Description:**  
Efficiently searches for a target in a sorted array by repeatedly dividing the search interval in half.

**Variations:**  
- Vanilla binary search (find a single element)  
- First / last occurrence search in a sorted array with duplicates  
- Binary search on answer (optimization problems)

**Time Complexity:**  
- Best: O(1)  
- Average: O(log n)  
- Worst: O(log n)

**Space Complexity:** O(1)

**Use Cases:**  
- Finding elements in sorted arrays/lists  
- Searching boundaries (first/last occurrence)  
- Optimization problems like “minimum maximum distance”  

---

## 2. Depth-First Search (DFS)

**Description:**  
Graph/tree traversal that explores as far as possible along each branch before backtracking. Often recursive.

**Variations:**  
- DFS on graph (recursive with visited set)  
- DFS on grid/matrix (4-direction exploration, e.g., "Number of Islands")  
- DFS with backtracking (permutations, combinations, N-Queens)  
- DFS iterative using a stack (avoids recursion depth limits)  
- Tree DFS:  
  - Preorder (root → left → right)  
  - Inorder (left → root → right, useful for BSTs)  
  - Postorder (left → right → root, useful for deletions/evaluations)  
  - DFS for path accumulation (root-to-leaf paths)  
  - Iterative DFS for trees

**Time Complexity:** O(V + E) (vertices + edges)

**Space Complexity:**  
- Recursive DFS: O(h) for recursion stack (tree height or max depth)  
- Graph: O(V) for visited storage

**Use Cases:**  
- Tree/graph traversals  
- Pathfinding, connected components  
- Topological sorting  
- Generating permutations/combinations  
- Evaluating expressions on trees  

---

## 3. Breadth-First Search (BFS)

**Description:**  
Graph/tree traversal that explores all neighbors at the current depth before moving deeper. Uses a queue.

**Variations:**  
- BFS on graph  
- BFS on grid/matrix (shortest path, 4-direction expansion)  
- Level-order traversal of trees  
- Multi-source BFS (propagation problems, e.g., "Rotting Oranges")  
- Bidirectional BFS (start and end meet, optimizes shortest path)

**Time Complexity:** O(V + E)

**Space Complexity:** O(V) (queue + visited)

**Use Cases:**  
- Shortest path in unweighted graphs  
- Level-order traversal in trees  
- Connected components detection  
- Puzzle or game-solving shortest moves  

---

## 4. Two Pointers

**Description:**  
Two indices move through an array from different directions or speeds to solve problems efficiently.

**Variations:**  
- Opposite ends / converging pointers (sorted array sums, container problems)  
- Same direction (subsequence checks, merging arrays)  
- Fast & slow pointers (linked list cycle detection, middle node)  
- Partitioning / Dutch National Flag (move zeros, sort colors)  
- Three pointers / k-sum extensions  

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Use Cases:**  
- Pair sums in sorted arrays  
- Palindrome and subsequence checks  
- Array/string partitioning problems  
- Sliding over arrays/strings efficiently  

---

## 5. Sliding Window

**Description:**  
Maintain a “window” (contiguous segment) and move it along the array/string, updating results dynamically to optimize brute-force approaches.

**Variations:**  
- Fixed-size window (maximum sum of subarray length k)  
- Dynamic window (expand + shrink, e.g., longest substring with k distinct characters)  
- Minimum window substring (shrink while maintaining condition)  
- Sliding window with monotonic queue (maintain max/min efficiently)

**Time Complexity:** O(n)

**Space Complexity:** O(1) or O(k) depending on stored data

**Use Cases:**  
- Maximum/minimum in subarrays  
- Longest substring without repeating characters  
- Pattern matching problems  
- Real-time streaming data analysis  

---

## 6. Prefix Sum

**Description:**  
Precompute cumulative sums (or other operations) so that range queries can be answered quickly.

**Time Complexity:**  
- Preprocessing: O(n)  
- Query: O(1)

**Space Complexity:** O(n)

**Use Cases:**  
- Fast range sum queries  
- Subarray sum problems (e.g., sum equals k)  
- Difference arrays for range updates  
- 2D prefix sums in matrices/images  

---

## 7. Sorting + Greedy

**Description:**  
Sort elements in a useful order and make locally optimal (greedy) choices to achieve a global optimum.

**Variations:**  
- Interval Scheduling (sort by end time, take earliest finishing)  
- Meeting Rooms (sort starts and ends, count overlaps)  
- Coin Change (descending order, pick largest first for canonical systems)  
- Job Scheduling / Weighted Deadlines (maximize profit by filling slots backwards)  
- Fractional Knapsack (sort by value/weight ratio, pick highest first)

**Time Complexity:**  
- Sorting: O(n log n)  
- Greedy pass: O(n)

**Space Complexity:** O(1)–O(n) depending on implementation

**Use Cases:**  
- Task/interval scheduling  
- Resource allocation  
- Coin change minimization  
- Knapsack/fractional resource optimization  
- Booking and meeting room problems  

---

# Notes

- DFS and BFS are foundational graph/tree algorithms.  
- Two pointers and sliding window are critical for array/string problems.  
- Binary search and sorting + greedy patterns often appear in optimization problems.  
- Prefix sum is key for cumulative or range query problems.  

---

