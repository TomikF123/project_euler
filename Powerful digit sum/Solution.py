a=2
b=1
idk = []


def sum_of_digits(i):
    output = 0
    i = str(i)

    for n in i:
        output += int(n)
    return output
for n in range(99):

    for j in range(99):
        x = (a+n)**(b+j)
        idk.append(sum_of_digits(x))


print(idk)
print(max(idk))


input = "  "
