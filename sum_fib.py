fib = [0] * 51
fib[1] = 1

sum = fib[0] + fib[1]

for i in range(2, 51):
  fib[i] = fib[i - 1] + fib[i - 2]
  sum = sum + fib[i]

print(sum)