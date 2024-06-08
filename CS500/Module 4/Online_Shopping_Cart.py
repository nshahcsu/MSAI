
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
# Step 2: prompt the user for two items and create two objects of the ItemToPurchase class.
    
# Technique 1: Object creation of class ItemToPurchase using default constructor with default initialized value
item1 = ItemToPurchase()
print('Item 1')
# assign user input value via property assignment
item1.item_name = input('Enter Item Name: \n')
item1.item_price = float(input('Enter Item Price: \n'))
item1.item_quantity = int(input('Enter Item Quantity: \n'))

# Technique 2: Take User Input and store them in local variable.
print('\nItem 2')
in_item_name = input('Enter Item Name: \n')
in_item_price = float(input('Enter Item Price: \n'))
in_item_quantity = int(input('Enter Item Quantity: \n'))

# Object Creation of class ItemToPurchase using parameterized constructor with passing attribute values during initialization
item2 = ItemToPurchase(in_item_name, in_item_price, in_item_quantity)

# Step 3: Add the costs of the two items together and output the total cost

# Invoke print_item_cost() for each object and print item cost.
# Calculate Total Cost and format the output values appropriately.
print('\n-------TOTAL COST---------\n')
item1.print_item_cost()
item2.print_item_cost()
print('\n\tTotal:', '${:.2f}'.format((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)))
print('==============================')
print('Thank you for shopping with us!\n')
 