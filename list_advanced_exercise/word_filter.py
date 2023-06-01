text = input().split()
filtered = [print(x) for x in text if len(x) % 2 == 0]