from collections import defaultdict

s = "abdwoeiafhnhubgbtgjatgbabgjbuofbahurfbyuagvrfaerfh"


def findMaxFreq(s: str) -> str:
    if not s:
        return ""
    maxFreq = 1
    pos = 0
    map = defaultdict(int)
    posMap = dict()
    for i, c in enumerate(s):
        if not posMap.get(c):
            posMap[c] = i
        map[c] += 1
        if map[c] > maxFreq:
            pos = i
            maxFreq = map[c]
        elif map[c] == maxFreq:
            if pos > posMap[c]:
                pos = i
                maxFreq = map[c]
    return s[pos], maxFreq


print(findMaxFreq(s))
