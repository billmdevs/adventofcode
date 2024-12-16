import os

curdir = os.getcwd()
fp = os.path.join(curdir, 'input_files', 'advcode2test')

safe = 0
unsafe = 0

with open(fp, "r") as nuclear:
    reports = nuclear.readlines()

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

for line in reports:
    nums = [int(i) for i in line.split()]
    ans += is_safe(nums)

print(ans)

