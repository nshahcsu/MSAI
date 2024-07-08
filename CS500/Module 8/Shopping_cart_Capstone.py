

# Define a class ItemToPurchase with Attributes Item Name, Item Price, Item Quantity, Item Description
# Step 1

class ItemToPurchase:
    item_name : str
    item_price : float
    item_quantity : int
    description : str

    # Constructor with 4 parameters with initialized values
    def __init__(self, name = 'none', price = 0, quantity = 0, description = ''):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.description = description

    # Method for calculating cost of one item for given quantity at user provided value and Print them.
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', '${:.2f}'.format(self.item_price), '=', '${:.2f}'.format(self.item_price * self.item_quantity))

# Define Class with Attributes Customer Name, Current Date, Cart Items List
# Step 4

class ShoppingCart:
    customer_name : str
    current_date : str
    cart_items = []

    # Default Constructor to initialize customer name and date
    def __init__(self, name='none', date = 'January 1,2020'):
        self.customer_name = name
        self.current_date = date
    
    # Method to Add an item to Cart Items List. Parameter - ItemtoPurchase
    def add_item(self,temp_item):
       self.cart_items.append(temp_item)

    # Method to Modify an item. 
    def modify_item(self,temp_item):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == temp_item.item_name:
                if( int(temp_item.item_price) != 0):
                    self.cart_items[i].item_price = temp_item.item_price
                if( temp_item.item_quantity != 0):
                    self.cart_items[i].item_quantity = temp_item.item_quantity
                if( temp_item.description != ''):
                    self.cart_items[i].description = temp_item.description
                #shopping_cart.cart_items.update(temp_item)
                item_found = True
                break
        if(not item_found):
            print('Item not found in cart.')

    # Method to Remove an item.
    def remove_item(self,rmv_item):
        item_found = False
        for i in range(len(self.cart_items)):            
            if self.cart_items[i].item_name == rmv_item:
                del self.cart_items[i]
                item_found= True
                break
        if(not item_found):
            print('Item not found in cart.')

                
    # Method to get total number of items in the cart.
    def get_num_items_in_cart(self):
        total_count = 0
        for item in self.cart_items:
            total_count += item.item_quantity
        return total_count
    
    # Method to Calculate total cost.
    def get_cost_of_cart(self):
        Total_Cost = 0
        for item in self.cart_items:
            Total_Cost += (item.item_price * item.item_quantity)
        return Total_Cost

    # Method to Print Cart Information and Total.
    def print_total(self):
        total_cart_Cost = 0
        total_cart_Cost = self.get_cost_of_cart()
        # Invoke print_item_cost() for each object and print item cost.
        # Calculate Total Cost and format the output values appropriately.
        
        print(shopping_cart.customer_name,'\' Shopping Cart -', self.current_date)
        if self.cart_items:
            print('\tNumber of Items:', self.get_num_items_in_cart())
            for item in shopping_cart.cart_items:
                item.print_item_cost()
            print('\n\tTotal:', '${:.2f}'.format(total_cart_Cost))
            print('==============================')
            print('Thank you for shopping with us!\n')
        else:
            print('SHOPPING CART IS EMPTY.')
    
    # Method to print description of cart items.
    def print_descriptions(self):
        #print('\tOUTPUT ITEMS\' DESCRIPTIONS')
        print(self.customer_name +'\'s Shopping Cart -', self.current_date)
        if self.cart_items:
            print('\tItem Descriptions')
            for item in self.cart_items:
                print(item.item_name, ':', item.description)
        else:
            print('SHOPPING CART IS EMPTY.')


# Main Area
# Method to print Menu    
def print_menu(obj_cart):
    print('\t\tMENU\n')
    print('\ta - Add item to cart')
    print('\tr - Remove item from cart')
    print('\tc - Change item quantity')
    print('\ti - Output items \'descriptions\'')
    print('\to - Output shopping cart')
    print('\tq - Quit')
    print('\t\tChoose an option:\n')


        
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
c_name = input('Please Enter your Name: ')
c_date = input('Please type current date (in the format - January 1, 2020) ')

MAX_ITEM = 10
item_count = 0

if(c_name or c_date):  
    shopping_cart = ShoppingCart(c_name,c_date)
else:
    shopping_cart = ShoppingCart()

print('Customer Name:', shopping_cart.customer_name)
print('Today\'s Date:', shopping_cart.current_date)

while (item_count< MAX_ITEM):
    print_menu(shopping_cart)
    user_input = input().lower()
    if user_input == 'a':
        temp_item = ItemToPurchase()
        # assign user input value via attribute assignment
        try:
            print('ADD ITEM TO CART')
            temp_item.item_name = input('Enter the item Name: \n')
            temp_item.description = input('Enter the item description:\n')
            temp_item.item_price = float(input('Enter the item Price: \n'))
            temp_item.item_quantity = int(input('Enter the item Quantity: \n'))
            shopping_cart.add_item(temp_item)
            item_count += 1
        except:
            print('Invalid Input.')
    elif user_input == 'r':
        print('REMOVE ITEM FROM CART')
        rm_item = input('Enter name of item Name to remove.\n')
        shopping_cart.remove_item(rm_item)
    elif user_input == 'c':
        temp_item = ItemToPurchase()
        # assign user input value via attribute assignment
        try:
            print('CHANGE ITEM QUANTITY')
            temp_item.item_name = input('Enter the item name: \n')
            temp_item.item_quantity = int(input('Enter the new quantity: \n')) 
        except:
            print('Invalid Input.')

        shopping_cart.modify_item(temp_item)
    elif user_input == 'i':
        print('\tOUTPUT ITEMS\' DESCRIPTIONS')
        shopping_cart.print_descriptions()
    elif user_input == 'o':
        print('\tOUTPUT SHOPPING CART')
        shopping_cart.print_total()
    elif user_input == 'q':
        print('You have selected to Exit.')
        print('Thank you for shopping with us!\n')
        break
    else:
        print('Please select valid input or press q to Quit.')
