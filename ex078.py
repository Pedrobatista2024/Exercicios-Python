num = []
mai = men = 0
for c in range(0,5):
    num.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print(f'O maior numero digitado foi o {mai} nas posições: ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor numero digitadi foi o {men} nas posições: ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end='')