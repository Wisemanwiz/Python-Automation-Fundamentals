# This code asks the user to enter their monthly budget

def get_budget():
    monthly_budget = int(input('Enter monthly budget: '))
    return monthly_budget


# This code displays the menu options for the user to select their choice
def menu_options():
    print('1. Add expense')
    print('2. View balance')
    print('3. Exit')

    choose = int(input('Select your choice: '))
    return choose


# ---- MAIN PROGRAM ---

currency = "zł"   #  currency defined once

balance = get_budget()
print('Your monthly budget is:', balance, currency)

while True:
    selected_choice = menu_options()

    if selected_choice == 1:
        check_expense = int(input('Enter expense amount: '))
        balance = balance - check_expense

        if balance < 0:
            print('⚠️ Warning: you have overspent! Balance:', balance, currency)

    elif selected_choice == 2:
        print('Balance:', balance, currency)

    elif selected_choice == 3:
        print('Goodbye!')
        break

    else:
        print('Invalid option, please try again.')
