a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c < a:
    a, c = c, a
if a > b:
    a, b = b, a
print(a, b, c)
