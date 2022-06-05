def fact(value1):
    i = 0
    factors=[1]
    for i in range(2,value1):
        if value1%i==0:
            factors.append(i)
    return sum(factors)

def main():
    no1 = int(input("Enter any number: "))
    ret = fact(no1)
    print("Addition of all factors is: ",ret)

if __name__ == "__main__":
    main()