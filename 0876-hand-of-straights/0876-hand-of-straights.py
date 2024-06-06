class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handCounter = defaultdict(int)
        for val in hand:
            handCounter[val] += 1
            
        allKeys =  list(handCounter.keys())
        heapq.heapify(allKeys)
        
        while allKeys:
            cur=allKeys[0]
            
            for i in range(cur,cur+groupSize):
                if i not in handCounter:
                    return False
                handCounter[i]-=1
                if handCounter[i]==0:
                    if i != allKeys[0]:
                        return False
                    heapq.heappop(allKeys)
                
            
        return True
                    
                
        
        