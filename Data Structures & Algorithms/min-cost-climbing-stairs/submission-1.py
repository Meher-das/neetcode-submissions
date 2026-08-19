class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        answer = [0,0]
        for i in range(2,len(cost)+1):
            x = min(answer[i-1]+cost[i-1], answer[i-2]+cost[i-2])
            answer.append(x)
        return answer[-1]
