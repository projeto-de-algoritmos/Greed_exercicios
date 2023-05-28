def minCandies(ratings):
    n = len(ratings)
    candies = [1] * n

    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    return sum(candies)


ratings1 = [1, 0, 2]
print(minCandies(ratings1))  # saida: 5

ratings2 = [1, 2, 2]
print(minCandies(ratings2))  # saida: 4
