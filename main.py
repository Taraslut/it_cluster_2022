def murder(k, l):
    s = l[k - 1:len(l):k]

    for x in s:
        if x == s[-1]:
            last_element = l.index(s[-1])
        l.remove(x)

    l = l[last_element:] + l[:last_element]

    return l


n = int(input('к-сть людей '))
k = int(input('step '))
l = [i for i in range(1, n + 1)]

while len(l) > k - 1:
    l = murder(k, l) + l

if len(l) == 2:
    l.pop(0)
if len(l) == 3:
    l.pop(0)
    l.pop(1)
if len(l) == 4:
    l.pop(0)
    l.pop(1)
    l.pop(1)
print(f'залишився - {l}')
