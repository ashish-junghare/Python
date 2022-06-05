def pattern(value1):
	for i in range(value1):
		for i in range(value1):
			print("*",end=" ")
		print()
	return()

def main():
	no1=int(input("Enter number: "))
	ret=pattern(no1)

if __name__=="__main__":
	main()