
import sqlite3 as db

conn = db.connect("qm.db")

def show_leaderboard(conn):
    cur = conn.cursor()
    cur.execute("SELECT name, score, question, percentage FROM leaderboard ORDER BY percentage DESC")
    all_entries = cur.fetchall()

    print("\n Leaderboard:")
    print(f"{'Name':<15}{'Correct':<10}{'Wrong':<10}{'Percentage':<10}")
    print("-" * 45)

    for entry in all_entries:
        name, score, question, percentage = entry
        wrong = question - score
        print(f"{name:<15}{score:<10}{wrong:<10}{percentage:.2f}%")





