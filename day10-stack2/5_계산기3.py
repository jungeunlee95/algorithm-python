import sys
sys.stdin = open("5_계산기3", "r")

for t in range(1, 11):
    N = int(input())
    a = input()
    stack = [0] * 1000000
    sic = ['*', '+']
    top = -1
    result = ""

    for i in range(N):
        if( a[i] in sic and stack[0] == 0):
                top +=1
                stack[top] = a[i]
        elif(a[i] == '('):
            top+=1
            stack[top] = a[i]
        elif(a[i] == ')'):
            while( stack[top] != '(' ):
                result += stack[top]
                stack[top] = 0
                top -= 1
            stack[top] = 0
            top -= 1
        elif( a[i] == '*'):
            if(stack[top] == '*'):
                result += stack[top]
                stack[top] = a[i]
            else:
                top += 1
                stack[top] = a[i]
        elif(a[i] == '+'):
            if(stack[top] == '('):
                top += 1
                stack[top] = a[i]
            else:
                result += stack[top]
                stack[top] = a[i]
        else:
            result += a[i]
    while top != -1:
        result += stack[top]
        stack[top] = 0
        top -= 1
    for i in range(len(result)):
        if result[i] == '+':
            stack[top - 1] = stack[top - 1] + stack[top]
            top -= 1
        elif result[i] == '-':
            stack[top - 1] = stack[top - 1] - stack[top]
            top -= 1
        elif result[i] == '*':
            stack[top - 1] = stack[top - 1] * stack[top]
            top -= 1
        elif result[i] == '/':
            stack[top - 1] = int(stack[top - 1] / stack[top])
            top -= 1
        else:
            top += 1
            stack[top] = int(result[i])
    print(f'#{t} {stack[0]}')
