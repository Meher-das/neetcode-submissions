from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [-cnt for _ , cnt in Counter(tasks).items()]
        heapq.heapify(count)
        time = 0
        queue = deque()
        while queue or count:
            time += 1
            if count:
                x = heapq.heappop(count) + 1
                if x != 0:
                    queue.append([x, time + n])
            if queue and queue[0][1] == time:
                y = queue.popleft()[0]
                if y != 0:
                    heapq.heappush(count, y)
        return time
