#!/usr/bin/env python3
import sys
from typing import List


def check(X: int, K: int, A: List[int]) -> bool:
    count = 0
    for a in A:
        count += X // a
        if count >= K:
            return True
    return False


def solve(N: int, K: int, A: "List[int]"):
    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, K, A):
            right = mid
        else:
            left = mid
    print(right)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N: int = int(next(tokens))
    K: int = int(next(tokens))
    A: "List[int]" = [int(next(tokens)) for _ in range(N)]
    solve(N, K, A)


if __name__ == '__main__':
    main()
