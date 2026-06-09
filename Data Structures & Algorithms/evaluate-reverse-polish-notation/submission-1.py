class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c =="+":
                stack.append(stack.pop()+stack.pop())
            elif c =="-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                #进行计算需要string to int,并且最后返回的也需要是int
                stack.append(int(c))
        
        return stack[0]
        