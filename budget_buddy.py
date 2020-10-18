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

# Current month with %B argument,which displays entire month name
current_month = datetime.now().strftime('%B')

# Current time in year-month-day. Followed by Hour:Minute.
# Used to track when data was entered.
# Not used as of yet on 2020-10-17, but will be as the program develops.
current_time = datetime.now().strftime('%Y-%m-%d %H:%M')

######Not in use yet#####
# def monthly_chart():
    # my_data = [expenses and deposits here]
    # my_labels = 'Expenses', 'Deposits'
    # plt.pie(my_data, labels=my_labels,autopct='%1.1f%%')
    # plt.title('{}'.format(current_month))
    # plt.axis('equal')
    # plt.show()
    
# menu = ("1.Deposit\n"
       # "2.Expense\n"
       # "3.Cash on hand\n"
       # "4.Balance\n"
       # "5.Create Chart\n"
       # "5.Quit\n")
#################################################
    
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
        return conn

if __name__ == '__main__':
    sql_connection(default_path)


def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE {}(Deposit integer, Expenses integer, {} integer, Balance integer, Date text)".format(current_month,'Cash_on_Hand'))
    conn.commit()
conn = sql_connection(default_path)
if conn:
    sql_table(conn)
else:
    print('Exiting')



