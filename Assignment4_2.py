data1=lambda no1,no2:no1*no2

def main():
    no1=int(input("Enter your number: "))
    no2=int(input("Enter your number: "))
    ret=data1(no1,no2)
    print("multiplication of",no1,"and",no2,"is",ret)



if __name__ == "__main__":
    main()