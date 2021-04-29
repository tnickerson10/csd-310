#Travis Nickerson
#April 29th, 2021
#Assignment 9.3
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

    cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")


    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()


    print("\n  -- DISPLAYING PLAYERS AFTER INSERT --")

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")
    

    print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

    print("\n  -- DISPLAYING PLAYERS AFTER DELETE --")

    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    for i in players:
        print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

    

   





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