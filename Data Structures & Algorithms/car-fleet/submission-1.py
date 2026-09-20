class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = sorted(([p, s] for p, s in zip(position, speed)), reverse = True)
        for p, s in pair:
            arrivingTime = (target-p)/s
            if stack and arrivingTime <= stack[-1]:
                pass
            else:
                stack.append(arrivingTime)
        
        return len(stack)


        