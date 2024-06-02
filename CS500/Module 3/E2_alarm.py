#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
#Write a Python program to solve the general version of the above problem. 
#Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
#The program should output what the time will be on a 24-hour clock when the alarm goes off.

current_time_24hr_format = int(input('Enter time now in hours (in 24hr format) :') )
time_to_wait = int(input('Enter numbers hours to wait for the alarm :'))

time_alarm_to_go = (current_time_24hr_format + time_to_wait) % 24
days = time_to_wait // 24
if time_alarm_to_go == 0:
    print('The alarm will go off at midnight: ', time_alarm_to_go,  'in',days, 'day(s).' )
else:
    print('The alarm will go off at: ', time_alarm_to_go, 'in',days, 'day(s).' )