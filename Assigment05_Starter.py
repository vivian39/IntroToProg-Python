# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# WWang,08.08.2022,Created started script
# <Wei Wang>,<08/08/2022>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = ""  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
strFile = "ToDoList.txt"

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
Menu of Options
1) Show current data
2) Add a new item.
3) Remove an existing item.
4) Save Data to File
5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice == '1':
        for dicRow in lstTable:
            print(dicRow["task"] + ',' + dicRow["priority"])
            continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strItem = input("task: ")
        strValue = input("priority: ")
        lstTable.append({"task": strItem, "priority": strValue})
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strItem = input("task to remove: ")
        found = False
        for row in lstTable:
            if row["task"].lower() == strItem.lower():
                found = True
                lstTable.remove(row)
                break
        if found:
            print("row found and removed")
        else:
            print("row not found")

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["task"]) + ',' + str(row["priority"] + '\n'))
        objFile.close()
        print("Now in file!")

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        strChoice = input("Exit? ('y/n'): ")
        if strChoice.lower() == 'y':
            break
