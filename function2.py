def Addition(No1, No2):             # Function defination
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    # Keyword Arguments
    ret = Addition(No2 = value1,No1 = value2)       # Function call
    print("Addtion is : ",ret)

if __name__ == "__main__":
    main()