n = 9

for _ in range(int(input())):
g = []

for i in range(n):
c = list(input())

g.append(c)

for k in range(n):
if k == 0: g[0][0] = ['1', '2'][g[0][0] == '1']
if k == 1: g[1][4] = ['1', '2'][g[1][4] == '1']
if k == 2: g[2][8] = ['1', '2'][g[2][8] == '1']
if k == 3: g[3][1] = ['1', '2'][g[3][1] == '1']
if k == 4: g[4][3] = ['1', '2'][g[4][3] == '1']
if k == 5: g[5][6] = ['1', '2'][g[5][6] == '1']
if k == 6: g[6][2] = ['1', '2'][g[6][2] == '1']
if k == 7: g[7][5] = ['1', '2'][g[7][5] == '1']
if k == 8: g[8][7] = ['1', '2'][g[8][7] == '1']

for i in g:
print(*i, sep='')