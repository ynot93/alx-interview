#!/usr/bin/python3
"""
The coin change problem
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
