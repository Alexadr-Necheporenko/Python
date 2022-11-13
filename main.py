def maximum(i,j):
    if i>j:
        print(i)
    else:
        print(j)
maximum(8,6)
def minimum_3(i,j,k):
    if i<j and i<k:
        print(i)
    elif j<i and j<k:
        print(j)
    elif k<j and k<i:
        print(k)
    elif i==j==k:
        print('Variables are not entered')
minimum_3(3,3,0)
def module(i):
    if i<0:
        mod=i*(-1)
        print(mod)
    elif i>0:
        print(i)
    elif i==0:
        print('0 no sign')
module(-3)
def summa(i,j):
    amount=i+j
    print(amount)
summa(1,5)
def true_or_false(i):
    if i>0:
        print('Positive x>=0')
    elif i<0:
        print('Negative')
    elif i==0:
        print('Neitral')
true_or_false(0)
