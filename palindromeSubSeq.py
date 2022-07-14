import time


def method1():
    candidates = set(
        ["11111", "00000", "10101", "01010", "00100", "11011", "10001", "01110"]
    )

    c = 0

    def backtracking(path, k, s, collect, startidx):
        nonlocal c
        if len(path) == k:
            if path in candidates:
                c += 1
                collect.append(path)
            return
        for i in range(startidx, len(s)):
            path += s[i]
            backtracking(path, k, s, collect, i + 1)
            path = path[:-1]

    def getPalindromeCount():
        nonlocal c
        s = "10100010111000100100101011110001001000100000000111100100100111"
        res = []
        backtracking("", 5, s, res, 0)
        # print(res)
        # print(c)
        return c

    print(getPalindromeCount())


def method2():
    def getPalindromeCount(s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for sz in range(3, n):
            for i in range(0, n - sz + 1):
                j = i + sz - 1
                dp[i][j] = dp[i][j - 1]
                if dp[i + 1][j] != dp[i + 1][j - 1]:
                    dp[i][j] += dp[i + 1][j] - dp[i + 1][j - 1]
                if s[i] == s[j]:
                    dp[i][j] += j - i - 1
        for i in range(0, n):
            for j in range(i + 4, n):
                if s[i] == s[j]:
                    res += dp[i + 1][j - 1]
        return res

    print(
        getPalindromeCount(
            "10100010111000100100101011110001001000100000000111100100100111"
        )
    )


if __name__ == "__main__":
    t = time.time()
    # method1()
    method2()
    print(time.time() - t)
