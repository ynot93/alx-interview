#!/usr/bin/python3
"""
Prime Game Module
"""
from typing import List


def isWinner(x: int, nums: List[int]) -> str:
    """
    Return name of the player that won the most rounds
    of the prime game
    """
    def generate_primes(max_n: int) -> List[int]:
        """
        Sieve of Eratosthenes
        """
        is_prime = [True] * (max_n + 1)
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, max_n + 1) if is_prime[p]]
        return primes

    max_n = max(nums)
    primes = generate_primes(max_n)
    maria_won = 0
    ben_won = 0

    for n in nums:
        remaining = set(range(1, n + 1))
        turn = "Maria"
        
        while True:
            available_prime = next((p for p in primes if p in remaining), None)
            
            if available_prime is None:
                if turn == "Maria":
                    ben_won += 1
                else:
                    maria_won += 1
                break
            
            multiple = available_prime
            while multiple <= n:
                if multiple in remaining:
                    remaining.remove(multiple)
                multiple += available_prime
            
            turn = "Ben" if turn == "Maria" else "Maria"

    if maria_won > ben_won:
        return "Maria"
    elif ben_won > maria_won:
        return "Ben"
    else:
        return None
