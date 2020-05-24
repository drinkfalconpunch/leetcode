class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]
            max_weight = max(stones)
            stones.remove(max_weight)
            max_weight2 = max(stones)
            stones.remove(max_weight2)
            if max_weight != max_weight2:
                stones.append(abs(max_weight - max_weight2))