import sys
sys.stdin = open("3_이진탐색", "r")

T = int(input())
for t in range(1, T+1):
    a = int(input())
    b = [i for i in range(1, a+1) ]

    ans1 = b[a//2]

    first = 0
    last = a-1
    cnt = 0
    while(cnt != a//2):

    print(f"#{t} {ans1}")
