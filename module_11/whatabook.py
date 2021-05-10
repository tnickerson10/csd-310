#Travis Nickerson
#May 5th, 2021
#Assignment 11
#GitHub: https://github.com/tnickerson10/csd-310
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def displayBooks(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()

    print("\n -- BOOK LISTINGS --\n")

    for i in books:
        print(f" Book Name: {i[0]}\n Book Author: {i[1]}\n Book Details: {i[2]}\n")


def displayMenu():

    print("\n -- WHATABOOK MAIN MENU --")
    print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")

    choice = int(input(" PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))
    while choice <= 0 or choice > 4:
        print("\n** INVALID SELECTION: PLEASE TRY AGAIN WITH THE OPTIONS BELOW! **")
        print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")
        choice = int(input(" PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))
        
    return choice


def displayLocations(_cursor):

    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()

    print("\n -- CURRENT STORE LOCATIONS -- \n")

    for i in stores:
        print(f" Location: {i[1]}\n")

def validateUser():

    print("\n -- ACCOUNT LOGIN --\n")

    userID = int(input("PLEASE ENTER YOUR USER ID: "))

    while userID <= 0 or userID > 3:
        print("\n** INVALID USER ID. TRY AGAIN! **\n")
        userID = int(input("PLEASE ENTER YOUR USER ID: "))

    return userID


def displayAccountMenu():

    print("\n-- ACCOUNT MAIN MENU --\n")
    print(" 1. Show Wishlist\n 2. Add A Book To Your Wishlist\n 3. Main Menu\n 4. Exit Program\n")

    accountOptions = int(input("\n PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))

    while accountOptions <= 0 or accountOptions > 4:
        print("\n** INVALID SELECTION: PLEASE TRY AGAIN WITH THE OPTIONS BELOW! **")
        accountOptions = int(input("\n PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))

    return accountOptions

def displayBooksToAdd(_cursor, _user_id):

    availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(availableBooks)
    booksThatCanBeAdded = _cursor.fetchall()

    print("\n -- BOOKS THAT CAN BE ADDED -- \n")

    for i in booksThatCanBeAdded:
        print(f"\n Book ID: {i[0]}\n Book Name: {i[1]}\n")
    

# def addBookToWishlist(_cursor, _user_id, _book_id):

def displayWishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()

    print("\n -- YOUR WISHLIST BOOKS --\n")

    for i in wishlist:
        print(f" Book Name: {i[4]}\n Author: {i[5]}\n")



try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    print("\n WELCOME TO WHATABOOK! ")

    mainMenuSelection = displayMenu()

    while mainMenuSelection < 4:

        if mainMenuSelection == 1:
            displayBooks(cursor)            
        if mainMenuSelection == 2:
            displayLocations(cursor)           
        if mainMenuSelection == 3:
            myID = validateUser()
            accountOptions = displayAccountMenu()
            while accountOptions <= 4:
                if accountOptions == 1:
                    displayWishlist(cursor, myID)                           
                if accountOptions == 2:
                    displayBooksToAdd(cursor, myID)
                if accountOptions == 4:
                    sys.exit()
                accountOptions = displayAccountMenu()
        mainMenuSelection = displayMenu()
        if mainMenuSelection == 4:
            sys.exit()
    print("Program Terminated")
    sys.exit()   
                


    

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()