x = 10
y = 15
z = 10.0  # even though it is a float it is equivalent to x

print(x > y)  # False
print(y > x)  # True

if (x > y):
    print('X is bigger than y!')
else:
    print('Y is bigger or equal to X!')
