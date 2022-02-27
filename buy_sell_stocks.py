class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        T = O(N)
        S = O(1)
        '''
        l , r = 0 , 1 
        buy = prices[l]
        p = 0 
        while l < r and r < len(prices):
            if prices[l] < prices[r]: # sell
                p += prices[r] - buy
                buy = prices[r]
            elif prices[l] > prices[r]: #buy
                buy = min(buy, prices[r] )
            l += 1
            r += 1
        return p
