#DSC 510
#Week 3
#Programming Assignment 3.1
#Author: Tim Hollis
#09/24/2025

#Change Control Log:

#Change#:1
#Change: Removed prior change logs, changed made prior to publishing
#Date of Change: 09/24/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/24/2025

#Change#:2
#Change: Replaced flat rate pricing ($0.95/ft) from previous assignment
#        to reflect volume-based discounts and tiered pricing
#Lines Impacted: 48-56
#Date of Change: 09/24/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/24/2025

#Change#:3
#Change: Added proximity alert logic to notify users
#        when they are within 10% of the next pricing tier
#Lines Impacted: 60-77, 114-122
#Date of Change: 09/24/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/24/2025

#Change#:4
#Change: Wrapped feet input and pricing logic in a loop
#        to allow users to revise their purchase amount before payment
#Lines Impacted: 119-120
#Date of Change: 09/24/2025
#Author: Tim Hollis
#Change Approved by: Tim Hollis
#Date Moved to Production: 09/24/2025


#Importing Datetime

from datetime import datetime

from nbclient.client import timestamp

#Welcome message to user

print('Welcome to the Fierce and Fabulous Fiber Optic Cost Calculator')


#Define Pricing Tiers

def tiered_pricing(length):
    if length <= 100:
        return 0.95
    elif length <= 250:
        return 0.85
    elif length <= 500:
        return 0.75
    else:
        return 0.55

#Creating Proximity check and statement if within 10% of next tier

def check_proximity(length):
    tiers=[
        (100,0.95),
        (250,0.85),
        (500,0.75),
        (float('inf'),0.55)
    ]

    for i,(threshold,price) in enumerate(tiers):
        if length<=threshold:
            if i < len(tiers) - 1:
                next_threshold,next_price=tiers[i+1]
                next_tier_start=threshold+1
                feet_needed=next_tier_start-length
                trigger_zone=threshold*0.10
                if 0<feet_needed<=trigger_zone:
                    return f'If you add {feet_needed:.2f} feet you will only pay (${next_price}/ft)'
            break
    return None

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

#Calculate tiered pricing and total cost

while True:
    cost_per_foot=tiered_pricing(feet_requested)
    total_cost=feet_requested*cost_per_foot
    print(f'\nPrice per foot: ${cost_per_foot:.2f}')
    print(f'Total for {feet_requested} feet is ${total_cost:.2f}')

#Check for proximity to price reduction

    proximity_message=check_proximity(feet_requested)
    if proximity_message:
        print(proximity_message)
        revise=input('Would you like to add to your purchase today? (y/n):'
        ).strip().lower()
        if revise=='y':
            feet_requested=float(input('Enter new amount of cable needed in feet: '))
            continue #Allow user to edit the amount they are purchasing
    break #exit the loop if no revision

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

#Receipt inclusion calculations

timestamp=datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
standard_price=0.95
standard_total=feet_requested*standard_price
savings=standard_total-total_cost if feet_requested>100 else 0

#Print receipt

print('\n'+'-'*50)
print('Installation Receipt'.center(50))
print(f'Date and Time: {timestamp}')
print(f'Company Name: {company_name}')
print(f'Length of Fiber Optic Cable Purchased: {feet_requested:.2f} feet')
print(f'Price per foot: ${cost_per_foot:.2f}')
print(f'Total Cost of Installation: ${total_cost:.2f}')
print(f'Cash Rendered: ${cash_rendered:.2f}')
print(f'Change Given: ${change_given:.2f}')

if feet_requested>100:
    print(f'By purchasing {feet_requested:.2f} feet you saved ${savings:.2f}')
print('-'*50)

#Cheeky Gratitude Message

print('Thank you for your payment!')
print('Your Fabulous Fiber Fantasy is now a reality!')
