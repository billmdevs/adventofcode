import os

curdir = os.getcwd()
fp = os.path.join(curdir, 'input_files', 'advcode2')

ans = 0

with open(fp, "r") as nuclear:
    reports = nuclear.read().strip().split('\n')

def is_safe(nums):
    inc = nums[1] > nums[0]
    if inc:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if not -3 <= diff <= -1:
                return False
        return True
# This is really slow!!! To improve it I think you could do a dynamic program where the state is (index in sequence, allowed to remove, is increasing). you have to check if the subsequence of everything up till before the last index is safe, and whether the last gap is good. if it's not, try removing the last or second-to-last index (if you're allowed to).

def is_really_safe(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False


for line in reports:
    nums = [int(i) for i in line.split()]
    ans += is_really_safe(nums)

print(ans)

