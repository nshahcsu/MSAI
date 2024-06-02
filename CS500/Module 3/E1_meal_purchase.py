# program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then 
#calculate the amounts with an 18 percent tip and 7 percent sales tax. 
#Display each of these amounts and the total price.

#Global Variable Section. 

# Sales Tax and Tip are set globally so, we can leverage this variable everytime we need to use them.
# In future, if any of these changes, we have to update here. All other calculations remains the same.
# increases readability and reduce number of code lines to change/review for maintenance.

SALES_TAX = 0.07
TIP = 0.18


food_cost = float(input('Enter the charge for the food:') )
tip = food_cost * TIP
tax = food_cost * SALES_TAX
 

print('\n\tRECEIPT')
print('------------------------')
print('Food Charge \t:', '${:.2f}'.format( food_cost))
# Add a gratuity, sales tax and  total to the receipt
print('Tip (18%)\t:' , '${:.2f}'.format(tip))
print('Sales Tax (7%)\t:' , '${:.2f}'.format(tax))
print('--------------------------')
print('Total Price\t:', '${:.2f}'.format(food_cost + tip + tax))

print('\n===============================================')
print('Thank you for your business! Have a good day!')
print('===============================================')