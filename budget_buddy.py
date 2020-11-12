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
    """Creates table in database based on the current month, 
    if table exsists already it connects to the table instead """
    cursor_obj = conn.cursor()
    cursor_obj.execute(f"CREATE TABLE IF NOT EXISTS {current_month} (Deposit float, Deposit_Date real, Expense_Amount float, Expense_Type text, Cash_on_Hand float, Balance float)")
    conn.commit()
    print(f'Table {current_month} successfully created in budget.db')
conn = sql_connection(default_path)
if conn:
    monthly_table(conn)
else:
    print('Exiting')


def insert_deposits(amt):
    """Uses deposit function in the functions file to ask for a deposit amount
    adds the amount into the current month table under Deposit coloumn"""
    insert_command_amt = """insert into {} (Deposit, Deposit_Date) values (?,?)""".format(current_month)
    insert_amount = amt
    insert_timestamp = current_time_iso
    multi_insert_date_amount = insert_amount, insert_timestamp
    conn.execute(insert_command_amt, multi_insert_date_amount)
    conn.execute("commit;")
 
    
def monthly_deposit_total():
    """Takes the total deposits from the Deposit coloumn,
    adds them all together, setting null values to 0. Returns
    the sum of the deposits"""
    # mdt = monthly deposit total
    mdt_query = """Select (Deposit) From {}""".format(current_month)
    cursor = conn.cursor()
    cursor.execute(mdt_query)
    total1 = 0
    for row in cursor:
        deposit = row[0] if row[0] else 0
        total1 += deposit
    print(f"Your total deposits this month is: ${total1}")
    return total1
 
    
def insert_expenses(expense_type, cost):
    """Uses expense type function in functions file, which creates a tuple. Tuple is
    passed to this function after its unpacked, putting the type of expense and cost 
    in the appropiate coloumn."""
    insert_expense_command = """insert into {} (Expense_Type, Expense_Amount) values (?,?)""".format(current_month)
    insert_expense_name = expense_type
    insert_expense_amt = cost
    multi_expense_insert = insert_expense_name, insert_expense_amt
    conn.execute(insert_expense_command, multi_expense_insert)
    conn.execute("commit;")


def monthly_total():
    """Adds up the total amount of expenses, calls the monthly deposit total,
    subtracts the expenses from the deposit total. Then it prompts the user
    if they want to add in any cash on hand they may have. Calculating the
    new total with cash on hand factored into the amount as well."""
    monthly_expenses = """Select (Expense_Amount) from {}""".format(current_month)
    cursor = conn.cursor()
    cursor.execute(monthly_expenses)
    total2 = 0
    for row in cursor:
        expense = row[0] if row[0] else 0
        total2 += expense
    print(f"Your total expenses this month is: ${total2}")
    monthly_sum = monthly_deposit_total() - (total2)
    print(f"Your total this month is: ${monthly_sum}\n"
           "Do you want to add any cash you have on hand to this total?")
    menu_prompt = input("1. Yes\n"
                        "2. No\n")
    if menu_prompt == "1":
       absolute_total = cash_on_hand() + monthly_sum
       print(f"\nAfter adding in your cash on hand, you have: ${absolute_total}\n")
    elif menu_prompt =="2":
        print('Cash on hand will not be added.\n')
    
    
def cash_on_hand():
    """
    Cash_on_hand function, this is asking how much money not in bank
    accounts do you have.
    """
    c_o_h = None
    while not c_o_h: 
        temp = input('How much money do you have on hand:\n')
        try:
            c_o_h = float(temp)
        except ValueError:
            print(f'{temp} - was an invalid entry. Please only enter a valid number.\n')
    return c_o_h    
    

   
    


