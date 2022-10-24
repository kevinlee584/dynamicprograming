from functools import reduce

def Factorial(a):
    return 1 if a <= 0 else reduce((lambda x, y: x * y), range(1, a+1))

def C(x, y):
    a, b, c = Factorial(x), Factorial(y), Factorial(x-y)

    return int(a / (b * c))
'''
t(b, n, k) 指的是在n個stack中，至少有一個stack裡面有k個robots的分法。
因此，要計算一個stack有k個robots、兩個stack有k個robots、三個stack有k個robots......
的總和次數
'''

def t(b, n, k):
    i, j = 1, 0

    while i * k <= b:
        j += solve(b-k*i, n-i, k-1) * C(n, i)
        i += 1
    
    return j

def solve(b, n, k):
 
    if b <= k:
        return C(n+b-1, b)

    elif k == 1:
        return C(n, b)

    else:
        return solve(b, n, k-1) + t(b, n, k)


if __name__ == '__main__' :

    print("(%d, %d, %d) = %d" % (3, 4, 2, solve(3, 4, 2), ))
    print("(%d, %d, %d) = %d" % (10, 10, 5, solve(10, 10, 5), ))
    print("(%d, %d, %d) = %d" % (10, 5, 4, solve(10, 5, 4), ))

