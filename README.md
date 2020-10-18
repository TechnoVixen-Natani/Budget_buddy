# About
 This is my version of a personal budget program that I have codenamed Budget Buddy or bb for short.
 What is this program you may ask. Well its simple as the name may suggest. It is a budgeting program, based on python and uses  SQLite3 for modifing the database that this program creates. 
 I know there are hundreds if not thousands of budgeting software out there with fancy features and what not, but I did not make them. I wanted something tailored to me that I could call my own and be proud of. So that is why Budget Buddy was made.

# Resources used
OS module
sqlite3
datetime
Error class from sqlite3 module

What does this do?
We create a database named budget on the current working user desktop. That file will be the database this program always enters data to and pulls from.
There is a menu prompt that you will be able to select one of the options to execute. The program will then send the data to your budget.db file on the desktop. Where it will be stored for later use. 
You will see that there is an option to create a chart, this function is a work in progress and as I develope the program further you will be able to export your monthly expenses and deposits into an easy to read pie chart visual graph.

# Installation
This program is built on python 3.8.2 and uses SQLite3  which is available freely at https://www.sqlite.org/download.html
Find the the version appicible to your system, download and install the program. Following the onscreen prompts from SQLite3 installer. 

# Running Program
Open with command prompt or your favorite IDE, such as Spyder or PyCharm. I prefer Spyder but you can use whatever IDE you want. 
Once you open the program you should be greeted with a welcome message and short instructions on how to use the software. It will explain what each menu selection does. To select an option you simply type the corresponding number.

---EXAMPLE---

Please select an option out of the menu below.
1.Deposit
2.Expense
3.Cash on Hand
4.Balance
5.Create Chart
6.Quit

Select number '1' by typing '1' and hit enter. (1 without the quotes)
You are then prompted to enter the deposit amount. Using numbers numbers only.
Say you need to enter: $420.69 as a deposit. 
You would simply type '420.69' (no quotes)
The program will keep track of the deposit.

The same goes for an expense. You don't even need to use a negative sign. The program will automatically calculate out the monthly balance with each deposit and expense entered. Subtracting all expenses from the total deposits.

If you enter 6, the program will stop the current process it is doing, saving all data entered prior to pressing 6, to the database. Then it will give its sad 'Are you sure you done?' message before prompting to "press any key to exit..."
---END EXAMPLE--- 

# Work in progress
This program is a work in progress, functionality will vary as I develop the program. Feedback and error reporting is appreciated.

THE NAME WAS ORIGINALLY A QUICK OFF THE TOP OF MY HEAD  QUIP.  BUT I DID A LITTLE SEARCHING AND FOUND A LOT OF BUDGETING PROGRAMS ARE NAMED THIS SAME THING. I WOULD LIKE TO PROPOSE  A NAME CHANGE AND I AM OPEN TO SUGGESTIONS. IF YOU HAVE ANY PLEASE FEEL FREE TO LET ME KNOW VIA EMAIL OR POST IT IN THE ISSUES SECTION ON THE REPO. TITLE IT "NAME SUGGESTION" ALL CAPS PLEASE. ALL SUGGESTIONS MUST BE SAFE FOR WORK-UNFORTUNATE I KNOW. AND THEY NEED TO BE SERIOUS SUGGESTIONS.

Please direct bug reports to fayth.c@technovixen-codes.net