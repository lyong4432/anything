# 비효율적인 코드
for i in range(1,13):
    if i == 8:
        continue
    print(i, end = ' ')

print()
# 효율적인 코드 
for i in list(range(1,8)) + list(range(9,13)):
    print(i, end = ' ')

print()
