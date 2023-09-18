class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [(row:= [1])]

        for _ in range(1, numRows):

            row = list(map(sum,pairwise([0]+row+[0])))
            ans.append(row)

        return ans