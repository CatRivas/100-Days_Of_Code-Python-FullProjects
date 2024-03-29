#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip_porcentage = int(input('What porcentage tip would you like to give? 10, 12 or 15? '))
number_people = int(input('How many people to split the bill? '))

tip = bill * (tip_porcentage / 100)   
total_bill = bill + tip
personal_bill = total_bill / number_people
format_bill = f'{personal_bill:.2f}' #we guarantee that the result has exactly two decimal places.
# format_bill = round(personal_bill,2) don't use round() because there are certain occasions where you round the number does not guarantee that it has two decimal places.

print(f'Each person should pay: ${format_bill}')