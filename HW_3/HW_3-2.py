# =========================
# HW3-2：Two Sum
# =========================


def two_sum_brute(nums, target):
    """
    暴力解：
    使用雙層迴圈檢查任兩個數字。
    時間複雜度 O(N^2)。
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


def two_sum_hash(nums, target):
    """
    效率解：
    使用 dict 記錄看過的數字與 index。
    時間複雜度 O(N)。
    """

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9

print("========== HW3-2：Two Sum ==========")
print("nums =", nums)
print("target =", target)

print("暴力解結果：", two_sum_brute(nums, target))
print("效率解結果：", two_sum_hash(nums, target))