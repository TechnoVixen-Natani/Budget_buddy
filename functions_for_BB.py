# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 00:32:04 2020

@author: TechnoVixen-Natani aka Fayth

Operational functions for main program. These are the actual data collection portion
of the program.
"""


import budget_buddy


total_money = 0


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
            print(f"{temp} - was an invalid entry. Please make sure you entered a valid number")

    # This is how to return a tuple. This means you can assign two variables when calling this function as seen below
    return expense_type, cost


#def balance(expense_amount: int):
    #"""Balance function to be used later on as well"""
    #return total_money - expense_amount


def cash_on_hand():
    """
    Cash_on_hand function, this is asking how much money not in bank
    accounts do you have.
    """
    return float(input('How much money do you have on hand:'))


while True:
    menu_option = input("What option do you want to do?\n" 
                        "1: Enter deposit\n"
                        "2: Enter cash on hand\n"
                        "3: Enter expenses\n"
                        "4: Monthly Deposit Total\n")
    
    if menu_option == "1":
        deposit_amount = deposits()
        #total_money += deposit_amount
        budget_buddy.insert_deposits(deposit_amount)
        
    elif menu_option == "2":
        cash_amount = cash_on_hand()
        #total_money += cash_amount
        budget_buddy.insert_cash(cash_amount)

    elif menu_option == "3":
        #new_expense_type, new_expense_amount = input_expense_item()
        #print(f"The user wants to add {new_expense_type} for ${new_expense_amount}")
        expense_type, cost = input_expense_item()
        budget_buddy.insert_expenses(input_expense_item)
        #Code below was used previously, attempting changes but keeping the code just in case for a fall back 
        #current_balance = balance(new_expense_amount) + cash_on_hand()
        #total_money = current_balance
        #print(f"Total balance is ${total_money}")
    
    elif menu_option == "4":
        budget_buddy.monthly_deposit_total()


    

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


