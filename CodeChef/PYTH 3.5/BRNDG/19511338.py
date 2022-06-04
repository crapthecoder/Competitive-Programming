from itertools import combinations as comb

for _ in range(int(input())):
    n = int(input())

    lis = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
           1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912,
           1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472,
           274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416,
           35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624,
           2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968,
           72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488]

    numbers = lis[:lis.index(min(lis, key = lambda x: abs(x - n))) + 1]
    print(len([seq for j in range(len(numbers), 0, -1) for seq in comb(numbers, j) if sum(seq) == n][0]))