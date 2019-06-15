
def checkStack(s):
    stack = [0] * len(s)
    top = -1
    wrong = 0
    for i in range(len(s)):
        if (s[i] == "("):
            top += 1
            stack[top] = s[i]
        elif s[i] == ")":
            if top == -1:
                wrong = 1
                break
            if stack[top] == "(":
                top -=1
    if top == -1 and not wrong : return "Yes"
    else: return "No"

a = "()()((()))"
b = "((()((((()()((()())((())))))"

print("괄호 짝이 맞니?",checkStack(a))
print("괄호 짝이 맞니?",checkStack(b))


# 2
# stack = [0] * 100
# top = -1
# str = "(()()))"
#
# wrong = 0
# for i in range(len(str)):
#     if str[i] == '(':
#         top += 1; stack[top] = str[i]
#     elif str[i] == ')':
#         if top == -1:
#             wrong = 1
#             break
#         if stack[top] == '(':
#             top -= 1
#
# if top == -1 and not wrong : print("correct!")
# else: print("wrong!")
