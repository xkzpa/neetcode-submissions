class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        stack = []
        for o in operations:
            if o[0] == "-":
                record.append(-int(o[1:]))
            if o.isdigit():
                record.append(int(o))
            else:  
                if o == 'C':
                    record.pop()
                if o == 'D':
                    record.append(record[-1] * 2)
                if o == '+':
                    record.append(record[-1] + record[-2])
                
        return sum(record)