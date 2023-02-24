n=10
n_sum = (n**2 +n)/2
out = int(n_sum**2)
for x in range(n+1):
    out -=x**2

print(out)
n =99**99
o = 0
for digit in str(n):
    o+=int(digit)
print(o)
