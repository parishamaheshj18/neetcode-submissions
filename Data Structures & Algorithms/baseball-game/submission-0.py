class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans_stack = []
        for operation in operations:
            try:
                ans_stack.append(int(operation))
            except:
                if operation == "+":
                    sum_ = ans_stack[-1] + ans_stack[-2]
                    ans_stack.append(sum_)
                elif operation=="D":
                    double = 2*ans_stack[-1]
                    ans_stack.append(double)
                elif operation=="C":
                    ans_stack.pop()
        return sum(ans_stack)


        