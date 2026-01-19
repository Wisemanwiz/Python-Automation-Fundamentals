my_pass = 'swordfish'
# This code checks if the password is correct
print('Enter your password:')
passWord = input('>')

if passWord == my_pass :
    print('"Access granted"')

else:
    print('"Access denied"')


# This code allow users to enter any number and check if its even or odd.

print('Enter your number:')
number = int(input('>'))

if number %  2 == 0:
    print('Its an even number!')

else:
    print('Its an odd number!')

# Here we ask user to enter their score and print out result based on their score.

print('Enter your score from 0-100:')
score = int(input('>'))

if score >= 90:
    print('A')

elif score >= 80:
    print('B')

elif score >= 70:
    print('C')

elif score >= 60:
    print('D')
else:
    print('F')



# This code allows user to input name and password and check if its correct.

print('Enter your username:')
name = input('>')

print('Enter your password:')
password = int(input('>'))

if name == ('admin') and password == (1234):
    print('"Login successful"')

else:
    print('"Login failed"')

# This code ask user to guess the secret number

secrete_number = 8

print('Guess the secret number:')
user_name = int(input('>'))

if user_name == 8:
    print('"you guessed right"')

else:
    print('"wrong guess"')
