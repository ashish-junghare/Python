def pattern(i=0):
    if i < 5:
        print("*",end=" ")
        i +=1
        pattern(i)


def main():
    pattern()


if __name__ == "__main__":
    main()