import sys
import math

input = sys.stdin.readline

def isValid(r1,r2,r3):
    if not (str(math.sqrt(r1[0]*r1[1]+r2[0]*r2[1]+r3[0]*r3[1])).isdigit()):
        return False
    else:
    
 



    
    


t = int(input())

for _ in range(t):
    l = list(map(int,input().split()))
    r1 = l[:2]
    r2 = l[2:4]
    r3 = l[4:]
    if isValid(r1,r2,r3):
        print("YES")
    else:
        print("NO")

