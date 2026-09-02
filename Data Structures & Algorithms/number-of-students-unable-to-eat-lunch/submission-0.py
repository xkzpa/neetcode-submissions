class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        sandwich_left = len(sandwiches)        
        for s in sandwiches:
            i = 0
            while i < len(students) and q[0] != s:
                t = q.popleft()
                q.append(t)
                i += 1
            if q[0] == s:
                q.popleft()
                sandwich_left -= 1
            else: 
                break
        return sandwich_left