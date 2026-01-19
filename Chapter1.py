myName = 'Wisdom'
print('Hello,' +  myName + str('!') +  ' Welcome to Python.')  # This code prints your name and a welcome message


smallNum = 5
bigNum = 10
totalNum = smallNum + bigNum
print('The sum is:', totalNum) # This code add two values together to get total value


print('What is your name:')
name = input('>')
print('Hello,' +  name + str('!') + ' Nice to meet you.') # This code ask user to type their name and concatenate their name with a string


print('Enter your age:')
age = int(input('>'))
print('Next year you will be  ' + str(int(age) + 1)) # This code ask user for thier age and tells them how old they will be in 1 year

# This short program allows users to enter their name, favourite food and city and add a short story combining user input

print('Enter your name:')
name = input('>')

print('Enter your favourite food:')
food = input('>')

print('Enter your favourite city:')
city = input('>')

print(name + ' loves ' +   food  + ' and enjoy living in ' +  city)
