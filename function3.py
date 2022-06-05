# Default arguments
def Area(PI = 3.14, radius):
    ans = 0.0
    ans = PI * radius * radius
    return ans

def main():
    print("Enter radius of circle")
    value = float(input())

    ret = 0.0
    ret = Area(radius = value)
    # ret = Area(PI = 7.10, radius = value)

    print("Area of circle is : ",ret)

if __name__ == "__main__":
    main()