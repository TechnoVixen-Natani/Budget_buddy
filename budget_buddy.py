# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:03:58 2020

@author: fayth
"""

# Budget program nicknamed budget buddy
# Tracking deposits and storing them for later calling
# Tracking expenditures for later calling as well
# Ability to call both deposits and expenditures and output the balance remaining

# Importing OS module to determine desktop path
import os
import sqlite3
from datetime import datetime
from sqlite3 import Error


# Deposits function so we can call it later on
def deposits():
    deposits = int(float(input('Please enter deposit amount:' )))                       
    return deposits

# Expenses function to be used later on as well
def expenses():
    expenses = int(float(input('Please enter expense amount:')))
    return expenses

# Balance function to be used later on as well
def balance():
    balance = (deposits() + cash_on_hand()) - expenses()
    return balance

# Cash_on_hand function, this is asking how much money not in bank
# accounts do you have.
def cash_on_hand():
    cash_on_hand = int(float(input('How much money do you have on hand:')))
    return cash_on_hand


#####Program is still a WIP. Changes will be made.######

# def monthly_chart():
    # current_month = datetime.now().strftime('%B')
    # my_data = [expenses and deposits here]
    # my_labels = 'Expenses', 'Deposits'
    # plt.pie(my_data, labels=my_labels,autopct='%1.1f%%')
    # plt.title('{}'.format(current_month))
    # plt.axis('equal')
    # plt.show()
    

    
# Using os module to determine the current users desktop path so we can 
# make the budget database file on the desktop so it is easier to find.
# Sqlite3 module and Error module as well to create a connection to the 
# database after it is made, returning error (e) if the database does not exist.
desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
default_path = os.path.join(desktop, "budget.db")

if os.path.exists(default_path):
    print('Database already exists')
    pass
else:
    pass

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Connected succsefully to {} using Sqlite3 version {}!'.format(default_path, sqlite3.version))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(default_path)







menu = ("1.Deposit\n"
        "2.Expense\n"
        "3.Cash on hand\n"
        "4.Balance\n"
        "5.Create Chart\n"
        "5.Quit\n")