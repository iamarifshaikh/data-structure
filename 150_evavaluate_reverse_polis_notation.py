def evalRPN():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    stack = []

    for i in range(len(tokens)):
        if tokens[i].isdecimal():
            stack.append(tokens[i])
        # else:
        #     print(stack)
        #     one = stack.pop()
        #     two = stack.pop()
        #     stack.append(eval(f"{two} {tokens[i]} {one}"))
    print(stack)
    return int(stack[0])
print(evalRPN())