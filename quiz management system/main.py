# a) Main Menu (main.py):
# - Displays the main options: Login, Play Quiz, Show Leaderboard, Exit.
# - Controls navigation to respective modules.

import sqlite3 as db
import admin
import quiz as qb
import leaderboard as lb
conn = db.connect("qm.db")

print("Welcome to The Quiz")

def main():
    while True:
        choice = int(input("""
        1)Login
        2)Play Quiz
        3)Show Leaderboard
        4)Exit
        Enter your choice -> """))

        if choice == 1:
           admin.auth(conn)
           break
        elif choice == 2:
            qb.quiz(conn)
        elif choice == 3:
            lb.show_leaderboard(conn)
        elif choice == 4:
            print("Thanks for playing")
            break
        else:
            print("Invalid option")

if __name__=="__main__":
    main()
