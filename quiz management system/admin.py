# b) Admin Authentication (admin.py):
# - Allows admin login using username and password.
# - Provides options to modify quiz, create user, change password

import sqlite3 as db
import quizmgmt
conn = db.connect("qm.db")
def auth(conn):
    cur = conn.cursor()
    un = input("enter username: ")
    pwd = input("enter password: ")
    qry=f'''select username,role
    from login 
    where username='{un}'  and password ='{pwd}'  and  status='active' '''
    cur.execute(qry)
    rs = cur.fetchone()
    if(rs==None):
        print("Invalid username or password")
    else:
        print(f"Welcome {rs[1]} ({un})")
        manageadmin(conn,un)
    # - Provides options to modify quiz, create user, change password

def manageadmin(conn,username):
    while(True):
        a_o = int(input('''
            1. Modify quiz
            2. Create user
            3. Change password
            4. Remove an admin
            5. Clear leaderboard
            6.exit
            Enter your choice ->
            '''))
        if a_o == 1:
            quizmgmt.quiz_mgmt()
        elif a_o == 2:
            new_admin(conn)
        elif a_o == 3:
            changepassword(conn, username)
        elif a_o == 4:
            remove_admin(conn)
        elif a_o == 5:
            clear(conn)
        else:
            break

def new_admin(conn):
    cur = conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm = input("Re enter your password: ")
    if password == confirm:
        new_qry = '''INSERT INTO login (username, password, status, role) VALUES (?, ?, ?, ?)'''
        cur.execute(new_qry, (username, password, 'active', 'admin'))
        conn.commit()
        print("Admin enter successfully")
    else :
        print("invalid password!!!!")

def changepassword(conn,un):
    cur = conn.cursor()
    new_password = input("Enter new password: ")
    con_new_password = input("Re-enter new password: ")
    if new_password == con_new_password:
        qry = '''UPDATE login SET password = ? WHERE username = ?'''
        cur.execute(qry, (new_password, un))
        conn.commit()
        print("Password updated successfully.")
    else:
        print("invalid password!!!!")

def remove_admin(conn):
    cur = conn.cursor()
    remove = input('Enter username to remove: ')
    qry = '''DELETE FROM login WHERE username = ?'''
    cur.execute(qry, (remove,))
    conn.commit()
    print("Successfully removed:", remove)

def clear(conn):
    cur = conn.cursor()
    cur.execute("DELETE from leaderboard")
    print("leaderboard deleted successfully")
    conn.commit()
