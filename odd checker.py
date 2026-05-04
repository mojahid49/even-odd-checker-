#even/odd checker 

num =int(input("Enter your number: "))

if num%2 == 0:
	print("The number you entered is even.")
elif num%2 != 0:
	print("The number you entered is odd.")
else:
	print("Invalid number.")
	
while True:
	try:
		num = int(input("Enter your number: "))
	except ValueError:
		print("please Enter valid numbers!")
		
		choice =input("Do you wanna continue? yes/no: ")
		if choice != "yes":
			print("Bye bro! ")
			break

