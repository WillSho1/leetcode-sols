from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_set = {'+', '-', '*', '/'}
        num_stack = []

        for token in tokens:
            if token in op_set:
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                if token == '+': num_stack.append(num_1 + num_2)
                elif token == '-': num_stack.append(num_1 - num_2)
                elif token == '*': num_stack.append(num_1 * num_2)
                elif token == '/': num_stack.append(int(num_1 / num_2))
            else:
                num_stack.append(int(token))
        return num_stack.pop()