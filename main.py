n, k = map(int, input().split)
result = 0

while True:
  target = (n // k) * k
  result += (n - targer)
  n = target

  if n < k:
    break

  result += 1
  n //= k

result += (n - 1)
print(result)