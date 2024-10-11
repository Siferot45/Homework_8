#validation of input data
def validation_input(number):
    while True:
        try:
            return int(input(number))
        except:
            print("error: Enter the number again. For example (123)") 
            
#input data for comparison
first = validation_input("Enter the first number: ")
second = validation_input("Enter the second number: ")
third  = validation_input("Enter the third number: ")

#checking the equality of numbers
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)