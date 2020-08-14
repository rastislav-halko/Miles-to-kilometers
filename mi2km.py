#1. prompt user to enter number of miles in a float form (decimals allowed):
miles = input('Enter a distance in miles: ')

#2. convert string input entered by user to a number (integer):
miles_float = float(miles)

#3. convert the miles-to-km multiplier from string to float:
multiplier = float(1.609344)

#4. actual conversion:
kilometers_value = (miles_float * multiplier)

#5. Final output prints out the amount of miles entered by the user in the form of a string (since we are using the miles variable instead of miles_float) plus value of kilometers converted from float back to a string. Finally the word kilometers is added to conclude the output:
print(miles + ' miles equals ' + str(kilometers_value) + ' kilometers.')
