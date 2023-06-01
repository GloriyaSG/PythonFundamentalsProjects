divisor = int(input())
boundary = int(input())
maxnum = 0
for n in range(1,boundary+1):
    if n % divisor == 0:
        if maxnum <= n:
            maxnum = n
print(maxnum)