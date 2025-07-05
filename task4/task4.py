import sys
import statistics

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    nums = [int(line.strip()) for line in file if line.strip()]

median = statistics.median(nums)
moves = sum(abs(num - median) for num in nums)

print(int(moves))
