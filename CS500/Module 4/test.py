""" i = 0
password = "secret" 

while (True):
  user_input = input("Please enter the password: ")
  i += 1
  if(user_input == password):
    print('Access granted. Welcome!')
    break
  elif (user_input != password and i < 5): 
    print('Incorrect password. Please try again.')
  else:
    print('Too many incorrect Attempt. Please try after 30 mins')
    break
 """


x = int(input('Please enter max length of X co-ordinate: '))
y = int(input('Please enter max length of Y co-ordinate: '))
z = int(input('Please enter max length of Z co-ordinate: '))

lst = []
for i in range(x):
 
  for j in range(y):
    
    for k in range(z):
      lst.append(tuple([i,j,k]))

print('All the possible co-ordinate for 3D object are: \n',lst)
 

