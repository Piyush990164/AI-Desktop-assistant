import sqlite3
from internet import check_internet_connection


def create_connection():

    
    connection = sqlite3.connect("memory.db")
    return connection  

def get_questions_and_answers():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM questionsAndAnswers")

    return cur.fetchall()


def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()

    # Use parameterized query to avoid SQL injection or errors with special characters
    query = "INSERT INTO questionsAndAnswers (question, answer) VALUES (?, ?)"
    cur.execute(query, (question.lower(), answer.lower()))
    con.commit()


    
def get_answer_from_memory(question):
    con = create_connection()
    cur = con.cursor()

    # Look for an exact match (case insensitive)
    query = "SELECT answer FROM questionsAndAnswers WHERE LOWER(question) = ?"
    cur.execute(query, (question.lower(),))
    result = cur.fetchone()

    return result[0] if result else ""



def get_name():
    con = create_connection()
    cur = con.cursor()

    query = "select value from memory where name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]

def update_name(new_name):
    con = create_connection()
    cur = con.cursor()

    query = "update memory SET value = '" + new_name + "' where name = 'assistant_name'"
    cur.execute(query)
    con.commit()


def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()

    query = "UPDATE memory SET value = '" + str(last_seen_date) + "' WHERE name = 'last_seen_date'"
    cur.execute(query)
    con.commit()

def get_last_seen():
    con = create_connection()
    cur = con.cursor()

    query = "SELECT value FROM memory WHERE name = 'last_seen_date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])


def turn_on_speech()   :
    if (check_internet_connection):
        con = create_connection()
        cur = con.cursor()
        query = "UPDATE memory set value = 'on' WHERE name = 'speech'"
        cur.execute(query)
        con.commit()

        return(" Ok I will speak now")
    else:
        return(" Please connect to the internet to use speech recognition feature.")

        


def turn_off_speech():
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory set value = 'off' WHERE name = 'speech'"
    cur.execute(query)
    con.commit()   
    return " Speech recognition is turned off."


def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'speech'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0]) 

    if ans == "on":
        return True
    else:
        return False
    
   


    



