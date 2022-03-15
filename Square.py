#input: int from 1 - 1,000
#ouput: all perfect squares before that number from least to greatest
n = int(input())
i = 1
while i * i <= n:
    print(i * i)
    i += 1
