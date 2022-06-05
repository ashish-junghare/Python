def facto(no):
    if no==0:
        return 1
    a= no* facto(no-1)
    return a

def main():
    value=int(input("Enter value to get factorial: "))
    ret=facto(value)
    print("factorial of {} is {}".format(value,ret))
if __name__ == "__main__":
    main()
