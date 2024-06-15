
def calculate_points(books_this_month):
    if(0 < books_this_month < 2):
        return 0
    elif(2 <=  books_this_month < 4):
        return  5
    elif(4 <= books_this_month < 6):
        return 15
    elif(6 <= books_this_month < 8):
        return 30
    elif(books_this_month >= 8):
        return  60
    else:
        print('Error: Invalid Entry.')

try:
    i_books_this_month = int(input('Please Enter number of books purchased this month:'))
    points_earned = calculate_points(books_this_month=i_books_this_month)
    print('\t   ,')
    print('\t__/ \__')
    print('\t\     /')
    print('\t/_   _\\')
    print('\t  \\ /')
    print('===== Rewards Summary ======\n')
    print('Points Earned this month:', points_earned )
    print('\nEnjoy Reading the books! Thank you!\n')
except:
    print('Incorrect Input. Please try again and enter a valid number for booked purchased in this month.')

# https://www.w3schools.com/python/python_functions.asp
# 