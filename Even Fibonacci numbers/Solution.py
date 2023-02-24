
def fibanoci_sequence():
    output = 0
    temp = 0
    fib0 = 1
    fib1 = 1
    n = 0
    a = 0
    while n <4*10**6:

        n=fib0+fib1
        if n%2==0:
            print(n)
            output += n
        temp=n
        fib0 = fib1
        fib1=temp
    print(f"output{output}")
fibanoci_sequence()



