def calculate():
    s = "(1+(44+5+2)-3)+(6+8)"
    stack = []
    total_bracket = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
            total_bracket += 1

        elif s[i] == ")":
            total_bracket -= 1
            
            signAddOpp = 0
            signSubOpp = 0
            
            firstNum = ""
            secondNum = ""

            string = ""

            while stack[-1] != "(":
                popped = stack.pop()
                string = f"{popped}" + string
            print(string,stack)
            temp = []
            for i in range(len(string)):
                
                if string[i] != "+" and string[i] != "-":
                    if not signAddOpp and not signSubOpp:
                        firstNum = f"{string[i]}" + firstNum
                    else:
                        secondNum = f"{string[i]}" + secondNum
                else:
                    if not signAddOpp and not signSubOpp:
                        if string[i] == "-":
                            signSubOpp += 1
                        else:
                            signAddOpp += 1
                    else:
                        if signAddOpp:
                            if not temp:
                                temp.append(int(firstNum) + int(secondNum))

                        else:
                            if not temp:
                                temp.append(int(firstNum) - int(secondNum))
                print(stack)
            stack.pop()

        else: stack.append(s[i])
        # print(stack)

print(calculate())