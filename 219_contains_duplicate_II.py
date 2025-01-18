from typing import List


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    last_seen = {}
    i = 0
    for num in nums:
        if num in last_seen:
            if i - last_seen[num] <= k:
                return True
        last_seen[num] = i
        i += 1

    return False
