filename = 'million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line.rstrip()
    
birthday = input('Enter birthday in format mmddyy: ')
if birthday in pi_string:
    print('Your birthday is in the first 700,000 digits of pi!')
else:   
    print('You fucking suck')
    
    

    
    
