def digits(value1):
    sum = 0
    for digit in str(value1):
        sum = sum + int(digit)
    return (sum)

def main():
    no1 = int(input("Enter any number: "))
    ret = digits(no1)
    print("Addition of digits is:",ret)

if __name__ == "__main__":
    main()