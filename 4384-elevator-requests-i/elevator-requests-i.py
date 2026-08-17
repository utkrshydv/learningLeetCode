class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = requests[0]

        for i in range(1, len(requests)):
            time += abs(requests[i-1] - requests[i])
            
        return time



        