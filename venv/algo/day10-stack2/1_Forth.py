'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다.
예를 들어 3+4는 다음과 같이 표기한다.

3 4 + .

Forth에서는 동작은 다음과 같다.
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오.
만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
'''
import sys

sys.stdin = open("1_Forth", "r")

T = int(input())
for t in range(1, T+1):

    a = input().split()
    b = ['-', '+', '/', '*']
    stack = [0] * len(a)
    top = -1

    for i in range(len(a)):
        if(len(a)==3 and a[1] in b and a[0] not in b):
            if(a[1]=='+'):
                print(f"#{t} {a[0]}")
                break
            elif (a[1] == '-'):
                print(f"#{t} -{a[0]}")
                break
            else:
                print(f"#{t} error")
                break

        if(a[i] == '.'):
            print(f"#{t} {stack[top]}")
            break
        if(a[i] not in b):
            top += 1
            stack[top] = int(a[i])
        else:
            if(top < 1):
                print(f"#{t} error")
                break
            else:
                num1 = stack[top]
                num2 = stack[top-1]
                stack[top - 1] = 0
                stack[top] = 0
                top -= 1
                if(a[i] == '+'):
                    stack[top] = num2 + num1
                elif (a[i] == '-'):
                    stack[top] = num2 - num1
                elif (a[i] == '/'):
                    stack[top] = num2 // num1
                elif (a[i] == '*'):
                    stack[top] = num2 * num1


