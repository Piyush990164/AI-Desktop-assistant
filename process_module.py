from output_module import output
from time_module import get_time, get_date
from database import *
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
import assistant_details
from web import open_facebook, open_google, close_browser, open_youtube, open_instagram, open_discord, open_google_drive
from music import next_song, previous_song, stop_music, play_music, pause_music, shuffle_playlist
from display import change_wallpaper
from news import get_news


def process(query):
    answer = get_answer_from_memory(query).strip()

    if answer == "":
        output(" Don't know this one, should I check on the internet?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else:
            output(" Can you please tell me what it means?")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "").strip()
                value = get_answer_from_memory(ans)
                if value == "":
                    return " Can't help with this one."
                else:
                    insert_question_and_answer(query, value)
                    return " Thanks, I will remember it for the next time"
            else:
                return " Can't help with this one."

    # MUSIC CONTROLS
    
    
    elif answer == "play music":
        return play_music()
    
    elif answer == "pause music":
        return pause_music()
    
    elif answer == "stop music":
        return stop_music()
    
    elif answer == "next song":
        return next_song()
    
    elif answer == "previous song":
        return previous_song()
    
    elif answer == "shuffle playlist":
        return shuffle_playlist()
    


    elif answer == "change wallpaper":
        return change_wallpaper()
    

    elif answer == "get news":
        return get_news()


    


    # OTHER FEATURES
    elif answer == "get time details":
        return "Time is " + get_time()

    elif answer == "check internet connection":
        if check_internet_connection():
            return " Internet is connected"
        else:
            return " Internet is not connected"

    elif answer == "tell date":
        return " Date is " + get_date()
    
    elif answer == "on speak":
        return turn_on_speech()
    
    elif answer == "off speak":
        return turn_off_speech()

    elif answer == "close browser":
        close_browser()
        return " Closing browser"
    
    elif answer == "open facebook":
        open_facebook()
        return " Opening Facebook"
    
    elif answer == "open google":
        open_google()
        return " Opening Google"
    
    elif answer == "open youtube":
        open_youtube()
        return " Opening Youtube"
    
    elif answer == "open instagram":
        open_instagram()
        return " Opening Instagram"
    
    elif answer == "open discord":
        open_discord()
        return " Opening Discord"
    
    elif answer == "open google drive":
        open_google_drive()
        return " Opening Google Drive"

    elif answer == "change name":
        output(" Okay! What do you want to change my name to?")
        temp = take_input()
        if temp == assistant_details.name:
            return " I am already called " + assistant_details.name + ", right?"
        else:
            update_name(temp)
            assistant_details.name = temp
            return " Now you can call me " + temp

    else:
        output(" Don't know this one, should I check on the internet?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else:
            output(" Can you please tell me what it means?")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "").strip()
                value = get_answer_from_memory(ans)
                if value == "":
                    return " Can't help with this one."
                else:
                    insert_question_and_answer(query, value)
                    return " Thanks, I will remember it for the next time"     
            else:
                return " Can't help with this one."
 

            


if __name__ == "__main__":
    memory_value = get_answer_from_memory("start speaking")
    print(f'Memory response for "start speaking": {memory_value}')

    if memory_value != "on speak":  
        insert_question_and_answer("start speaking", "on speak")
        print("Inserted 'start speaking' -> 'on speak' into memory.")
        memory_value = get_answer_from_memory("start speaking")
        print(f'Updated memory: "start speaking" -> {memory_value}')

    result = process("start speaking")
    print(f'Assistant: {result}')
    
    
    
    
"""
from output_module import output
from time_module import get_time, get_date
from database import get_answer_from_memory, insert_question_and_answer, update_name
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
import assistant_details

def process(query):
    answer = get_answer_from_memory(query)
    
    if answer:
        if answer == "get time details":
            return f"Time is {get_time()}"
        elif answer == "check internet connection":
            return "Internet is connected" if check_internet_connection() else "Internet is not connected"
        elif answer == "tell date":
            return f"Date is {get_date()}"
        elif answer == "change name":
            return change_assistant_name()
        return answer
    
    return handle_unknown_query(query)

def handle_unknown_query(query):
    output("Don't know this one, should I check on the internet?")
    if "yes" in take_input():
        answer = check_on_wikipedia(query)
        if answer:
            return answer
    
    output("Can you please tell me what it means?")
    ans = take_input()
    
    if "it means" in ans:     
        value = get_answer_from_memory(ans.replace("it means", "").strip())
        if value:
            insert_question_and_answer(query, value)
            return "Thanks, I will remember it for the next time"
    
    return "Can't help with this one."

def change_assistant_name():
    output("Okay! What do you want to change my name to?")
    new_name = take_input()
    
    if new_name == assistant_details.name:
        return f"I am already called {assistant_details.name}, right?"
    
    update_name(new_name)
    assistant_details.name = new_name
    return f"Now you can call me {new_name}"
"""






        

