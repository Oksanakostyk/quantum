
#Variant_1
def calc_sum1(n):
    sum1=0
    for i in range (1,n+1):
        sum1+=i
    return sum1

#Variant_2
def calc_sum(n):
    s=(x for x in range (1,n+1))
    return sum(s)

if __name__ == '__main__':
    n=int(input(''))
    print(calc_sum1(n))
    print(calc_sum(n))