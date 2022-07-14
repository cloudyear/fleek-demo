from typing import List


def cardinalitySorting(nums: List[int]) -> List:
    # tmp = [bin(i).count("1") for i in nums]
    # _, res = zip(*sorted(zip(tmp, nums)))
    # return list(res)
    tmp = [(i, bin(i).count("1")) for i in nums]
    res = sorted(tmp, key=lambda x: (x[1], x[0]))
    return [i[0] for i in res]


print(cardinalitySorting([1, 2, 3, 4]))

# substring lc 647
# subsequence lc 730
