lines = open("distancedump.txt")
count = 0
arr = lines.read().split("\n")
del arr[-1]
for line in arr:
    #print(line)
    count += float(line)
arr.sort()
print("Median: " + str(arr[int(len(arr)/2)]))
print("Mean: " + str(count/len(arr)))
print("Total: " + str(len(arr)))