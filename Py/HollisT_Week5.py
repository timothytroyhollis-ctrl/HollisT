#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Course: DSC510
#Week: 5
#Assignment: 5.1 Calc/Avg Tool
#Author: Tim Hollis
#Date: 10/7/2025
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def perform_calculation(operation):
    """Performs arithmetic operation (+, -, *, /) on two user-input numbers."""
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                print('You cannot divide by zero silly, try again')
                return None
            return num1 / num2
        else:
            print('Invalid operation, please try again')
            return None
    except ValueError:
        print('Please enter a valid numeric value')
        return None

def calculate_average():
    """Calculates average of a series of numbers entered by user"""
    try:
        count=int(input('How many numbers would you like to average today? '))
        if count <= 0:
            print('Sorry, you must enter a number greater than 0 ')
            return None

        total=0
        for i in range(count):
            while True:
                try:
                    num=float(input(f'Enter number {i+1}: '))
                    total+=num
                    break
                except ValueError:
                    print('Please enter a valid number')

        average=total/count
        return average
    except ValueError:
        print('Please enter a valid number')
        return None

def main():
    """Entry point for the program"""
    print('='*65)
    print('You are now using the Mathematical Operations and Avg Calculator')
    print('='*65)

    while True:
        print('\nChoose one of the following operations:')
        print('1: Perform basic calculation (+,-,*,/)')
        print('2: Calculate average')
        print('3: To Exit Program')

        choice = input('Enter your choice (1/2/3): ').strip()

        if choice == '1':
            operation=input('Enter operation (+,-,*,/) ').strip()
            result=perform_calculation(operation)
            if result is not None:
                print(f'The result of {operation} operation:{result:.2f}')
        elif choice == '2':
            average=calculate_average()
            if average is not None:
                print(f'The numbers you entered average out to: {average:.2f}')
        elif choice == '3':
            print('Thank you for using this tool, Bye for now!')
            break
        else:
            print('Invalid choice, please enter 1,2,or 3.')

    
if __name__ == '__main__':
    main()
