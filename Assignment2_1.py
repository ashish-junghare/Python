import Arithmetic as arr

def main():
    no1 = int(input("Enter first  number: "))
    no2 = int(input("Enter Second  number: "))

    ret = arr.Add(no1, no2)
    print("Addition is : ", ret)


    ret = arr.Sub(no1, no2)
    print("Substraction is : ", ret)

    ret = arr.Mult(no1, no2)
    print("Multiplication is : ", ret)

    ret = arr.Div(no1, no2)
    print("Division is : ", ret)


if __name__ == "__main__":
    main()