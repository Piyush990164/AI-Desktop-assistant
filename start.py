from input_module import take_input
from process_module import process 
from output_module import output
from welcome import greet
import translator
import os
from music import play_music
from web import open_facebook, open_google, close_browser, open_youtube, open_instagram, open_discord, open_google_drive


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
   
greet() #welcome message

while True:
    i = take_input()
    o = process(i)
    output(o)

# from input_module import take_input
# from process_module import process 
# from output_module import output
# from welcome import greet
# import translator  # this gives access to translateNow()
# import os

# def clear_terminal():
#     os.system('cls' if os.name == 'nt' else 'clear')

# clear_terminal()
# greet()  # welcome message
# print("Welcome to the Assistant!")

# while True:
#     i = take_input()
#     o = process(i)

#     if o == "translator_mode":
#         print("Switching to Translator Mode...")
#         translator.translateNow()
#         continue  # After translator mode, return to assistant loop

#     output(o)
