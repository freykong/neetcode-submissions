# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper(pairs, 0, len(pairs) - 1)
    
    def helper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        mid = (start + end) // 2

        self.helper(pairs, start, mid)
        self.helper(pairs, mid + 1, end)

        self.merge(pairs, start, mid, end)
        
        return pairs
    
    def merge(self, arr, start, mid, end):
        l = arr[start: mid + 1]
        r = arr[mid + 1: end + 1]

        i, j, k = 0, 0, start

        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            k += 1
            i += 1
            
        while j < len(r):
            arr[k] = r[j]
            k += 1
            j += 1


