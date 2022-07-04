


def operation(num1, num2, operation):
	n1=int(num1)
	n2=int(num2)
	if(operation=="+"):
		return n1+n2
	elif (operation=="-"):
		return n1-n2
	elif (operation=="/"):
		return n1/n2	
	elif (operation=="*"):
		return n1*n2	
def main():
	while True:
		num1= input("Enter you First number: ")
		if num1.isdigit():
			break
		else:
			print("\nThat is invalid input , please try again.\n") 
	while True:
		num2= input("Enter you Second number: ")
		if num2.isdigit():
			break
		else:
			print("\nThat is invalid input , please try again.\n") 
	while True:
		operations=["+","-","/","*"]
		_operation= input("What is the Operation (+,-,*,/): ")
		if _operation in operations :
			break
		else:
			print("\nThat operation is not valid, please try again.\n") 
	answer = operation(num1,num2,_operation)
	print(str(answer))
	#write your code here
	pass





if __name__ == '__main__':
	main()
