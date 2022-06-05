def prime(value1):
	if value1 > 1:
		for i in range(2, value1):
			if (value1 % i) == 0:
				print("It is not a prime value")
				break
		else:
			print("It is a prime value")

	else:
		print("It is not a prime value")
		return()


def main():
    no1 = int(input("Enter any number : "))
    ret = prime(no1)


if __name__ == "__main__":
    main()