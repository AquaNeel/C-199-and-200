import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

questions = [
    "What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Pizza",
    "How many bones are there in the human body? \n a.208 \n b.209 \n c.207 \n d.206",
]
answers = [
    'c','d'
]
def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will receive a quest. The answer to that should be one of the following.".encode('utf-8'))
    conn.send("Good luck!".encode('utf-8'))
    index,question,answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.rec(2048).decpde('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1 
                    conn.send(f"Bravo! Your score is {score} \n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time".encode('utf-8'))
            else: 
                remove(conn)
        except:
            continue
def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions) -1)
    random_question = questions[random_index]
    random_answer = answers [ random_index]
    conn.send(random_question.enconde('utf-8'))
    return random_index,random_question,random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)
