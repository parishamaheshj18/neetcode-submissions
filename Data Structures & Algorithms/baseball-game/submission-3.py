class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans_stack = []
        total = 0
        for operation in operations:
                if operation.lstrip("-").isdigit():
                    ans_stack.append(int(operation))
                    total+=int(operation)
                elif operation == "+":
                    sum_ = ans_stack[-1] + ans_stack[-2]
                    ans_stack.append(sum_)
                    total+=sum_
                elif operation=="D":
                    double = 2*ans_stack[-1]
                    ans_stack.append(double)
                    total+=double
                elif operation=="C":
                    total-=ans_stack.pop()

        return total


        