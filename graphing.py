# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 02:22:03 2020

@author: TechnoVixen-Natani aka Fayth
"""
import matplotlib.pyplot as plt
import budget_buddy

def monthly_chart():
    
    expense_type = budget_buddy.insert_expenses
    deposit = budget_buddy.monthly_deposit_total()
    my_data = [expense_type, deposit]
    my_labels = ['Expense Types' , 'Deposits']
    plt.pie(my_data, labels=my_labels,autopct='%1.1f%%')
    plt.title('Current Month')
    plt.axis('equal')
    plt.show()    


