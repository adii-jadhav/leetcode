class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s= ''.join(map(str,digits))
        i=int(s)+1
        li=list(map(int,str(i)))  
        return li