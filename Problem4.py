import sys
from itertools import permutations
def fo(n):
    m=[i+1 for i in range(n)]
    c=1
    for i in list(permutations(m)):
        temp=0
        for x in m:
            for j in range(len(i)):
                try:
                    if abs(i[j+x]-i[j])==x:
                        temp=1
                        break
                except:
                    continue
        if temp==0:
            print('Arrangement No.'+str(c))
            for j in i:
                print('1 '*(j-1)+'Q '+'1 '*(n-j))
            c+=1
if __name__=='__main__':
    fo(int(sys.stdin.readline().strip()))
