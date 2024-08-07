tc, E = map(int,input().split())
array = list(map(int,input().split()))
G = [[] for _ in range(100)]
for i in range(E):
    v1,v2 = array[i*2], array[i*2+1]
    G[v1].append(v2)

print(G)

for i in range(E*2):
    v1,v2 =
