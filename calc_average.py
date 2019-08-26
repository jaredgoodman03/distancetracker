lines = open("distancedump.txt")
count = 0
arr = lines.read().split("\n")
nums = []
del arr[-1]
for line in arr:
    #print(line)
    count += float(line)
    nums.append(float(line))
nums.sort()
print(nums)
print("Median: " + str(nums[int(len(nums)/2)]))
print("Mean: " + str(count/len(arr)))
#print("Average gas used: " + str((1/24.7)*arr[int(len(arr)/2)]) + " gallons")
print("Total: " + str(len(arr)))