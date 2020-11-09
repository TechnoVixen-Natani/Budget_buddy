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
current_time = datetime.now().strftime('%Y-%m-%d')
current_time_iso = datetime.now().isoformat(sep=' ',timespec='minutes')


"""Using os module to determine the current users desktop path so we can 
make the budget database file on the desktop so it is easier to find.
Sqlite3 module and Error module as well to create a connection to the 
database after it is made, returning error (e) if the database does not exist."""
desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
default_path = os.path.join(desktop, "budget.db")

if os.path.exists(default_path):
    print('Database already exists\n')
    pass
else:
    print(f'Creating database budget.db at {desktop}')
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    cursorObj.execute(f"CREATE TABLE {current_month}(Deposit integer, Expenses integer, Cash_On_Hand integer, Balance integer, Date text)")
=======
    cursorObj.execute(f"CREATE TABLE {current_month} (Deposit integer, Expense_Amount integer,Expense_Type text, Cash_on_Hand integer, Balance integer, Date text)")
>>>>>>> Stashed changes
=======
    cursorObj.execute(f"CREATE TABLE IF NOT EXISTS {current_month} (Deposit float, Deposit_Date real, Expense_Amount float, Expense_Type text, Cash_on_Hand float, Balance float)")
>>>>>>> Stashed changes
    conn.commit()
    print(f'Table {current_month} successfully created in budget.db')
conn = sql_connection(default_path)
if conn:
    monthly_table(conn)
else:
    print('Exiting')


def insert_deposits(amt):
    insert_command_amt = """insert into {} (Deposit, Deposit_Date) values (?,?)""".format(current_month)
    insert_amount = amt
    insert_timestamp = current_time_iso
    multi_insert_date_amount = insert_amount, insert_timestamp
    conn.execute(insert_command_amt, multi_insert_date_amount)
    conn.execute("commit;")
    
def monthly_deposit_total():
    # mdt = monthly deposit total
    mdt_query = """Select (Deposit) From {}""".format(current_month)
    cursor = conn.cursor()
    cursor.execute(mdt_query)
    total = 0
    for row in cursor:
        total += row[0]
    print(f"Your total deposits this month is: ${total}")
    
def insert_expenses(amt):
    insert_expense_command = """insert into {} (Expense_Type, Expense_Amount) values (?,?)""".format(current_month)
    insert_expense_name = str()
    insert_expense_amt = amt
    multi_expense_insert = insert_expense_name, insert_expense_amt
    conn.execute(insert_expense_command, multi_expense_insert)
    conn.execute("commit;")




"""
May not use the insert_cash function. Code is here just in case for now
"""
#def insert_cash(amt):
 #   insert_command_cash = """insert into {} (Cash_on_hand, Cash_Date) values(?,?)""".format(current_month)
 #   insert_cash_amount = amt
 #   insert_timestamp_cash = current_time_iso
 #   multi_insert_cash_date = insert_cash_amount, insert_timestamp_cash
 #   conn.execute(insert_command_cash, multi_insert_cash_date)
 #   conn.execute("commit;")
   
    


