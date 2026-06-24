# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs)-1)
        return pairs
    
    def helper(self, pairs, s, e):
        if e - s <= 0:
            return pairs
        
        pivot = pairs[e]
        l = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[l] = pairs[l], pairs[i]
                l += 1
        
        pairs[e] = pairs[l]
        pairs[l] = pivot

        self.helper(pairs, l + 1, e)
        self.helper(pairs, s, l - 1)
        