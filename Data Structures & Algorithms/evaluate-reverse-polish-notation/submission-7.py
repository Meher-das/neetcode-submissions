class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opset = set()
        opset.add("+")
        opset.add("-")
        opset.add("*")
        opset.add("/")
        for token in tokens:
            if token not in opset:
                stack.append(int(token))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    stack.append(b+a)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(b*a)
                elif token == "/":
                    if a*b < 0:
                        stack.append(-1*(abs(b)//abs(a)))
                    else:
                        stack.append(b//a)
        return stack.pop()

            