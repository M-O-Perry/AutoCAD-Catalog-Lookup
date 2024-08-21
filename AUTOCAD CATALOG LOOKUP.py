import pyodbc
import os

#INPUT
#The user MUST enter at least two characters
userInput = ""
while len(userInput) <= 1:
    userInput = input("\nPlease enter a keyword. Ctrl + C to quit.\n")

while True:
    #SETUP & RESET
    try:
        #I found this on the internet, sorry
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=E:\Public\AutoCADShare\AeData\en-US\Catalogs\default_cat.mdb;'
            )
        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()
        tempCursor = cnxn.cursor()
        tableList = []
        totalFound = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        if userInput[len(userInput)-1:len(userInput)] == "*":
            hasStar = True
        else:
            hasStar = False
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("ERROR: Failed to access database\n")
        print("Ensure that the database is located at \nE:\Public\AutoCADShare\AeData\en-US\Catalogs\default_cat.mdb")
        print("Ensure that this user has the proper Read/Write permissions to the database")
        input("\nPress Enter to quit\n")
        break
    
    #OPTIMIZE
    #Used for reversing the array since most data is located near the alphabetical middle/end
    for table_info in cursor.tables(tableType='TABLE'):
        tableList.append(table_info)

    #SEARCH
    print("Searching for " + userInput)
    print("")
    print("")

    #Loops through each TABLE
    for table_info in reversed(tableList):
        tempCursor.execute('select * from [' + table_info.table_name + ']')

        #Loops through each ROW
        for row in tempCursor.fetchall():

            #Loops through each DATA
            for value in row:
                valueStripped = str(value).replace(' ','')
                userInputStripped = userInput.replace(' ','')

                if (hasStar) and (valueStripped.find(userInputStripped[0:len(userInputStripped)-1]) != -1):
                        totalFound += 1
                        print(table_info.table_name + "\n" + valueStripped)
                        print()
                
                elif (not hasStar) and (valueStripped.find(userInputStripped) != -1):
                        totalFound += 1
                        print(table_info.table_name)
                        print()

    #CONCLUSION
    print("\nFound " + str(totalFound) + " entries\n")
    userInput = ""
    while len(userInput) <= 1:
        userInput = input("\nPlease enter a keyword. Ctrl + C to quit.\n")
