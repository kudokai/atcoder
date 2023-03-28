'''
Created on 2019/07/08

@author: B4
'''

mod = 1e9+7

if __name__ == '__main__':
    n, k = map(int, input().split())
    if k>(n-1)*(n-2)//2:
        print(-1)
    else:
        edge = [[] for i in range(n+1)]
        for i in range(2,n+1):
            edge[1].append(i)
            edge[i].append(1)
        #print(edge[1:])
        for i in range(1,(n-1)*(n-2)//2-k+1):
            j = 2
            k = i
            while(j+k>n):
                k -= n-j
                j += 1
            edge[j].append(j+k)
            edge[j+k].append(j)
            
#         print(edge[1:])
        out_u = []
        out_v = []
        for i in range(1,n+1):
            for j in edge[i]:
                out_u.append(i)
                out_v.append(j)
                edge[j].remove(i)
        for i in range(len(out_u)):
            print(out_u[i], out_v[i])
    