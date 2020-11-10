# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 00:32:04 2020

@author: TechnoVixen-Natani aka Fayth

Operational functions for main program. These are the actual data collection portion
of the program.
"""


import budget_buddy


def deposits():
    """Deposits function so we can call it later on"""
    return float(input('Please enter deposit amount:'))


def input_expense_item() -> tuple:
    """
    Prompt the user to enter an expense type, and the amount for the expense
    :return: Tuple - expense type, amount
    """
    expense_type = input("What is the expense item?\n").capitalize()
    cost = None

    # must ensure that the user provides a valid number! In this case, a valid decimal!
    while not cost:
        temp = input(f"How much was '{expense_type}'?\n")

        try:
            cost = float(temp)

        except ValueError:
            print(f"{temp} - was an invalid entry. Please make sure you entered a valid number\n")
    print(f'User wants to add {expense_type} for ${cost}\n')
    return expense_type, cost
   

def cash_on_hand():
    """
    Cash_on_hand function, this is asking how much money not in bank
    accounts do you have.
    """
    return float(input('How much money do you have on hand:'))


while True:
    menu_option = input("What option do you want to do?\n" 
                        "1: Enter deposit\n"
                        "2: Enter Expenses\n"
                        "3: Monthly Deposits Total\n"
                        "4: Monthly Balance\n\n")
    
    if menu_option == "1":
        deposit_amount = deposits()
        budget_buddy.insert_deposits(deposit_amount)
        
    elif menu_option == "2":
        budget_buddy.insert_expenses(*input_expense_item())

    elif menu_option == "3":
        budget_buddy.monthly_deposit_total()

    
    elif menu_option == "4":
        #this command will take the deposits, subtract expenses and ask user if they want to add cash on hand
        print('Command not implimented yet, please try again later')

    

#####Program is still a WIP. Changes will be made.######



######Not in use yet######
# def monthly_chart():
    # my_data = [expenses and deposits here]
    # my_labels = 'Expenses', 'Deposits'
    # plt.pie(my_data, labels=my_labels,autopct='%1.1f%%')
    # plt.title('{}'.format(current_month))
    # plt.axis('equal')
    # plt.show()    
#################################################


