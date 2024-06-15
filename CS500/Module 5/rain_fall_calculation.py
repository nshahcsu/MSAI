'''Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
'''

import statistics

dict_month = {	'01':'January',
		        '02':'February',
		        '03':'March',
		        '04':'April',
		        '05':'May',
		        '06':'June',
		        '07':'July',
		        '08':'August',
		        '09':'September',
		        '10':'October',
		        '11':'November',
		        '12':'December'		}
MAX_YEARS = 100
lst_rainfall =[]
total_number_of_months = 0
try:
    number_of_years = int(input('Please Enter number of Years to calculate Rainfall Stats.\n'))
    if(0 < number_of_years < MAX_YEARS):
        for year in range(1, number_of_years+1):
            for month in dict_month.values():
                print('Please Enter Rainfall for Year:', year, 'and Month:', month)
                inches_rain = float(input())
                lst_rainfall.append(inches_rain)
                total_number_of_months += 1
    else:
        print("Invalid Entry. (Please try again and enter whole number between 0 and 100.)")


    print('\t      __   _')
    print('\t    _(  )_( )_')
    print('\t   (_   _    _)')
    print('\t  / /(_) (__)')
    print('\t / / / / / /')
    print('\t/ / / / / /')
    print('===== Rain Statistics =====\n')
    print('Total Number of Months:', total_number_of_months)
    print('Total rainfall (in', number_of_years, 'year(s)):', round((sum(lst_rainfall)),2), 'inch(es)')
    print('Average rainfall:', round((statistics.mean(lst_rainfall)),2), 'inch(es) per month \n')

except:
    print('Error!! Invalid Entry. Please try again.')
# https://docs.python.org/3/library/statistics.html
# https://www.geeksforgeeks.org/python-statistics-mean-function/
#
