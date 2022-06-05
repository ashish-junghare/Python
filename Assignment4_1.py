data1=lambda no1:no1**2

def main():
    no1=int(input("Enter your number: "))
    ret=data1(no1)
    print("power of 2 of",no1,"is",ret)



if __name__ == "__main__":
    main()