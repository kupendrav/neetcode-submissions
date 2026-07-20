class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for n in nums:
            map[n]=map.get(n,0)+1
        sorted_items=sorted(map.items(),key=lambda x:x[1],reverse=True)  
        ans=[]
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans      