import sys
import math

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    nums = [int(line.strip()) for line in file]
    result_digit = round(sum(nums)/len(nums))
    count = 0

    for id, i in enumerate(nums):
        while i != result_digit:
            if i < result_digit:
                i += 1
                count += 1
            elif i > result_digit:
                i -= 1
                count += 1
            else:
                nums[id] = i

print(int(count))
