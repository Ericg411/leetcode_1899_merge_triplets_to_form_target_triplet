from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [False] * len(target)
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                result[0] = True
            if triplet[0] <= target[0] and triplet[1] == target[1] and triplet[2] <= target[2]:
                result[1] = True
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] == target[2]:
                result[2] = True
            
        return result[0] and result[1] and result[2]