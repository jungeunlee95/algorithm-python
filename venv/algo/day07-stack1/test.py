correct = 783
num = 0
while(True):
    S = B = O = 0
    if(correct == num):
        break
    num = int(input())
    a = str(correct)
    b = str(num)

    for i in range(3):
        for j in range(3):
            if b[j] == a[i]:
                if(i==j):
                    S += 1;
                    break
                else:
                    B += 1;
                    break
            elif(j==2):
                O+=1
                break
    print(S,B,O)
