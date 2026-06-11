def twoSum( nums: list[int], target: int) -> list[int]:
    i = 0
    data = {}
    for n in nums:
        req = target - n
        if req in data:
            return [data[req],i]
        data[n] = i
        i+=1
print(twoSum([3,3],6))