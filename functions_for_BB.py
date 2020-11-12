# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 00:32:04 2020

@author: TechnoVixen-Natani aka Fayth

Operational functions for main program. These are the actual data collection portion
of the program.
"""


import budget_buddy


def deposits() -> float:
    """Asks a user to input an amount of a deposit. Returns only once a valid deposit is entered."""
    deposit = None
    while not deposit:
        temp = input('Please enter deposit amount:')
        
        try:
            deposit = float(temp)
        except ValueError:
            print(f'{temp} - was an invalid entry.Please make sure you enter a valid number.\n')
    return deposit


def input_expense_item() -> tuple:
    """
    Prompt the user to enter an expense type, and the amount for the expense
    :return: Tuple - expense type, amount
    """
    expense_type_menu = input("What is the expense item, please choose from the menu options.\n"
                         "1. Bills\n"
                         "2. Food\n"
                         "3. Other\n")
    
    if expense_type_menu == "1":
        expense_type = ("Bills")
    
    elif expense_type_menu == "2":
        expense_type = ("Food")
    
    elif expense_type_menu == "3":
        expense_type = ("Other")
        
    cost = None

    # must ensure that the user provides a valid number! In this case, a valid decimal!
    while not cost:
        temp = input(f"How much did you spend on '{expense_type}'?\n")

        try:
            cost = float(temp)

        except ValueError:
            print(f"{temp} - was an invalid entry. Please make sure you entered a valid number.\n")
    
    print(f'\nUser wants to add {expense_type} expense type for ${cost}\n')
    return expense_type, cost


while True:
    menu_option = input("What option do you want to do?\n" 
                        "1: Enter deposit\n"
                        "2: Enter Expenses\n"
                        "3: Monthly Deposits Total\n"
                        "4: Monthly Balance\n\n")
    
    # Enter deposit
    if menu_option == "1":
        deposit_amount = deposits()
        budget_buddy.insert_deposits(deposit_amount)
    
    # Enter expenses, passes to database for recording
    elif menu_option == "2":
        budget_buddy.insert_expenses(*input_expense_item())

    # Calculates total deposits from database
    elif menu_option == "3":
        budget_buddy.monthly_deposit_total()

    # Calculates sum of deposits and expenses, prompts user if they want to add cash on hand.
    elif menu_option == "4":
        budget_buddy.monthly_total()
      
    

#####Program is still a WIP. Changes will be made.######







