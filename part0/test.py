sum = 0
for i in range(1,11):
    if i%2 ==0:
        continue
    if i%10 == 5:
        break

    sum = sum+1
print(sum)
