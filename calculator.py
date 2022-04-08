
def main():
	#write your code here
	firstN= input("Enter first number: ")
	secondN= input("Enter second number: ")
	operation= input("Enter the operation (+,-,*,/): ")

	if firstN.isdigit() == False :
		print("Valid Input")
	elif secondN.isdigit() == False :
		print("Valid Input")
    

	elif operation == "+" :
		answer = int(firstN) + int(secondN)
		print("answer is", answer)
	elif operation == "-" :
		answer = int(firstN) - int(secondN)
		print("answer is", answer)
	elif operation == "*" :
		answer = int(firstN) * int(secondN)
		print("answer is", answer)
	elif operation == "/" :
		answer = int(firstN) / int(secondN)
		print("answer is", answer)
	else:
		print("Valid Operation")



	pass
	



if __name__ == '__main__':
	main()
