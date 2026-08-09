class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        hash_map = {}
        stack = []
        counter = len(temperatures) - 1
        while counter >= 0:
            if not stack:
                stack.append(temperatures[counter])
            else:
                while stack and stack[-1] <= temperatures[counter]:
                    stack.pop()
                if stack:
                    answer[counter] = hash_map[stack[-1]] - counter
                stack.append(temperatures[counter])
        
            hash_map[temperatures[counter]] = counter 
            counter -= 1
        return answer