# class Solution:
#     def climbStairs(self, n: int) -> int:

#         def dfs(i):
#             if i >= n:
#                 return i == n
#             return dfs(i + 1) + dfs(i + 2)

#         return dfs(0)

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)