def jump(nums):
    n = len(nums)
    steps = 0
    maxReach = 0
    end = 0

    for i in range(n - 1):
        maxReach = max(maxReach, i + nums[i])

        if i == end:
            end = maxReach
            steps += 1

    return steps
nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))  # saida: 2

nums2 = [2, 3, 0, 1, 4]
print(jump(nums2))  # saida: 2
