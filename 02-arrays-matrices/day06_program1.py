def reverse_list(nums: list, start: int, end: int) -> None:
    """Reverse nums in place between indices start and end (inclusive)."""
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate_array(nums: list, k: int) -> list:
    """Rotate the list to the right by k positions (in place)."""
    if not nums:
        return []

    n = len(nums)
    k = k % n  # handles k larger than the list length

    reverse_list(nums, 0, n - 1)  # 1. reverse the whole list
    reverse_list(nums, 0, k - 1)  # 2. reverse the first k elements
    reverse_list(nums, k, n - 1)  # 3. reverse the remaining n-k elements
    return nums


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shift = 3
    result = rotate_array(num_list, shift)
    print(f"The rotated list result: {result}")