# First solution. Too slow.
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maximum = -999999
        for i, _ in enumerate(A):
            sums = []
            sublist = A[i:] + A[:i]
            for j, w in enumerate(sublist):
                for k in range(len(sublist) - j):
                    sums.append(sum(sublist[k:]))
            if max(sums) > maximum:
                maximum = max(sums)
        return maximum

