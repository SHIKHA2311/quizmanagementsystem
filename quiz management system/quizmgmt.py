# - Load questions from CSV
# - Add, delete, view questions

import sqlite3 as db
conn = db.connect("qm.db")


def quiz_mgmt():
    while True:
        user = int(input("""
        1. load question
        2. add question
        3. delete question
        4. view question
        Enter your choice -> 
        """))
        if user == 1:
            load_question(conn)
        if user == 2:
            add_question(conn)
        if user == 3:
            deletequestion(conn)
        if user == 4:
            view(conn)

def load_question(conn):
    cur = conn.cursor()
    file = input("Enter file name: ")
    fp = open(file,"r")
    qry = """insert into questions(question,a,b,c,d,correct,hint,explanation) values"""
    c=0
    for i in fp.readlines():
        if c==0:
            pass
        else:
            qry+="""('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}'),""".format(*i.split(",")[1:])
        c+=1
    qry=qry.rstrip(',')
    cur.execute(qry)
    conn.commit()
    cur.close()
    print("file loaded successfully..")



def add_question(conn):
    cur = conn.cursor()
    cur= conn.cursor()
    tup=("question","option1","option2","option3","option4","correct","hint","explanation")
    lst=[]
    for i in tup:
        lst.append(input(f"enter {i}: "))
    qry="""insert into questions(ques,a,b,c,d,correct,hint,explanation) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(*lst)
    cur.execute(qry)
    conn.commit()
    cur.close()
    print("question inserted")


def deletequestion(conn):
    cur = conn.cursor()
    user = int(input("1. You want to delete all question, 2. You want delete one question"))
    if user == 1:
        qry = '''delete from questions'''
        cur.execute(qry)
        conn.commit()
        cur.close()
        print("question deleted successfully")
    elif user == 2:
        terminate = input("Enter question number: ")
        qry = "DELETE FROM questions WHERE qno = ?"
        cur.execute(qry, (terminate,))
        conn.commit()
        cur.close()
        print("entered question number is deleted")

def view(conn):
    cur = conn.cursor()
    qry = '''select * from questions'''
    cur.execute(qry)
    conn.commit()
    rows = cur.fetchall()
    if not rows:
        print("No questions found.")
    else:
        print("Questions:")
        for row in rows:
            print("""
            Q{0:<2} {1:<60}
            a){2:<20} b){3:<20}
            c){4:<20}"d){5:<20}
            Answer {6:}
            """.format(*row))
    cur.close()


