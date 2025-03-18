from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0] * len(target)
        for i in range(len(triplets)):
            for j in range(len(triplets[i])):
                print(triplets[i][j], target[j])
                if triplets[i][j] == target[j]:
                    result[j] = triplets[i][j]
        print(result)
        return result == target