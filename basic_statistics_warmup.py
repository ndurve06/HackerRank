# Enter your code here. Read input from STDIN. Print output to STDOUT

#arr = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
#length = len(arr)

length = int(input())
arr = list(map(int, input().split()))
mean = sum(arr)/length
median = 0
mode = 0
sd = 0
lb = 0
ub = 0

median_list = arr
median_list.sort()
if length % 2 == 1:
    median = median_list[length//2]
else:
    median = (median_list[length//2 - 1 ] + median_list[length//2]) / 2

counter = {}
for num in arr:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

ordered = sorted(counter.items(), key=lambda x: x[1], reverse=True)
mode = ordered[0][0]

for i in range(length):
    sd += (arr[i] - mean)**2
sd = (sd/length)**0.5

se = sd/(length**0.5)
z_critical = 1.96
lb = mean - z_critical * se
ub = mean + z_critical * se

print(round(mean, 1))
print(round(median, 1))
print(mode)
print(round(sd, 1))
print(round(lb, 1), round(ub, 1))