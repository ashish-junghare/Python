def num(i):
    if i <= 5:
        print(i,end=" ")
        i +=1
        num(i)


def main():
    num(1)


if __name__ == "__main__":
    main()