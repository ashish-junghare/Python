def num(no):
    if no>0:
        print(no,end=" ")
        no=no-1
        num(no)

def main():
    num(5)
if __name__ == "__main__":
    main()