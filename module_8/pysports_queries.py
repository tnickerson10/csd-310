#Travis Nickerson
#April 24th, 2021
#Assignment 8.3
#GitHub: https://github.com/tnickerson10/csd-310
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")

    for i in teams:
        print(f"\n Team ID: {i[0]}\n Team Name: {i[1]}\n Mascot: {i[2]}\n")

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS -- \n")

    
    for j in players:
        print(f"  Player ID: {j[0]}\n  First Name: {j[1]}\n  Last Name: {j[2]}\n  Team ID: {j[3]}\n")





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