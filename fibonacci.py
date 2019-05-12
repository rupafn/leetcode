import array
mem = [i for i in range(100)];
def fib(n):
    if(n==0):
        mem[0]= 1
    elif(n==1):
        mem[1]=1;
    else:
        result = fib(n-1)+fib(n-2);
        mem[n] = result;
        return result

print(fib(0));
