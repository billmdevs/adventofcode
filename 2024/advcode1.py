import os
from collections import Counter

curdir = os.getcwd()
fp = os.path.join(curdir, 'input_files', 'advcode1')

nums1, nums2 = [], []
with open(fp, 'r') as nums:
    for num in nums:
        nums1.append(int(num.split()[0]))
        nums2.append(int(num.split()[1]))

#print(nums1)
#print("*********************************************************************************************************************")
#print(nums2)

#nums1 = sorted(nums1)
#nums2 = sorted(nums2)
#distance = []
#for n1, n2 in zip(nums1, nums2):
#    distance.append(abs(n1 - n2))

#pairsum = sum(distance)

#print(pairsum)

count = Counter(nums2)
sim_score = [n1*count[n1] for n1 in nums1]
#print(sum(sim_score))
print(sim_score)

