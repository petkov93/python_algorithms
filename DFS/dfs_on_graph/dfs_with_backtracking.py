"""
DFS + undo step → useful in generating permutations/combinations/paths.
Outer function holds results, inner dfs builds partial solution.

✅ Used in: "Permutations", "N-Queens", "Word Search".
"""

def permutations(nums):
    result = []
    used = [False] * len(nums)

    def dfs(path):
        if len(path) == len(nums):
            result.append(path[:])   # copy
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()           # backtrack
                used[i] = False

    dfs([])
    return result

print(permutations([1,2,3]))
