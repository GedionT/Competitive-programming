class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        is_prime = [0]*n
        visited = set()
        is_prime[0] = 1
        is_prime[1] = 1
        count = 2

        for i in range(2, n):
            if i**2 > n:
                break
            else:
                if not is_prime[i]:
                    for j in range(i**2, n, i):
                        if j not in visited:
                            is_prime[j] = 1
                            visited.add(j)
                            count += 1
                
        return n - count