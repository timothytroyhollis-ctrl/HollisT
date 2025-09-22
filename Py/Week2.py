#DSC 510
#Week 2
#Programming Assignment 2.1
#Author: Tim Hollis
#09/18/2025

#Change Control Log:

#Change#:1
#Change: Implemented while True loop to prevent premature exit
#        when user enters 0 feet; now re-prompts until valid input is received
#Lines Affected: 63-71
#Date of Change: 09/18/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/18/2025

#Change#:2
#Change: Input break statement inside while True loop to allow program to
#        continue when valid input given for number of feet of cable needed
#Lines Affected: 68-71
#Date of Change: 09/18/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/18/2025

#Change#:3
#Changes: Added cash_rendered and change_given input with print statement;
#         includes error message if amount rendered is less than total cost
#Lines Affected: 81-93
#Date of Change: 09/18/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/18/2025

#Change#:4
#Changes: Enhanced receipt with payment details and gratitude message;
#         centered header for improved readability
#Lines Affected: 98-110
#Date of Change: 09/18/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/18/2025

#Change#:5
#Changes: Added payment prompt; cash payment hard-coded as only payment method
#Lines Affected: 75-77
#Date of Change: 09/18/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/18/2025

#Welcome message to user

print('Welcome to the Fierce and Fabulous Fiber Optic Cost Calculator')

#Request the company name from user

company_name=input('Please enter your company name: ')

#Request # of feet from user - include error handling for any amount <0

while True:
    try:
        feet_requested=float(input("Enter fiber optic cable length needed in feet: "))
        if feet_requested<=0:
            print('Sorry, I cannot sell you that amount, please enter a value above zero')
        else:
            break # Valid input-exit the loop
    except ValueError:
        print('Invalid response, please enter a numeric value.')

#Calculate and present total cost

cost_per_foot=0.95
total_cost=feet_requested*cost_per_foot
print(f'Total for {feet_requested:.2f} feet of cable is ${total_cost:.2f}')

# Prompt for payment; cash payment is hard-coded as the only option

while True:
    try:
        cash_rendered=float(input('Enter cash amount rendered: '))
        if cash_rendered<total_cost:
            print('Sorry, insufficient amount to cover the purchase cost')
        else:
            break # Acceptable amount input-exit the loop
    except ValueError:
        print('Invalid response, please enter a numeric value.')

#Calculate Change

change_given=cash_rendered-total_cost

#Print receipt

print('\n'+'-'*50)
print('Installation Receipt'.center(50))
print(f'Company Name: {company_name}')
print(f'Length of Fiber Optic Cable Purchased: {feet_requested:.2f} feet')
print(f'Price per foot: ${cost_per_foot}')
print(f'Total Cost of Installation: ${total_cost:.2f}')
print(f'Cash Rendered: ${cash_rendered:.2f}')
print(f'Change Given: ${change_given:.2f}')
print('-'*50)

#Cheeky Gratitude Message

print('Thank you for your payment!')
print('Your Fabulous Fiber Fantasy is now a reality!')
