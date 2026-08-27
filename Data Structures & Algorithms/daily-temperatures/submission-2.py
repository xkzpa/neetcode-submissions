class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temps)
        for i, t in enumerate(temps):
            while stack and t > stack[-1][0]:
                stackTemp, stackInx = stack.pop()
                result[stackInx] = i - stackInx
            stack.append([t,i])
        return result