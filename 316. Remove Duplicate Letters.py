def removeDuplicateLetters():
    s = "cbacdcbc"
    last = {s[i] : i for i in range(len(s))}
    print(last)
    stack = []
    seen = set()

    for index,char in enumerate(s):
        if char in seen:
            continue
        while stack and stack[-1] > char and last[stack[-1]] > index:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return "".join(stack)

result = removeDuplicateLetters()
print(result)