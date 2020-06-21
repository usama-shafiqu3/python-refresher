"""                                   Python Refresher-0.1                  """
import os

def welcome_note():
    print("Hello {} to {} {}. Let's Start the course".format(user_name, code_lang, lang_version))

def header():
    print("::::::::::::::::::::::::Alphatuts++:::::::::::::::::::::::")
    print("::::::::::::::: Let's Learn Coding Together ::::::::::::::")
def dsply_data():
    print("::::::::::::::::::::::::Alphatuts++:::::::::::::::::::::::")
    print(":::::::::::::::::::   User Information :::::::::::::::::::")
    print("         NAME : {}           Course : {}".format(user_name, code_lang))


header()
user_name = input("Kindly Enter Your Name Please : ")
code_lang = input("{} Which  language do you want to learn ? ".format(user_name))
lang_version = int(input("Which Version do you want to learn ? "))
welcome_note()
os.system('cls')
dsply_data()