class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sorted_heights = sorted(heights)
        unexpected = 0

        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                unexpected += 1

        return unexpected
        