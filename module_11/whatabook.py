#Travis Nickerson
#May 5th, 2021
#Assignment whatabook
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

""" DISPLAY BOOK LISTINGS METHOD """
def displayBooks(_cursor):

    # Grabbing the books from database
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()
    # Printing the books in database with for loop in books
    print("\n -- BOOK LISTINGS --\n")
    for i in books:
        print(f" Book Name: {i[0]}\n Book Author: {i[1]}\n Book Details: {i[2]}\n")

""" DISPLAY MAIN MENU METHOD """
def displayMenu():

    print("\n -- WHATABOOK MAIN MENU --")
    print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")

    # Take in the users choice of Main Menu Options
    choice = int(input(" PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))

    # If the user inputs anything other than a Main Menu Option the user will be re-prompted
    while choice <= 0 or choice > 4:
        print("\n** INVALID SELECTION: PLEASE TRY AGAIN WITH THE OPTIONS BELOW! **")
        print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")
        choice = int(input(" PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))
        
    return choice

""" DISPLAYING STORE LOCATIONS METHOD """
def displayLocations(_cursor):

    # Grabbing store locations from database
    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()

    # Printing store locations with for loop in stores
    print("\n -- CURRENT STORE LOCATIONS -- \n")
    for i in stores:
        print(f" Location: {i[1]}\n")

""" VALIDATING USER METHOD """
def validateUser():

    print("\n -- ACCOUNT LOGIN --\n")

    # Storing user input for checking a valid USER ID
    userID = int(input("PLEASE ENTER YOUR USER ID: "))

    # Checking if user inputs a valid USER ID and re-promptig user if there is an invalid USER ID
    while userID <= 0 or userID > 3:
        print("\n** INVALID USER ID. TRY AGAIN! **\n")
        userID = int(input("PLEASE ENTER YOUR USER ID: "))

    return userID

""" DISPLAYING USER ACCOUNT MENU METHOD """
def displayAccountMenu():

    print("\n-- ACCOUNT MAIN MENU --\n")
    print(" 1. Show Wishlist\n 2. Add A Book To Your Wishlist\n 3. Main Menu\n 4. Exit Program\n")

    # Storing users selection of account menu
    accountOptions = int(input("\n PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))

    # Checking user input for account main menu and re-prompting if user enters and invlaid selection
    while accountOptions <= 0 or accountOptions > 4:
        print("\n** INVALID SELECTION: PLEASE TRY AGAIN WITH THE OPTIONS BELOW! **")
        accountOptions = int(input("\n PLEASE ENTER THE CORRESPONDING NUMBER FOR SELECTION! "))

    return accountOptions

""" DISPLAYING BOOKS THAT CAN BE ADDED TO WISHLIST METHOD """
def displayBooksToAdd(_cursor, _user_id):

    # Creating mySQL query to grab availbale books 
    availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    # Executing query                 
    _cursor.execute(availableBooks)

    # Storing the query results of books that  are available to be added to wishlist
    booksThatCanBeAdded = _cursor.fetchall()

    # Printing the books that can be added to wishlist with for loop over booksThatCanBeAdded
    print("\n -- BOOKS THAT CAN BE ADDED -- \n")
    for i in booksThatCanBeAdded:
        print(f"\n Book ID: {i[0]}\n Book Name: {i[1]}\n")
    
""" ADDING BOOK TO WISHLIST METHOD """
def addBookToWishlist(_cursor, _user_id, _book_id):

    # Executing mySQL query to add a book to wishlist of user
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, addBookID))

""" DISPLAYING USER WISHLIST METHOD """
def displayWishlist(_cursor, _user_id):

    # Executing mySQL query to access wishlist books with INNER JOIN
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    # Grabbong and storing wishlist books from query
    wishlist = _cursor.fetchall()

    # Printing wishlist books of user
    print("\n -- YOUR WISHLIST BOOKS --\n")
    for i in wishlist:
        print(f" Book Name: {i[4]}\n Author: {i[5]}\n")



try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    print("\n WELCOME TO WHATABOOK! ")

    # Storing display menu method return value in a variable for use in while loop
    mainMenuSelection = displayMenu()

    # Running program while mainMenuSelection is a proper user selection from Main Menu
    while mainMenuSelection < 4:
        # Main Menu selection 1 displays books in database
        if mainMenuSelection == 1:
            displayBooks(cursor) 
        # Main Menu selection 2 displays store locations         
        if mainMenuSelection == 2:
            displayLocations(cursor)
        # Main Menu selection 3 validates user ID and enters user account menu           
        if mainMenuSelection == 3:
            myID = validateUser()
            # Storing user input selection on Account Main Menu
            accountOptions = displayAccountMenu()
            # While loop runs and checks user input. if user selection equals 3 it returns them to 
            # the Main Menu
            while accountOptions != 3:
                # Account Menu selection 1 displays user wishlist
                if accountOptions == 1:
                    displayWishlist(cursor, myID)
                # Account Menu selection 2 displays books that can be added to wishlist and asks
                # user to input book ID they wish to add to their wishlist and then commits that book to 
                # the database                           
                if accountOptions == 2:
                    displayBooksToAdd(cursor, myID)
                    addBookID = int(input(" Enter the Book ID you want to add to your wishlist! "))
                    addBookToWishlist(cursor, myID, addBookID)
                    db.commit()
                # Account Menu selection 4 terminates program
                if accountOptions == 4:
                    sys.exit()
                accountOptions = displayAccountMenu()
        mainMenuSelection = displayMenu()
        # Main Menu selection 4 terminates the program
        if mainMenuSelection == 4:
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