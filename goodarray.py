from typing import List
import sys


def getQueryResult(N: int, queries: List[List[int]]) -> List[int]:
    goodArr = []
    ans = []
    while N > 0:
        p = 0
        while N / 2**p >= 1:
            p += 1
        p -= 1
        goodArr.insert(0, 2**p)
        N -= goodArr[0]
        if N == 0:
            break
    for q in queries:
        l, r, m = q
        tmp = 1
        l -= 1
        r -= 1
        if l < r:
            tmp *= goodArr[l]
            l += 1
        tmp *= goodArr[r]
        ans.append(tmp % m)
    return ans


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    q_num = int(sys.stdin.readline().strip())
    q_sz = int(sys.stdin.readline().strip())
    queries = []
    for i in range(q_num):
        queries.append([int(i) for i in sys.stdin.readline().strip().split()])
    # print(getQueryResult(26, [[1,2,1009],[3,3,5]]))
    print(getQueryResult(N, queries))
