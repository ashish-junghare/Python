def pattern(value1):
	for i in range(1,value1+1):
		for i in range(1,value1+1):
			print(i,end=" ")
		print()
	return()

def main():
	no1=int(input("Enter number: "))
	ret=pattern(no1)

if __name__=="__main__":
	main()