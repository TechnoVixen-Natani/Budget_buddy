# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:03:58 2020

@author: TechnoVixen-Natani aka Fayth 


Budget program nicknamed budget buddy
Tracking deposits and storing them for later calling
Tracking expenditures for later calling as well
Ability to call both deposits and expenditures and output the balance remaining
"""

# Importing OS module to determine desktop path
import os
import sqlite3
from datetime import datetime
from sqlite3 import Error


"""Current month with %B argument,which displays entire month name"""
current_month = datetime.now().strftime('%B')

"""Current time in year-month-day. Followed by Hour:Minute.
 Used to track when data was entered.
 Not used as of yet on 2020-10-17, but will be as the program develops."""
current_time = datetime.now().strftime('%Y-%m-%d %H:%M')


"""Using os module to determine the current users desktop path so we can 
make the budget database file on the desktop so it is easier to find.
Sqlite3 module and Error module as well to create a connection to the 
database after it is made, returning error (e) if the database does not exist."""
desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
default_path = os.path.join(desktop, "budget.db")

if os.path.exists(default_path):
    print('Database already exists')
    pass
else:
    pass

def sql_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Connected succsefully to budget.db using Sqlite3 version {}!'.format(sqlite3.version))
        return conn
    except Error as e:
        print(e)
    finally:
        if not conn:
            conn.close()
        

def monthly_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute(f"CREATE TABLE {current_month} (Deposit integer, Expense_Amount integer, Expense_Type text, Cash_on_Hand integer, Balance integer, Date text)")
    conn.commit()
conn = sql_connection(default_path)
if conn:
    monthly_table(conn)
else:
    print('Exiting')

if __name__ == '__main__':
    sql_connection(default_path)

#Program stops if table already exists. Need to fix this!!

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


def balance(expense_amount: int):
    """Balance function to be used later on as well"""
    return total_money - expense_amount


def cash_on_hand():
    """
    Cash_on_hand function, this is asking how much money not in bank
    accounts do you have.
    """
    return float(input('How much money do you have on hand:'))


while True:
    menu_option = input("What option do you want to do?\n 1: Enter deposit\n 2: Enter expenses\n")
    if menu_option == "1":
        deposit_amount = deposits()
        total_money += deposit_amount

    elif menu_option == "2":
        new_expense_type, new_expense_amount = input_expense_item()
        print(f"The user wants to add {new_expense_type} for ${new_expense_amount}")
        current_balance = balance(new_expense_amount) + cash_on_hand()
        total_money = current_balance
        print(f"Total balance is ${total_money}")


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


