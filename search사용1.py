from ssearch import seq_search

print('실수를 검색합니다.')
print('주의: \"End\"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1
