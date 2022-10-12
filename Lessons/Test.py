st = input()
shab = {i: st.count(i) for i in st}

n = int(input())
temp = {}
for _ in range(n):
    lst = input().split(': ')
    temp[int(lst[1])] = lst[0]

for key, value in shab.items():
    shab[key] = temp[value]

total = ''
for s in st:
    total += shab[s]

print(total)