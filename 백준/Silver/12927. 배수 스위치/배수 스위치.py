arr = list(input())

check = True
answer = 0
length = len(arr)
switch_list = [0] * length

for i in range(length):
    if arr[i] == 'Y':
        switch_list[i] = 1
for i in range(length):
    if switch_list[i] == 1:
        for j in range(length):
            if (j+1) % (i+1) == 0:
                if switch_list[j] == 0:
                    switch_list[j] = 1
                else:
                    switch_list[j] = 0
        answer += 1
print(answer)
