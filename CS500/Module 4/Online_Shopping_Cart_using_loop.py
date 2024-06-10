
# Define a class ItemToPurchase with attributes item_name (string), item_price (float), item_quantity (int)
# Default constructor Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method print_item_cost()

# Step 1: Define a class ItemToPurchase  
class ItemToPurchase:
    item_name : str
    item_price : float
    item_quantity : int

    # Constructor with 3 parameters with initialized values
    def __init__(self, name = 'none', price = 0, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    # Method for calculating cost of one item for given quantity at user provided value and Print them.
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', '${:.2f}'.format(self.item_price), '=', '${:.2f}'.format(self.item_price * self.item_quantity))


print('\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠈⢻⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⢻⡏⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⣹⠇⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣀⣀⣀⣸⣧⣀⣀⣀⣀⣿⣄⣀⣀⣀⣠⡿⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⣿⠃⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣤⣼⣧⣤⣤⣤⣤⣿⣤⣤⣤⣼⡏⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠤⠼⠷⠤⠤⠤⠤⠿⠦⠤⠾⠃⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⢶⣶⠶⠶⠶⠶⠶⠶⣶⠶⣶⡶⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣠⡿⠀⠀⠀⠀⠀⠀⢷⣄⣼⠇⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

print('\n\tWelcome to the Online Shopping Cart')

# Step 2: prompt the user for multiple items and create multiple objects of the ItemToPurchase class.
MAX_ITEM = 10
item_count = 0
items = []
while (item_count< MAX_ITEM):
    temp_item = ItemToPurchase()
    item_count += 1
    print('\nItem', item_count)
    # assign user input value via attribute assignment
    temp_item.item_name = input('Enter Item Name: \n')
    temp_item.item_price = float(input('Enter Item Price: \n'))
    temp_item.item_quantity = int(input('Enter Item Quantity: \n'))
    items.append(temp_item)
    
    if(item_count< MAX_ITEM):
        user_input = input('Do you want to add more item to the cart? (Y/N)\n')
        if(user_input == 'Y' or user_input == 'y'):
            continue
        elif (user_input == 'N' or user_input == 'n'):
            break
        else:
            user_input = input('Invalid Entry. Please select Type Y/N.\n')
            if(user_input == 'Y' or user_input == 'y'):
                continue
            else:
                break
            


# Step 3: Add the costs of the two items together and output the total cost

Total_Cost = 0
# Invoke print_item_cost() for each object and print item cost.
# Calculate Total Cost and format the output values appropriately.
print('\n-------TOTAL COST---------\n')
for item in items:
    item.print_item_cost()
    Total_Cost += (item.item_price * item.item_quantity)

print('\n\tTotal:', '${:.2f}'.format(Total_Cost))
print('==============================')
print('Thank you for shopping with us!\n')
 