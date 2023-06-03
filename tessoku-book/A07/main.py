#!/usr/bin/env python3
import sys


def solve(D: int, N: int, L: "List[int]", R: "List[int]"):
    candidates = [int()] * (D+2)
    for i in range(N):
        candidates[L[i]] += 1
        candidates[R[i]+1] -= 1
    for day in range(1, D+1):
        candidates[day] += candidates[day-1]
        print(candidates[day])

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(D, N, L, R)

if __name__ == '__main__':
    main()