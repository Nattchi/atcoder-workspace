#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
import sys
from typing import List


def is_cross(C: "List[str]", h: int, w: int, d: int) -> bool:
    return C[h][w] == C[h-d][w-d] == C[h-d][w+d] == C[h+d][w-d] == C[h+d][w+d] == "#"


def solve(H: int, W: int, C: "List[str]") -> None:
    N: int = min(H, W)
    ANS: List[int] = [int()] * (N+1)
    for h in range(1, H-1):
        for w in range(1, W-1):
            d: int = 1
            while is_cross(C, h, w, d):
                d += 1
                if d == N:
                    break
            if is_cross(C, h, w, d-1):
                ANS[d-1] += 1
    print(" ".join(map(str, ANS[1:])))


def main() -> None:
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H: int = int(next(tokens))
    W: int = int(next(tokens))
    C: List[str] = [next(tokens) for _ in range(H)]

    solve(H, W, C=C)


if __name__ == '__main__':
    main()